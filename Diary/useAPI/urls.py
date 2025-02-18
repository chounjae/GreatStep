from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'useAPI'

urlpatterns = [
    path('summary/', views.summary, name='summary'),
]
