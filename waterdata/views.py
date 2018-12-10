from django.shortcuts import render
from .forms import QueryForm


def home(request):
    form = QueryForm()
    return render(request,'waterdata/home.html',{'form':form})

def about(request):
    	return render(request,'waterdata/about.html')
