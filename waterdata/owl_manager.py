

# script: owl_manager.py
# class: OWLManager, methods: 
# this script used owlready2 package 
# contains methods for manipulating ontologies with
# high level functionality of owlready2 and dirty features of RDFLib


# imports for OWLManager
# imports for OWLSearch
from owlready2 import *
# imports for RDFGraph
"""
from rdflib import plugin
from rdflib.graph import Graph
from rdflib.store import Store
from rdflib_sqlalchemy import registerplugins
from rdflib.plugin import register
from rdflib.plugin import Parser
from rdflib.plugin import Serializer
from rdflib.namespace import *
from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph
"""




# manager class for hadnling all the ontology related tasks
# such as Laoding and Saving Ontology to Triple Store, Retrieving axioms, 
# Creating and making SPARQL queries, Updating ontology, etc.

# this class contains instances of OWLSearch and RDFLibGraph
# TODO: aggregation VS composition?
class OWLManager:
    
    # constructor initilizes instances of OWLSearch and RDFLibGraph
    def __init__(self):
        self.searcher = OWLSearch()
        #self.rdflib_graph = RDFLibGraph()
        self.onto = self.searcher.onto
        #self.graph = self.rdflib_graph.graph



# class: OWLSearch, methods: get_instances(q):[]
# this class used owlready2 package 
# contains methods for manipulating ontologies with
# high level functionality of owlready
# package for high-level handling of ontology

from .query_processor import QueryParser

# main class for searching through ontology of water
class OWLSearch():


    # constructor, arguments: path of the owl file
    def __init__(self,path="uploads/ontologies/water.owl"):
        self.onto = get_ontology(path).load()
        self.parser = QueryParser()


    # this method takes a query string and returns all the relevant individuals from WaterOnto 
    def get_instances(self,q):        
        # ins is the list of all classes that match the query
        matched_classes = self.onto.search(iri = '*'+q)
        # res is the list of instances of the first of all matched classes 
        individuals = [ str(ins).split('.')[1] for ins in matched_classes[0].instances()]        
        return individuals
    def search_ontology(self,q):
        searched_entities = []
        clean_words = self.parser.remove_stop_words(q)

        # 1. first concatenate all words with _ and search, e.g., Ground_Water_Body
        clean_words = [w.capitalize() for w in clean_words]
        concat_word = "_".join(clean_words)
        
        ## a. search with iri
        searched_entities = list(self.onto.search(iri="*"+concat_word+"*"))
        # 2. search individual terms of the query, e.g., Ground, Water, Body
        if not searched_entities:
            for word in clean_words:       
                searched_entities=list(self.onto.search(iri="*"+word+"*"))

        results = {}
        
        for entity in searched_entities:
            entity_string = str(entity).split('.')[1]
            if entity_string not in results:
                results[entity_string] = self.get_entity_details(entity)

        print(results)
        return results

    """
    import types
    def add_term(self,term):
        with self.onto:
            NewClass = types.new_class(term.capitalize(), (Thing,))
    """



    def get_entity_details(self,entity_class):
        iri = entity_class.iri
        comment = entity_class.comment
        sub_classes = [str(entity).split('.')[1] for entity in entity_class.subclasses()]
        ancestors = [str(entity).split('.')[1] for entity in  entity_class.ancestors()]
        instances = [str(entity).split('.')[1] for entity in entity_class.instances()]

        details = {
            'iri':iri,
            'comment':comment,
            'subclasses':sub_classes,
            'ancestors':ancestors,
            'instances':instances
        }

        return details





        
            
            


# class: RDFGraph, methods: openGraph, createGraph, add_triple,
# query_graph, get_triples, predicates_of, objects_of, subjects_of,
# predicate_objects_of, subject_objects_of, subject_predicates_of



# # class declaration
# class RDFLibGraph():
#     # class attributes
#     # configuration variables for Postgres
#     # TODO: change to Heroku Server
#     store_config_vars ="postgresql+psycopg2://dzhzauideqvjxz:a75420eeaaecace67c5587a1c95a683bc309433d1eaef6c98571d095f924eb83@ec2-54-235-156-60.compute-1.amazonaws.com:5432/d8imng26qfp5hm"
#     # name of triple store
#     store_name = "water_store"
#     #namespaces
#     #WATER =  Namespace()
#     graph = Graph()
#     #constructor
#     def __init__(self):
#         # register RDF/XML parser
#         #register('xml', Parser, 'rdflib.plugins.parsers.rdfxml', 'RDFXMLParser')
#         #registerplugins()
#         # get SQLAlchemy plugin to create a triple store 
#         #self.store = plugin.get("SQLAlchemy", Store)(identifier=self.store_name)
#         #self.openGraph()
#         self.graph.parse("uploads/ontologies/water.owl", format='xml')


