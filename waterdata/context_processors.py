from owlready2 import *
# TODO: get this variable from OWL manager class

def water_classes(request):
    # get ontology and load classes for search autocomplete
    onto = get_ontology("uploads/ontologies/water.owl").load()
    #onto = get_ontology("https://raw.githubusercontent.com/SaifullahKatpar/WaterOnto/master/water.owl").load()
    # string representaton of ThingClass types
    classes_list = [ (str(c).split('.')[1]).replace('_',' ') for c in onto.classes() ]
    return {'water_classes':classes_list}