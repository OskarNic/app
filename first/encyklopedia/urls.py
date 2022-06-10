from django.urls import path
from django.template import loader

from . import views
app_name = 'encyklopedia'

urlpatterns = [
    
    path('', views.index, name='index'),

    path('nation/', views.nation, name='nation'),

    path('tanks/', views.tanks, name='tanks'),

    path('types/', views.types, name='types'),


    #path('<int:nation_id>/tanks/', views.tanks, name='tanks'),

    #path('<int:nation_id>/type/', views.type, name='type'),
]