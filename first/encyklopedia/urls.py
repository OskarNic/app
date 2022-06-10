from django.urls import path

from . import views
app_name = 'encyklopedia'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:nation_id>/', views.detail, name='detail')
]
