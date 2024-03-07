from django.urls import path  #App_urls.py
from . import views  # Import your views

urlpatterns = [
    path('nam/',views.nam,name='nam'),
    path('name/',views.name,name='name'),
    path('home/',views.home,name='home'),
    path('login_view/',views.login_view,name='login_view'),
    path('send_email/',views.send_email,name='send_email'),
    path('vose/',views.vose,name='vose'),
    path('page/',views.page,name='page'),
    #path('',views.name,name=''),
    path('',views.fine,name='fine')

    ]