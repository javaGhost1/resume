from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    banner = About.image
    context = {'banner': banner}
    return render(request, 'info/home.html', context)

def about(request):
    return render(request, 'info/about.html')

def resume(request):
    education = Education.objects.all()
    work = Work.objects.all()
    context = {'education': education, 'work': work}
    return render(request, 'info/resume.html', context)
    
def portfolio(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'info/portfolio.html', context)

def contact(request):
    return render(request, 'info/contact.html')