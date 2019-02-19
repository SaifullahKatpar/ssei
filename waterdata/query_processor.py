
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
from itertools import chain
from nltk.corpus import wordnet
from .owl_manager import RDFLibGraph
class QueryParser:
    
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
        correct_q = str(b.correct())
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
    
    def get_nouns(self,q):
        doc = self.nlp(q)
        nouns = []
        for token in doc:
            if token.pos_ == 'NOUN' or token.pos_ =='PROPN':
                nouns.append(token.text)
        return nouns

    def remove_stop_words(self,q):
        doc = self.nlp(q)
        words = []
        for token in doc:
            if not token.is_stop:
                words.append(token.text)
        return words

    def get_wiki_urls(self,q):
        words = self.remove_stop_words(q)
        wikipedia_url = 'https://en.wikipedia.org/wiki/'
        dbpedia_url = 'http://dbpedia.org/page/'
        uris = []

        if len(words)>1:            
            main_word = '_'.join(words)
            main_word_title = ' '.join(words)
            temp = {'title':main_word_title,'src':'DBPedia','url':dbpedia_url+main_word,'desc':'description'}
            uris.append(temp)
            temp = {'title':main_word_title,'src':'Wikipedia','url':wikipedia_url+main_word,'desc':'description'}
            uris.append(temp)
        for w in words:
            temp = {'title':w,'src':'Wikipedia','url':wikipedia_url+w,'desc':'description'}
            uris.append(temp)
        for w in words:
            temp = {'title':w,'src':'DBPedia','url':dbpedia_url+w,'desc':'description'}
            uris.append(temp)

        return uris


    def get_dbpedia_urls(self,q):
        words = self.remove_stop_words(q)
        dbpedia_url = 'http://dbpedia.org/page/'
        uris = []
        for w in words:
            temp = {'title':w,'src':'DBPedia','desc':dbpedia_url+ w.capitalize()}
            uris.append(temp)
        return uris

    

    def get_synonyms(self,q):
        words = self.remove_stop_words(q)
        synonym_dict = dict()
        for word in words:
            synonyms = wordnet.synsets(word)
            lemmas = set(chain.from_iterable([w.lemma_names() for w in synonyms]))            
            synonym_dict[word] = lemmas
        return synonym_dict

"""
            diff_lemmas = []
            for w in lemmas:                
                if w!=word:
                    diff_lemmas.append(w)

    def get_def(self,word):
        syns = wordnet.synsets(word)
        return syns[0].definition()

"""
        
        
        
        


    






