from django.urls import path,include
from . import views
urlpatterns = [
   path("custmorpro/",views.custmor_profile,name="custmorpro"),
  
   ]