from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import QueryForm
from .models import Ontology
from django.views import View
from django.views.generic import ListView, DetailView
from .owl_manager import OWLManager
from .query_processor import QueryParser
# TODO: format results page for different ouputs


# this class creates instances of OWLSearch and RDFLibGraph names rdf and searcher
owl_manager = OWLManager()
# contains mappings and REST api services 
#api_manager = APIManager()
parser  = QueryParser()

current_term = ''
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
        current_term = q        
        ################################
        #INPUT: query 
        #OUPUT: list of URIs of resources, href to linked data page, list of uris of dbpedia resources
        count = 0
        #owl_results = owl_manager.rdflib_graph.regex_search(q)
        synonyms,count = parser.get_synonyms(q)
        print(synonyms)
        owl_results = owl_manager.searcher.search_ontology(q)
        return render(request, self.template_name,{'form':self.form,'q':q,'suggestion':None,'synonyms':synonyms,'count':count,'uris':None,'wateronto':owl_results,'data':None})

class OntologyList(ListView):
    template_name = 'waterdata/ontologies.html'
    model = Ontology

def home(request):
    form = QueryForm()
    return render(request,'waterdata/home.html',{'form':form})
def about(request):
    return render(request,'waterdata/about.html')

from django.shortcuts import redirect


"""
def add(request):
    owl_manager.searcher.add_term(current_term)
    return redirect('waterdata/result.html')
"""

def ontology_detail(request,ontology_id):
	ontology = get_object_or_404(Ontology,pk=ontology_id)
	return render(request,'waterdata/ontology_detail.html',{'ontology':ontology})
def water(request):
    return render(request,'waterdata/water.html')

def test(request):
    return render(request,'waterdata/test.html')
def get_resource(request):
    return HttpResponse('!')
    