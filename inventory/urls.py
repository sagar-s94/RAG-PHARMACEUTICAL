from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
   
    path("stockout/",views.stockout,name="stockout"),
    path("stockout_qty/",views.stockout_qty,name="stockoutqty"),
    path("stockout_update/",views.stockout_update,name="stockoutupdate"),
    path("stockout_edit/<int:id>/",views.stockout_edit,name="stockoutedit"),
    path("stockout_delete/<int:id>/",views.stockout_delete,name='stockoutdelete'),

    path("stockin/",views.stockin,name="stockin"),
    path("stockqty/",views.stockqty,name="stockqty"),
    path("stock_update/",views.update_stock,name="update_stock"),
    path("stock_edit/<int:id>/",views.stock_edit,name="stockedit"),
    path("stock_delete/<int:id>/", views.delect_stock, name="stockdelete"),

    
    
]