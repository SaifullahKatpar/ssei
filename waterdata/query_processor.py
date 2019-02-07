
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
import spacy

from .owl_manager import RDFLibGraph
class QueryParser:
    
    words_for_similarity = []
    nlp = spacy.load('en_core_web_sm')

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
        self.words_for_similarity = []
        for word in words:       
            similar_words = word.spellcheck()
            similar_word = str(similar_words[0][0])
            self.words_for_similarity.append(similar_word)
            if word!= similar_word:
                correct_q += '&nbsp<strong><i>'+similar_word+'</i></strong> '
            else:
                correct_q += word+' '
        return correct_q
    
    def get_nouns(self,q):
        doc = self.nlp(q)
        nouns = []
        for token in doc:
            if not token.is_oov and (token.pos_=='NOUN' or token.pos_=='PROPN'):
                nouns.append(token)
        return nouns

    







