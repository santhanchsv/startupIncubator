from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from main.models import Resources , StartUps , Schemes
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage

# Create your views here
def Homee(request):
    startups = StartUps.objects.all()
    context = {
        'startups': startups
    }
    return render(request , 'main/firstPage.html' , context)

def about(request):
    return render(request , 'main/about.html')
def four(request):
    return render(request , 'main/four.html')

def five(request):
    return render(request , 'main/five.html')

def seven(request):
    return render(request , 'main/seven.html')

def eight(request):
    return render(request , 'main/eight.html')

def nine(request):
    return render(request , 'main/nine.html')
def ten(request):
    return render(request , 'main/ten.html')

def leven(request):
    return render(request , 'main/leven.html')
def srh(request):
    return render(request , 'main/srh.html')
def csk(request):
    return render(request , 'main/csk.html')
def govpo(request):
    return render(request , 'main/govpo.html')

def value(request):
    return render(request , 'main/value.html')


def govtSchemes(request):
    schemes = Schemes.objects.all()
    context = {
        'schemes': schemes,
    }
    return render(request , 'main/govtScheme.html' , context)

def reources(request):
    courses = Resources.objects.all()
    context = {
        'courses': courses,
    }
    return render(request , 'main/resources.html' , context)

def topStartUps(request):
    startups = StartUps.objects.all()
    context = {
        'startups': startups,
    }
    return render(request , 'main/startups.html' , context)

def prediction(request):
    return render(request , 'main/Startup-Success-Prediction-using-ML.html')