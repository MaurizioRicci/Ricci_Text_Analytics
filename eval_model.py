from nltk.corpus import treebank
import BERT_model
from pytorch_pretrained_bert import BertTokenizer

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')


class _BertTxtContainer:  # memorizza la frase più lunga che BERT possa valutare
    def __init__(self):
        self.tokN = 0
        self.txt = ''

    def addTxtArr(self, inputTxt):
        tokenized = tokenizer.tokenize(inputTxt)
        if len(tokenized) + self.tokN <= 512:
            self.txt += inputTxt + ' '
            self.tokN += len(tokenized)
            return True
        return False


# calcolo perplexity su PennTreebank
N = len(treebank.sents())
perplexity = []
print('Frasi:', N)
bert_txt = _BertTxtContainer()
c = 0

for sent in treebank.sents()[:N]:
    c += 1
    sentTxt = ' '.join(sent)
    # se ho sforato, calcolo perplexity e inserisco la frase in un nuovo oggetto
    if not bert_txt.addTxtArr(sentTxt):
        perplexity.append(BERT_model.get_score(bert_txt.txt))
        # print('tokN', bert_txt.tokN, 'toks:', bert_txt.txt)
        bert_txt = _BertTxtContainer()
        bert_txt.addTxtArr(sentTxt)
    print(100*c/N, '%')
# finisco di processare l'ultimo testo
perplexity.append(BERT_model.get_score(bert_txt.txt))
# print('tokN', bert_txt.tokN, 'toks:', bert_txt.txt)

print(perplexity)
print('min:', min(perplexity), 'max:', max(perplexity), 'mean:',
      sum(perplexity)/len(perplexity), 'sum:', sum(perplexity))
