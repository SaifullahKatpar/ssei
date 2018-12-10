from owlready2 import *

class OWLReady():
	ontology_path = 'uploads/ontologies/'

	def __init__(self):
		self.onto = get_ontology(self.ontology_path+"water.owl").load()

	def list_classes(self):
		return list(self.onto.classes())

	def list_individuals(self):
		return list(self.onto.individuals())

	def list_object_properties(self):
		return list(self.onto.object_properties())

	def list_data_properties(self):
		return list(self.onto.data_properties())

	def list_annotation_properties(self):
		return list(self.onto.annotation_properties())

	def list_properties(self):
		return list(self.onto.annotation_properties())

	def list_disjoint_classes(self):
		return list(self.onto.disjoint_classes())

	def list_disjoint_properties(self):
		return list(self.onto.disjoint_properties())

	def list_disjoints(self):
		return list(self.onto.disjoints())

	def list_different_individuals(self):
		return list(self.onto.different_individuals())

	def list_get_namepace(self,base_iri):
		return list(self.onto.get_namepace(base_iri))