from django.urls import path, include
from main import views

urlpatterns = [
    path('' , views.Homee , name = 'Homee'),
    path('about/' , views.about , name = 'about'),
    path('startups/' , views.topStartUps , name = 'top-startups'),
    path('schemes/' , views.govtSchemes , name = 'schemes'),
    path('resources/' , views.reources , name = 'resources'), 
    path('predict/' , views.prediction , name = 'prediction'),
    path('value/' , views.value , name = 'value'),
     path('four/' , views.four , name = 'four'),
     path('five/' , views.five , name = 'five'),
     path('seven/' , views.seven , name = 'seven'),
     path('eight/' , views.eight , name = 'eight'),
     path('nine/' , views.nine , name = 'nine'),
     path('ten/' , views.ten , name = 'ten'),
     path('leven/' , views.leven , name = 'leven'),
     path('srh/' , views.srh , name = 'srh'),
     path('csk/' , views.csk , name = 'csk'),
      path('govpo/' , views.govpo , name = 'govpo'),


]