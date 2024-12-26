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


#memo.html에서 작성한 텍스트들 객체에 저장 및 리다이렉트
def memo(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        
        Memo.objects.create(title = title , content = content)
        
        return redirect('diary')
    
    return render(request , 'memo.html')


#memo에서 작성한 내용들 가져오기
def diary(request):
    #Memo.objects.all()으로 모든 메모를 가져옴 , order_by~~~으로 최신순 정렬 
    memos = Memo.objects.all().order_by('-created_at')  # 최신 메모 순으로 정렬
    return render(request, 'diary.html', {'memos': memos})