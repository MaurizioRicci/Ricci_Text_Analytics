import torch
from pytorch_pretrained_bert import BertTokenizer, BertForMaskedLM

# OPTIONAL: if you want to have more information on what's happening, activate the logger as follows
import logging
logging.basicConfig(level=logging.INFO)

NUMBER_OF_PREDICTIONS = 100

def predict(text, debug=True):
    # Load pre-trained model tokenizer (vocabulary)
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

    tokenized_text = tokenizer.tokenize(text)
    indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)
    masked_index = tokenized_text.index('[MASK]')

    # Create the segments tensors.
    segments_ids = [0] * len(tokenized_text)

    # Convert inputs to PyTorch tensors
    tokens_tensor = torch.tensor([indexed_tokens])
    segments_tensors = torch.tensor([segments_ids])

    # Load pre-trained model (weights)
    model = BertForMaskedLM.from_pretrained('bert-base-uncased')
    model.eval()

    # Predict all tokens
    with torch.no_grad():
        predictions = model(tokens_tensor, segments_tensors)

    #predicted_index = torch.argmax(predictions[0, masked_index]).item()
    #predicted_token = tokenizer.convert_ids_to_tokens([predicted_index])[0]
    #print(predicted_token)

    predicted_indexes = torch.topk(predictions[0, masked_index], NUMBER_OF_PREDICTIONS)[1]
    predicted_indexes_list = predicted_indexes.tolist()
    predicted_tokens = list(map(lambda idx: tokenizer.convert_ids_to_tokens([idx])[0], predicted_indexes_list))

    if debug:
        print('BERT predicted tokens:', predicted_tokens)

    return predicted_tokens

#predict('[CLS] I want to [MASK] the car because it is cheap . [SEP]')
