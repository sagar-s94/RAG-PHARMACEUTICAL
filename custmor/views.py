from django.shortcuts import render
from dashboard.models import cusignup

# Create your views here.
def custmor_profile(request):
    cusignups=cusignup.objects.all()


    return render(request,"custmorpro.html",{"cusignups": cusignups})

