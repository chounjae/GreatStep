from django.contrib import admin
from django.urls import path
from . import views
app_name ='board'


urlpatterns = [
    path('', views.post_list, name='post_list'),  # 게시글 목록
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),  # 게시글 상세 보기
    path('posts/new/', views.post_create, name='post_create'),  # 새 게시글 작성
    path('posts/<int:pk>/edit/', views.post_update, name='post_update'),  # 게시글 수정
    path('posts/<int:pk>/delete/', views.post_delete, name='post_delete'),  # 게시글 삭제
]
