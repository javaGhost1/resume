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
    schools = School.objects.all()
    job_experiences = Job_Experience.objects.all()
    context = {'schools': schools, 'job_experiences': job_experiences}
    return render(request, 'info/resume.html', context)
    
def portfolio(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'info/portfolio.html', context)

def contact(request):
    return render(request, 'info/contact.html')
