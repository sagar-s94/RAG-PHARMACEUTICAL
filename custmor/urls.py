from django.urls import path,include
from . import views
urlpatterns = [
   path("custmorpro/",views.custmor_profile,name="custmorpro"),
   path("prchshistory/",views.prchhistory,name="prchshistory"),
   ]