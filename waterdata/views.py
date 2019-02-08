from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import QueryForm
from .models import Ontology
from django.views import View
from django.views.generic import ListView, DetailView
from .query_processor import QueryParser
from .owl_manager import OWLManager
from .api_manager import APIManager
from .formatters import DataframeFormatter
# TODO: format results page for different ouputs


# cotains methods for performing NLTK operations on query
parser = QueryParser()
# this class creates instances of OWLSearch and RDFLibGraph names rdf and searcher
owl_manager = OWLManager()
# contains mappings and REST api services 
api_manager = APIManager()
# format data returned from APIManager in presentable formats
formatter = DataframeFormatter()


# class that obtains results from different sources and sends it to the template
class ResultView(View):
    # main result view
    template_name = 'waterdata/result.html'
    # input element of html, or search box
    form = QueryForm()

    # get the query by user from the GET parameters (dictionary containing names of elements as the keys)    
    def get(self, request):
        # get the query parameter value named source 
        q = request.GET['source']
        ################################
        #INPUT: query 
        #OUPUT: list of URIs of resources, href to linked data page, list of uris of dbpedia resources


        ###############################
        suggestion = parser.correct_query_italicized(q)
        nouns = parser.get_nouns(q)
        wikipedia_url = 'https://en.wikipedia.org/wiki/'
        #s = owl_manager.rdflib_graph.lookup_objects(q)
        #for l in s:
         #   for i in range(len(l)):
          #      print(l[i])
           #     print(type(l[i]))
         
        uris = []   
        for n in nouns:
            temp = {'title':n,'src':'Wikipedia','desc':wikipedia_url+n}
            uris.append(temp)


        linkedData = [{'title':'First linkedData','src':'SRC 1','desc':'DESC 1'},{'title':'First URI','src':'SRC 1','desc':'DESC 1'},{'title':'First URI','src':'SRC 1','desc':'DESC 1'}]   
        apis = [{'title':'First API','src':'SRC 1','desc':'DESC 1'},{'title':'First URI','src':'SRC 1','desc':'DESC 1'},{'title':'First URI','src':'SRC 1','desc':'DESC 1'}]   
        
        return render(request, self.template_name,{'form':self.form,'suggestion':suggestion,'uris':uris,'linkedData':linkedData,'apis':apis})

class OntologyList(ListView):
    template_name = 'waterdata/ontologies.html'
    model = Ontology

def home(request):
    form = QueryForm()
    return render(request,'waterdata/home.html',{'form':form})
def about(request):
    return render(request,'waterdata/about.html')

def ontology_detail(request,ontology_id):
	ontology = get_object_or_404(Ontology,pk=ontology_id)
	return render(request,'waterdata/ontology_detail.html',{'ontology':ontology})
def water(request):
    return render(request,'waterdata/water.html')

# url for testing purpose
def test(request):
    #rdf = owl_manager.rdflib_graph
    #triples = rdf.lookup_classes()
    #print(triples)
    q_p = QueryParser()
    triples = q_p.get_nouns('Show river flow in the ohio river in America')
    #return render(request,'waterdata/test.html',{'triples':triples})
    return render(request,'waterdata/test.html',{'triples':triples})

# direct uri to the resource from WaterOnto
def get_resource(request,resource_id):
    #parser = QueryParser()
    #res = parser.find_uriref(resource_id)
    #print(len(res))
    #rdf = RDFLibGraph()
    #res = rdf.regex_search(resource_id)
    return HttpResponse("Success")
