from owlready2 import *

# get the instances of a given OWL class
def get_owl_instances(owl_class):
    onto = get_ontology("uploads/ontologies/water.owl").load()
    ins = onto.search(iri = owl_class)
    return ins 

