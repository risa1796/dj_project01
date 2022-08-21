from django.urls import path
from . import views


urlpatterns = [

    path('', views.inputdata , name='inputdata'),
    path('result/', views.result, name='result'),
   
]