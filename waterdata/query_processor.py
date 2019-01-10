

import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag


nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def preprocess(sent):
    sent = word_tokenize(sent)
    sent = pos_tag(sent)
    return sent
