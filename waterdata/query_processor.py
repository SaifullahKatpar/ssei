
''' 
# script: query_processor.py 
# class: QueryManager
# methods: 
#       - preprocess
#       - 
 '''
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import wordnet
from autocorrect import spell

class QueryManager:

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

    
    
    
    '''     
        CC coordinating conjunction
        CD cardinal digit
        DT determiner
        EX existential there (like: “there is” … think of it like “there exists”)
        FW foreign word
        IN preposition/subordinating conjunction
        JJ adjective ‘big’
        JJR adjective, comparative ‘bigger’
        JJS adjective, superlative ‘biggest’
        LS list marker 1)
        MD modal could, will
        NN noun, singular ‘desk’
        NNS noun plural ‘desks’
        NNP proper noun, singular ‘Harrison’
        NNPS proper noun, plural ‘Americans’
        PDT predeterminer ‘all the kids’
        POS possessive ending parent’s
        PRP personal pronoun I, he, she
        PRP$ possessive pronoun my, his, hers
        RB adverb very, silently,
        RBR adverb, comparative better
        RBS adverb, superlative best
        RP particle give up
        TO, to go ‘to’ the store.
        UH interjection, errrrrrrrm
        VB verb, base form take
        VBD verb, past tense took
        VBG verb, gerund/present participle taking
        VBN verb, past participle taken
        VBP verb, sing. present, non-3d take
        VBZ verb, 3rd person sing. present takes
        WDT wh-determiner which
        WP wh-pronoun who, what
        WP$ possessive wh-pronoun whose
        WRB wh-abverb where, when
    '''    
    # takes a sentence and does the following:
    #   - tokenize
    #   - part-of-speech tagging POS 
    #   - spell correction
    # returns a list of tuples cotaning word and POS tag
    def preprocess(self, sent):       
        words = sent.split()
        correct_words = []
        for word in words:
            # if word is alphabetical, get its correct spelling
            if word.isalpha():
                correct_words.append(spell(word))
            # otherwise, append the word to correct words list
            else:
                correct_words.append(word)
        # convert list to string separated by spaces
        correct_sent = ' '.join(correct_words)
        # tokens of the string
        tokenized_sent = word_tokenize(correct_sent)
        # (token, POS-tag) tuples
        pos_tagged_sent = pos_tag(tokenized_sent)
        return pos_tagged_sent

    # get words similar in meaning to the query word
    # optional pos is the part of speech of the word
    def get_synonyms(self,word, pos=None):
        wordnet_pos = {
            "NOUN": wordnet.NOUN,
            "VERB": wordnet.VERB,
            "ADJ": wordnet.ADJ,
            "ADV": wordnet.ADV
        }
        if pos:
            synsets = wordnet.synsets(word, pos=wordnet_pos[pos])
        else:
            synsets = wordnet.synsets(word)
        synonyms = []
        for synset in synsets:
            synonyms += [str(lemma.name()) for lemma in synset.lemmas()]
        synonyms = [synonym.replace("_", " ") for synonym in synonyms]
        synonyms = list(set(synonyms))
        synonyms = [synonym for synonym in synonyms if synonym != word]
        return synonyms

#    def match_classes(self, word):
