from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import QueryForm
from .models import Ontology
from django.views import View
from django.views.generic import ListView, DetailView

#from .api_manager import APIManager
#from .formatters import DataframeFormatter
from .query_processor import QueryManager

# TODO: format results page for different ouputs
class ResultView(View):
    template_name = 'waterdata/result.html'
    form = QueryForm()
    
    def get(self, request):
        q = request.GET['source']
        #url = request.GET['source']
        #url = "https://waterservices.usgs.gov/nwis/site/?format=rdb&stateCd=NY"
        #content = APIManager().get_content_from_url(url)
        #df = DataframeFormatter().text_to_df(content)
        #html = DataframeFormatter().df_to_html(df)
        #return HttpResponse(html)
        res  = QueryManager().preprocess(q)
        return HttpResponse(res)
        #return render(request, self.template_name,{'form':self.form,'query':q})
''' def suggest(request):
    word = request.GET.get('source', None)
    ins = onto.search(iri = '*'+word)
 '''    
class OntologyList(ListView):
    template_name = 'waterdata/ontologies.html'
    model = Ontology
""" class OntologyDetail(DetailView):
    context_object_name = 'ontology'
    queryset = Ontology.objects.all()
 """
def home(request):
    form = QueryForm()
    return render(request,'waterdata/home.html',{'form':form})
def about(request):
    return render(request,'waterdata/about.html')
""" def ontologies(request):
    ontologies = Ontology.objects
    return render(request,'waterdata/ontologies.html',{'ontologies':ontologies})
 """
def ontology_detail(request,ontology_id):
	ontology = get_object_or_404(Ontology,pk=ontology_id)
	return render(request,'waterdata/ontology_detail.html',{'ontology':ontology})
def water(request):
    return render(request,'waterdata/water.html')

def test(request):
    return render(request,'waterdata/test.html')

def spell(request):
    return render(request,'waterdata/spell.html')
