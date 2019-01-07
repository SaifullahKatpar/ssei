from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import QueryForm
from .models import Ontology
from django.views import View
from django.views.generic import ListView, DetailView

class ResultView(View):
    template_name = 'waterdata/result.html'
    form = QueryForm()
    def get(self, request):
        res = request.GET['source']
        return render(request, self.template_name,{'form':self.form,'query':res})

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