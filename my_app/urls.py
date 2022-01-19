from my_app import views
from django.urls import path, include 
from django.contrib import admin


urlpatterns=[
    path('',views.home, name='home_page'),

    path('css/', include('my_app.urls')),
    path('new-search',views.new_search,name-'new_search'),


]