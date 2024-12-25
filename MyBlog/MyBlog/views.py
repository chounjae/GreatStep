from django.http import HttpResponse
from django.shortcuts import render , redirect
from .models import Post
from MyBlog.forms import PostForm
from .models import Memo

def index(request) :
    return render(request , "index.html")

def diary(request) :
    return render(request , "diary.html")

def memo(request) :
    return render(request , "memo.html")




# 글 작성 페이지
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()  # 글 저장
            return redirect('post_list')  # 글 목록 페이지로 리다이렉트
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

# 글 목록 페이지
def post_list(request):
    posts = Post.objects.all()  # 모든 글 가져오기
    return render(request, 'post_list.html', {'posts': posts})

