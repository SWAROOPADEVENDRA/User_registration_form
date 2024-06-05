from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from app.models import *

from app.forms import *

from django.core.mail import send_mail

def registration(request):
    d={'EUDO':UserForm(),'EPDO':ProfileForm()}
    if request.method=='POST' and request.FILES:
        NMUFDO=UserForm(request.POST)
        NMPFDO=ProfileForm(request.POST,request.FILES)

        if NMUFDO.is_valid() and NMPFDO.is_valid():
            MUFDO=NMUFDO.save(commit=False)
            pw=NMUFDO.cleaned_data['password']
            MUFDO.set_password(pw)
            MUFDO.save()

            MPFDO=NMPFDO.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()

            send_mail('Registration',
                      'Thank you for your registration',
                      'anushareddypavan@gmail.com',
                      [MUFDO.email],
                      fail_silently=False,
                      )
            return HttpResponse('Registration is successfull')
        else:
            return HttpResponse('Invalid data')
    return render(request,'registration.html',d)