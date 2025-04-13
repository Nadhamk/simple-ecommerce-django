
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path("",views.register),
    path("login",views.login,name="login"),
    path("registerview",views.registerview,name='registerview'),
    path("loginaccount",views.loginaccount),
    path("delete/<id>",views.deleteData,name="deletedata"),
    path("delete2/<id>",views.deleteUser,name="deleteuser"),
    path("admin",views.admin),
    path("user",views.user),
    path("check",views.check),
    path("product",views.product),
    path("productview",views.productview),
    path("productdisplay",views.productdisplay),
    path("delete1/<id>",views.deleteProduct,name="deleteproduct"),
    path("myprofile",views.myprofile,name='myprofile'),
    path("buy",views.buy),
    path("logout",views.logoutuser,name='logout'),
    path("myorder",views.myorder),
    path("delete3/<id>",views.deleteorder,name="deleteorder"),
    path("edit/<str:pk>",views.updateData,name="updateData"),
    
]



