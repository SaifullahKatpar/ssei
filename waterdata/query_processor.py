
# script: query_processor.py 
# class: QueryManager
# methods: 
#       - preprocess
#       - 

import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from autocorrect import spell

class QueryManager:

    def __init__(self):
        # Punkt Tokenizer Models from NLTK
        #nltk_deps = ['punkt', 'averaged_perceptron_tagger']
        #map(nltk.download, nltk_deps)
        try:
            nltk.data.find('punkt.zip')
            nltk.data.find('averaged_perceptron_tagger.zip')
        except LookupError:
            nltk.download('punkt')
            nltk.download('averaged_perceptron_tagger')
    
    
    # takes a sentence and does the following:
    #   - tokenize
    #   - part-of-speech tagging POS 
    #   - spell correction
    def preprocess(self, sent):       
        words = sent.split()
        correct_words  =  [spell(word) for word in words]
        correct_sent = ' '.join(correct_words)
        tokenized_sent = word_tokenize(correct_sent)
        pos_tagged_sent = pos_tag(tokenized_sent)
        return pos_tagged_sent
