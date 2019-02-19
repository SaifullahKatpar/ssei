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
#api_manager = APIManager()
# format data returned from APIManager in presentable formats
formatter = DataframeFormatter()


# class that obtains results from different sources and sends it to the template
class ResultView(View):
    # main result view
    template_name = 'waterdata/result.html'
    # input element of html, or search box
    form = QueryForm()
    url = "https://waterservices.usgs.gov/nwis/site/?format=rdb&stateCd=NY"
    content = APIManager().get_content_from_url(url)
    df = formatter.text_to_df(content)
    html_df = formatter.df_to_html(df.iloc[:10,:5])

    # get the query by user from the GET parameters (dictionary containing names of elements as the keys)    
    def get(self, request):
        # get the query parameter value named source 
        q = request.GET['source']
        ################################
        #INPUT: query 
        #OUPUT: list of URIs of resources, href to linked data page, list of uris of dbpedia resources
        suggestion = parser.correct_query_italicized(q)
        synonyms= parser.get_synonyms(q).items()
        count = 0
        for k, v in synonyms:
            for _ in v:
                count+=1
        uris = parser.get_wiki_urls(q)        
        owl_results = owl_manager.rdflib_graph.regex_search(q)

        return render(request, self.template_name,{'form':self.form,'suggestion':suggestion,'synonyms':synonyms,'count':count,'uris':uris,'wateronto':owl_results,'data':self.html_df})

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

def test(request):
    return render(request,'waterdata/test.html')
def get_resource(request):
    return HttpResponse('!')
    