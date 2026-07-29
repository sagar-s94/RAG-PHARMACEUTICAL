from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
  path("medicine/",views.medicine,name="medicine"),
  path("total_medicine/",views.total_medicine,name="total_medicine"),
  path('allopathy/edit/<int:id>/', views.edit_medicine, name='edit_medicine'),
  path('ayurvedic/edit/<int:id>/',views.edit_ayurvedic,name="edit_ayurvedic"),

  #allopathy
  path("allopathy/add/",views.allopathy_medicine_add,name="allopathy_medicine_add"),
  path("allopathy_medicine_delete/<int:id>/",views.allopathy_medicine_delete,name="allopathy_medicine_delete"),
  path("allopathy/update/",views.allopathy_medicine_update,name="allopathy_medicine_update"),
  path("allopathy/veiwdetail/",views.allopathy_medicine_veiwdetail,name="allopathy_medicine_veiwdetail"),
  #ayurvedic
  path("ayurvedic/add/",views.ayurvedic_medicine_add,name="ayurvedic_medicine_add"),
  path("ayurvedic_medicine_delete/<int:id>/",views.ayurvedic_medicine_delete,name="ayurvedic_medicine_delete"),
  path("ayurvedic/update/",views.ayurvedic_medicine_update,name="ayurvedic_medicine_update"),    
  path("ayurvedic/veiwdetail/",views.ayurvedic_medicine_veiwdetail,name="ayurvedic_medicine_veiwdetail"),
] 