
from django.urls import path
from . import views

urlpatterns = [

    path('',views.index,name= 'index'),
    path('about/',views.about,name= 'about'),
    path('services/',views.services,name= 'services'),
    path('property/',views.property,name= 'property'),
    path('work/',views.work,name= 'work'),
    path('team',views.team,name= 'team'),
    path('contact/',views.contact,name= 'contact'),

  
]