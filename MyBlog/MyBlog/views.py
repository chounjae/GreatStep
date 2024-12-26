from django.http import HttpResponse
from django.shortcuts import render , redirect , get_object_or_404
from .models import Post
from MyBlog.forms import PostForm
from .models import Memo
from django.core.paginator import Paginator

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


#memo에서 작성한 내용들 가져오기 , 페이지네이션
def diary(request):
    #Memo.objects.all()으로 모든 메모를 가져옴 , order_by~~~으로 최신순 정렬 
    memos = Memo.objects.all().order_by('-created_at')  # 최신 메모 순으로 정렬
    paginator = Paginator(memos , 5) #한 페이지에 5개 객체
    page_number = request.GET.get('page') #페이지 번호를 get 요청에서 가져오기
    page_obj = paginator.get_page(page_number) #해당 페이지의 메모 객체 가져오기
        
    return render(request, 'diary.html', {'page_obj': page_obj})

#특정 메모 id를 찾아서 반환하는 형식
def memo_detail(request , id):
    memo = get_object_or_404(Memo , id = id)
    return render(request , 'memo_detail.html' , {'memo' : memo})


