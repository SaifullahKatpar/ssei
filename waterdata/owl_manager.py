

# script: owl_manager.py
# class: OWLManager, methods: 
# this script used owlready2 package 
# contains methods for manipulating ontologies with
# high level functionality of owlready2 and dirty features of RDFLib


# imports for OWLManager
# imports for OWLSearch
from owlready2 import *
# imports for RDFGraph
from rdflib import plugin
from rdflib.graph import Graph
from rdflib.store import Store
from rdflib_sqlalchemy import registerplugins
from rdflib.plugin import register
from rdflib.plugin import Parser
from rdflib.plugin import Serializer





# manager class for hadnling all the ontology related tasks
# such as Laoding and Saving Ontology to Triple Store, Retrieving axioms, 
# Creating and making SPARQL queries, Updating ontology, etc.

# this class contains instances of OWLSearch and RDFLibGraph
# TODO: aggregation VS composition?
class OWLManager:
    
    # constructor initilizes instances of OWLSearch and RDFLibGraph
    def __init__(self):
        self.searcher = OWLSearch()
        self.rdflib_graph = RDFLibGraph() 



# class: OWLSearch, methods: get_instances(q):[]
# this class used owlready2 package 
# contains methods for manipulating ontologies with
# high level functionality of owlready
# package for high-level handling of ontology


# main class for searching through ontology of water
class OWLSearch():

    # constructor, arguments: path of the owl file
    def __init__(self,path="uploads/ontologies/water.owl"):
        self.onto = get_ontology(path).load()


    # this method takes a query string and returns all the relevant individuals from WaterOnto 
    def get_instances(self,q):        
        # ins is the list of all classes that match the query
        matched_classes = self.onto.search(iri = '*'+q)
        # res is the list of instances of the first of all matched classes 
        individuals = [ str(ins).split('.')[1] for ins in matched_classes[0].instances()]        
        return individuals

# class: RDFGraph, methods:



# class dec
class RDFLibGraph():
    # class attributes
    # configuration variables for Postgres
    # TODO: change to Heroku Server
    store_config_vars ="postgresql+psycopg2://postgres:saif666?@localhost:5432/watertestdb"
    # name of triple store
    store_name = "water_store"
    #namespaces
    #WATER =  Namespace()

    #constructor
    def __init__(self):
        # register RDF/XML parser
        register('xml', Parser, 'rdflib.plugins.parsers.rdfxml', 'RDFXMLParser')
        registerplugins()
        # get SQLAlchemy plugin to create a triple store 
        self.store = plugin.get("SQLAlchemy", Store)(identifier=self.store_name)        

    # get the graph specifying graph_id
    # open given graph in store
    def openGraph(self,graph_id="water_onto"):
        self.graph = Graph(self.store, identifier=graph_id)
        self.graph.open(self.store_config_vars, create=False)
        
    
    # create a new graph in store with given graph id and ontology
    def createGraph(self,ontology,graph_id="water_onto"):
        self.graph = Graph(self.store, identifier=graph_id)
        self.graph.open(self.store_config_vars, create=True)
        self.graph.parse(ontology, format='xml')
    
    # add triples to the graph
    def add_triple(self,s,p,o):
        #TODO: add code to add a triple the graph
        self.graph.add((s,p,o))

    def query_graph(self,q):
        result = self.graph.query("select * where {?s ?p ?o} limit 5")
        return result

    def get_triples(self):
        return self.graph.triples()

    def predicates_of(self,s,o):
        return self.graph.predicates(s,o) 
    
    def objects_of(self,s,p):
        return self.graph.objects(s,p) 

    def subjects_of(self,p,o):
        return self.graph.subjects(p,o)

    def predicate_objects_of(self,s):
        return self.graph.predicate_objects(s)

    def subject_objects_of(self,p):
        return self.graph.subject_objects(p)

    def subject_predicates_of(self,o):
        return self.graph.subject_predicates(o)



    




    





        
    













