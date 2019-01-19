from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import QueryForm
from .models import Ontology
from django.views import View
from django.views.generic import ListView, DetailView

#from .api_manager import APIManager
#from .formatters import DataframeFormatter
from .query_processor import QueryParser
from .owl_manager import OWLManager
from .api_manager import APIManager
from .formatters import DataframeFormatter
# TODO: format results page for different ouputs

parser = QueryParser()
owl_manager = OWLManager()
api_manager = APIManager()
formatter = DataframeFormatter()


class ResultView(View):
    template_name = 'waterdata/result.html'
    form = QueryForm()
    
    def get(self, request):
        q = request.GET['source']
        # TODO:
        # find subclasses and superclasses in ontology
        # find properties
        # find synonyms in ontology
        res = parser.get_correct_query(q)
        
        return render(request, self.template_name,{'form':self.form,'result':res})
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
    rdf = owl_manager.rdflib_graph
    triples = rdf.list_statements()
    print(triples)
    #return render(request,'waterdata/test.html',{'triples':triples})
    return HttpResponse('Success!')
# direct uri to the resource from WaterOnto
def get_resource(request,resource_id):
    #parser = QueryParser()
    #res = parser.find_uriref(resource_id)
    #print(len(res))
    rdf = RDFLibGraph()
    res = rdf.regex_search(resource_id)
    return HttpResponse(res)
