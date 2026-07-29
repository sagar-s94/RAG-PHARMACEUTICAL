from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
  path("",views.login,name="login"),

  path("admin_logout/",views.admin_logout,name="admin_logout"),

  path("dashboard/",views.dashboard,name="dashboard"),

  path("register/",views.register,name="register"),

  path("cu_signup/",views.cu_signup,name="cu_signup"),

  path("cust_login/",views.cust_login,name="cust_login"),

  path("cust_logout/", views.cust_logout, name="cust_logout"),

  path("profile/",views.cust_profile,name="profile"),

  path("cust_home/",views.customer_home,name="customerhome"),

  

  

  path("medicine_detail/",views.medicine_detail,name="medicinedetail"),

  path("delete/<int:id>/", views.delete_detail, name="delete_detail"),

  path("admin_mddetail_card/",views.admin_mddetail_card,name="admin_mddetail_card"),

  

  path("cust_mddetail/",views.detail_card,name="detailcard"),

  path("update_mddetail/",views.update_detail,name="updatedetial"),

  path("med_edit/<int:id>/",views.edit_detail,name="editdetail"),

  # supplier paths

  path("addsuplier/",views.addsupplier,name="addsupplier"),
  path("supplier_list/",views.suppliar_list,name="supplierlist"),
  path("supplier_update/",views.suppliar_update,name="suppliarupdate"),
  path("supplier_edit/<int:supplierid>/",views.suppliar_edit,name="supplier_edit"),
  # urls.py

  path("supplier_delete/<int:supplierid>/", views.supplier_delete, name="supplier_delete"),

  path ("invoice/",views.invoice,name="invoice"),
  path("geninvoice/<int:id>/",views.gen_invoice,name="gen_invoice")



  

]
    
