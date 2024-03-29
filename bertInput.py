from nltk.tokenize import word_tokenize
from pytorch_pretrained_bert import BertTokenizer
import string
import json

tokenizer = BertTokenizer.from_pretrained('bert-base-cased')
# 400K voci -> 4Mb. Ottenuto da https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json
myDict = json.load(open("myLargeDict.json", "r"))
affixes = ['\'d', '\'s', 'n\'t']

def tok_in_dict(tok):
    # controllo nel dizionario di BERT, poi in uno più grande, infine controllo che sia un numero
    # BERT ha dei numeri nel suo dizionario ma solo interi
    return (tok in affixes) or (tok in tokenizer.vocab) \
           or (tok.lower() in myDict) or (tok.replace('.', '').isdigit())


def format_str(text, debug=True):
    #text = 'I want to buy the car becaeuse it is cheap.'
    tokenized_text = word_tokenize(text)

    if debug:
        print('Tokenized text:', tokenized_text)

    unk_words = []

    for i in range(len(tokenized_text)):
        tok = tokenized_text[i]  # .lower()
        if not tok_in_dict(tok):
            unk_words.append(tok)
            tokenized_text[i] = '[MASK]'

    str = ' '.join(tokenized_text)
    bert_text = '[CLS] %s [SEP]' % str

    if debug:
        print('BERT input:', bert_text)

    if debug:
        print('Unk words:', unk_words)

    return bert_text, unk_words
