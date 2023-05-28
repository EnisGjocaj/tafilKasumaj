from django.urls import path
from . import views

app_name = 'dev'

urlpatterns = [
    path('dev/', views.index, name='dev-home'),
    
]