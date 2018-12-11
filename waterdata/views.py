from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.files import File
from .forms import QueryForm
from .models import Ontology
import parser


def home(request):
    form = QueryForm()
    return render(request,'waterdata/home.html',{'form':form})

def about(request):
    	return render(request,'waterdata/about.html')

def ontologies(request):
    ontologies = Ontology.objects
    return render(request,'waterdata/ontologies.html',{'ontologies':ontologies})

def ontology_detail(request,ontology_id):
	ontology = get_object_or_404(Ontology,pk=ontology_id)
	return render(request,'waterdata/ontology_detail.html',{'ontology':ontology})

def water(request):
    return render(request,'waterdata/water.html')
