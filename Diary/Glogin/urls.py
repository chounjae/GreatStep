from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'Glogin'

urlpatterns = [
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='account_logout'),
]
