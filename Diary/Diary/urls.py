from django.contrib import admin

from django.urls import path, include
from . import views



app_name ='Diary'
urlpatterns = [
    path('django_admin_is_very_important_url_so_you_should_lock_this_url/', admin.site.urls),
    path('',views.index),
    path('board/',include('board.urls')),
    path('accounts/' , include('allauth.urls')),
    path('useAPI/' , include('useAPI.urls')),

]
