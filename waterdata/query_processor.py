
''' 
# script: query_processor.py 
# class: QueryManager
# methods: 
#       - preprocess
#       - 
 '''
import nltk
from textblob import TextBlob
from textblob import Word

from .owl_manager import RDFLibGraph
class QueryParser:

    def __init__(self):
        # Punkt Tokenizer Models from NLTK
        #nltk_deps = ['punkt', 'averaged_perceptron_tagger']
        #map(nltk.download, nltk_deps)
        try:
            nltk.data.find('wordnet.zip')
            nltk.data.find('punkt.zip')
            nltk.data.find('averaged_perceptron_tagger.zip')
        except LookupError:
            nltk.download('wordnet')
            nltk.download('punkt')
            nltk.download('averaged_perceptron_tagger')

    def get_language(self,q):
        b = TextBlob(q)
        lang = b.detect_language()
        return lang

    def translate_to(self,q,lang):
        src = TextBlob(q)
        src.translate(to=lang)
        return src
    
    def correct_query_all(self,q):
        b = TextBlob(q)
        correct_q = b.correct()
        return correct_q

    def correct_query_italicized(self,q):
        sentence = TextBlob(q)
        words = sentence.words
        correct_q = ''
        for word in words:       
            similar_words = word.spellcheck()
            similar_word = str(similar_words[0][0])

            if word!= similar_word:
                correct_q += '&nbsp<strong><i>'+similar_word+'</i></strong> '
            else:
                correct_q += word+' '
        return correct_q
    
    
    





