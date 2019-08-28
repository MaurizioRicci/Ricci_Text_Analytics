import math

import torch
from pytorch_pretrained_bert import BertTokenizer, BertForMaskedLM

# OPTIONAL: if you want to have more information on what's happening, activate the logger as follows
import logging
logging.basicConfig(level=logging.INFO)

NUMBER_OF_PREDICTIONS = 100

# Load pre-trained model tokenizer (vocabulary)
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
# Load pre-trained model (weights)
model = BertForMaskedLM.from_pretrained('bert-base-uncased')
model.eval()


def predict(text, debug=True):

    tokenized_text = tokenizer.tokenize(text)
    indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)
    masked_index = tokenized_text.index('[MASK]')

    # Create the segments tensors.
    segments_ids = [0] * len(tokenized_text)

    # Convert inputs to PyTorch tensors
    tokens_tensor = torch.tensor([indexed_tokens])
    segments_tensors = torch.tensor([segments_ids])

    # Predict all tokens
    with torch.no_grad():
        predictions = model(tokens_tensor, segments_tensors)

    # predicted_index = torch.argmax(predictions[0, masked_index]).item()
    # predicted_token = tokenizer.convert_ids_to_tokens([predicted_index])[0]
    # print(predicted_token)

    predicted_indexes = torch.topk(predictions[0, masked_index], NUMBER_OF_PREDICTIONS).indices
    predicted_indexes_list = predicted_indexes.tolist()
    predicted_tokens = list(map(lambda idx: tokenizer.convert_ids_to_tokens([idx])[0], predicted_indexes_list))

    if debug:
        print('BERT predicted tokens:', predicted_tokens)

    return predicted_tokens


# def computeProbOverSuggestions(predictions, masked_index):
#     # computa la prob per ogni ids e risolve gli ids
#     softamax_sorted = torch.softmax(predictions[0, masked_index], 0).sort(descending=True)
#     softamax_sorted_values = softamax_sorted.values
#
#     prob_list = softamax_sorted_values.tolist()
#     index_list = softamax_sorted.indices.tolist()
#     res = []
#     for c in range(len(index_list)):
#         data = {'index':None, 'prob': None}
#         data['index'] = index_list[c]
#         data['prob'] = prob_list[c]
#         res.append(data)
#
#     for c in range(len(res)):
#         res[c]['tok'] = tokenizer.convert_ids_to_tokens([[res[c]['index']]][0])
#     return res

#predict('[CLS] I want to [MASK] the car because it is cheap . [SEP]')


def get_score(sentence):
    if sentence.strip() == '':
        raise Exception('Expected sentence, got empty string')
    sentence = sentence.lower()
    tokenize_input = tokenizer.tokenize(sentence)
    tensor_input = torch.tensor([tokenizer.convert_tokens_to_ids(tokenize_input)])
    predictions = model(tensor_input)
    loss_fct = torch.nn.CrossEntropyLoss()
    loss = loss_fct(predictions.squeeze(), tensor_input.squeeze()).data
    return math.exp(loss)  # calcola perplexity
