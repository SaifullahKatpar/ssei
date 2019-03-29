
''' 
# script: query_processor.py 
# class: QueryManager
# methods: 
#       - preprocess
#       - 
 '''
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 


from textblob import TextBlob
from textblob import Word
from itertools import chain
from nltk.corpus import wordnet
#from .owl_manager import RDFLibGraph
class QueryParser:
    
    def __init__(self):
        # Punkt Tokenizer Models from NLTK
        #nltk_deps = ['punkt', 'averaged_perceptron_tagger']
        #map(nltk.download, nltk_deps)
        try:
            nltk.data.find('wordnet.zip')
            nltk.data.find('punkt.zip')
            nltk.data.find('averaged_perceptron_tagger.zip')
            nltk.data.find('stopwords.zip')

        except LookupError:
            nltk.download('wordnet')
            nltk.download('punkt')
            nltk.download('averaged_perceptron_tagger')
            nltk.download('stopwords')

    def remove_stop_words(self, sentence):
        stop_words = set(stopwords.words('english')) 
        word_tokens = word_tokenize(sentence) 
        filtered_sentence = [w for w in word_tokens if not w in stop_words]         
        filtered_sentence = [] 
        for w in word_tokens: 
            if w not in stop_words: 
                filtered_sentence.append(w) 
        return filtered_sentence

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
    

    """
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
    
"""
    def get_synonyms(self,q):
        words = q.split(' ')
        synonym_dict = dict()
        for word in words:
            synonyms = wordnet.synsets(word)
            lemmas = set(chain.from_iterable([w.lemma_names() for w in synonyms]))                        
            synonym_dict[word] = list(lemmas)
        return synonym_dict

    def get_synonyms(self,q):
        words = q.split(' ')
        synonym_dict = dict()
        count = 0
        for word in words:
            synonyms = wordnet.synsets(word)
            lemmas = set(chain.from_iterable([w.lemma_names() for w in synonyms]))                        
            count+= len(lemmas)
            synonym_dict[word] = list(lemmas)
        return synonym_dict,count

    word_list = ['water','irrigation','river','country','geography','weather','air','ice','measurement','size','number']

    def get_sim(self,q):
        synset_words = [wordnet.synset(word+'.n.01') for word in self.word_list]
        similarities = []
        for word in q.split():
            word = wordnet.synset(word+'.n.01')
            for word_to_match in synset_words:
                similarities.append(word.wup_similarity(word_to_match))
        return any( i>0.30 for i in similarities)

