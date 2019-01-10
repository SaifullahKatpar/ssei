# script: owl_store.py
# class: OWLSearch, methods: get_instances(q):[]
# this script used owlready2 package 
# contains methods for manipulating ontologies with
# high level functionality of owlready


# package for high-level handling of ontology
from owlready2 import *


# main class for searching through ontology of water
class OWLSearch:

    # constructor, arguments: path of the owl file
    def __init__(self,path="uploads/ontologies/water.owl"):
        self.onto = get_ontology(path).load()



    def get_instances(self,q):        
        # ins is the list of all classes that match the query
        matched_classes = self.onto.search(iri = '*'+q)
        # res is the list of instances of the first of all matched classes 
        individuals = [ str(ins).split('.')[1] for ins in matched_classes[0].instances()]        
        return individuals