#     # get the graph specifying graph_id
#     # open given graph in store
#     def openGraph(self,graph_id="water_onto"):
#         #self.graph = Graph(self.store, identifier=graph_id)
#         #self.graph.open(self.store_config_vars, create=False)
#         pass
        
    
#     # create a new graph in store with given graph id and ontology
#     def createGraph(self,ontology,graph_id="water_onto"):
#         #self.graph = Graph(self.store, identifier=graph_id)
#         #self.graph.open(self.store_config_vars, create=True)
#         #self.graph.parse(ontology, format='xml')
#         pass

#     # add triples to the graph
#     def add_triple(self,s,p,o):
#         #TODO: add code to add a triple the graph
#         self.graph.add((s,p,o))

#     # pass a SPARQL query to the graph
#     def query_graph(self,q):
#         result = self.graph.query(q)
#         return result




#     def regex_search(self,pattern):
#         matched_in_subjects = self.lookup_subjects(pattern)
#         matched_in_objects = self.lookup_objects(pattern )
#         matched_in_predicates = self.lookup_predicates(pattern)
#         matched_in_triples = matched_in_objects + matched_in_predicates + matched_in_subjects
#         return matched_in_triples

#     # look the term in subjects, and return matching triples
#     def lookup_subjects(self,pattern):
#         q = """
#         SELECT * WHERE {  
#             ?s ?p ?o .   
#             FILTER (regex(?s, "pattern","i")) }
#         """
#         q= q.replace("pattern",pattern)
#         results = self.query_graph(q)        
#         str_results = []
#         for r in results:
#             temp = dict()
#             temp['SRC'] = 'WaterOnto'
#             temp['URI'] = str(r[0])
#             temp['LABEL'] = str(r[1])
#             temp['COMMENT'] = str(r[2])
#             str_results.append(temp)
#         return str_results


#     # look the term in objects, and return matching triples
#     def lookup_objects(self,pattern):
#         q = """
#         SELECT * WHERE {  
#             ?s ?p ?o .   
#             FILTER (regex(?o, "pattern","i")) }
#         """
#         q= q.replace("pattern",pattern)
#         results = self.query_graph(q)        
#         str_results = []
#         for r in results:
#             temp = dict()
#             temp['SRC'] = 'WaterOnto'
#             temp['URI'] = str(r[0])
#             temp['LABEL'] = str(r[1])
#             temp['COMMENT'] = str(r[2])
#             str_results.append(temp)
#         return str_results


#     # look the term in predicates, and return matching triples
#     def lookup_predicates(self,pattern):
#         q = """
#         SELECT * WHERE {  
#             ?s ?p ?o .   
#             FILTER (regex(?p, "pattern","i")) }
#         """
#         q= q.replace("pattern",pattern)
#         results = self.query_graph(q)        
#         str_results = []
#         for r in results:
#             temp = dict()
#             temp['SRC'] = 'WaterOnto'
#             temp['URI'] = str(r[0])
#             temp['LABEL'] = str(r[1])
#             temp['COMMENT'] = str(r[2])
#             str_results.append(temp)
#         return str_results

#     def get_triples(self):
#         triples = []
#         for s,p,o in self.graph:
#             triples.append((s,p,o))
#         return triples

#     def list_raw_statements(self):
#         statements = []
#         for row in self.graph:
#             statements.append(str(row))
#         return statements

#     def list_statements(self):
#         statements = []
#         for s,p,o in self.graph:
            
#             s_term = self._get_term(s)
#             p_term = self._get_term(p)
#             o_term = self._get_term(o)
            
#             if s_term and p_term and o_term:
#                 statements.append(s_term+' '+p_term+' '+ o_term )           
#         return statements

#     def _get_term(self,uri):
#         term = None
#         if '#' in uri:
#             terms = str(uri).split('#')
#             if len(terms)>1:
#                 term = terms[1]
#         return term




#     def predicates_of(self,s,o):
#         return self.graph.predicates(s,o) 
    
#     def objects_of(self,s,p):
#         return self.graph.objects(s,p) 

#     def subjects_of(self,p,o):
#         return self.graph.subjects(p,o)

#     def predicate_objects_of(self,s):
#         return self.graph.predicate_objects(s)

#     def subject_objects_of(self,p):
#         return self.graph.subject_objects(p)

#     def subject_predicates_of(self,o):
#         return self.graph.subject_predicates(o)



    




    





        
    













