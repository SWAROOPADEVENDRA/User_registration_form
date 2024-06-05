from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from app.models import *

from app.forms import *

def registration(request):
    d={'EUDO':UserForm(),'EPDO':ProfileForm()}
    
    return render(request,'registration.html',d)