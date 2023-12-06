from django.shortcuts import render
from django.http import HttpResponse

from models import Voiture

def index(request):
    voitureapp = Voiture.object.all()
    return render(request, 'voitureapp/index.html', {'voitureapp': voitureapp})