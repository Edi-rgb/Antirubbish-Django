from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "AntiRubbish/index.html")

def app(request):
    return render(request, "AntiRubbish/app.html")

def plastic(request):
    return render(request, "AntiRubbish/plastic.html")

def plastic_map(request):
    return render(request, "AntiRubbish/plastic_map.html")

def mancare(request):
    return render(request, "AntiRubbish/mancare.html")

def mancare_map(request):
    return render(request, "AntiRubbish/mancare_map.html")

def hartie(request):
    return render(request, "AntiRubbish/hartie.html")

def hartie_map(request):
    return render(request, "AntiRubbish/hartie_map.html")

def metale(request):
    return render(request, "AntiRubbish/metale.html")

def metale_map(request):
    return render(request, "AntiRubbish/metale_map.html")













    