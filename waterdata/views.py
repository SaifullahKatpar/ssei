from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .forms import QueryForm
from .models import Ontology

from django.views import View
from django.views.generic import ListView, DetailView
#from owlready2 import *
#from .owl_search import OWLSearch
#from .owl_store import RDFGraph



# TODO: format results page for different ouputs
class ResultView(View):
    template_name = 'waterdata/result.html'
    form = QueryForm()
    def get(self, request):
        q = request.GET['source']
        return render(request, self.template_name,{'form':self.form,'query':q})




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