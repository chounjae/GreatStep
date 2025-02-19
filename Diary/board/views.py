# views.py
from django.shortcuts import render , redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post
import openai
from django.conf import settings
import json
from django.views.decorators.csrf import csrf_exempt
#각 페이지마다 로그인 요구 모듈
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib import messages
# 게시글 상세 보기
@login_required(login_url='/accounts/login/')
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'board/post_detail.html', {'post': post})

# 새 게시글 작성
@login_required(login_url='/accounts/login/')
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # 🚨 DB에 바로 저장하지 않음
            post.user = request.user  # ✅ 현재 로그인한 유저 추가
            post.save()  # 저장
            return redirect('board:post_list')
    else:
        form = PostForm()
    return render(request, 'board/post_form.html', {'form': form})


# 게시글 수정
@login_required(login_url='/accounts/login/')
def post_update(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('board:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'board/post_form.html', {'form': form})


@login_required(login_url='/accounts/login/')
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':  # POST 요청일 때만 삭제 처리
        post.delete()
        return redirect('board:post_list')  # 삭제 후 게시글 목록으로 리디렉션
    
    return render(request, 'board/post_confirm_delete.html', {'post': post})

#post_list 페이지에 페이지네이션 기능 추가
@login_required(login_url='/accounts/login/')
def post_list(request):
    if not request.user.is_authenticated:
        return redirect('account_logout')  # 로그인 페이지로 리디렉션

    user = request.user
    posts = Post.objects.filter(user=user).order_by('-id')  # ✅ filter() 사용
    paginator = Paginator(posts, 5)  # 📌 한 페이지에 5개씩
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'board/post_list.html', {'page_obj': page_obj})


@login_required(login_url='/accounts/login/')
def summary(request, pk):
    post = get_object_or_404(Post, pk=pk)  # 게시글 가져오기
    result = None  # 요약 결과 저장 변수

    if request.method == "POST":
        user_content = post.content  # Post 모델의 content 필드 사용

        if user_content:
            prompt = f"""
            입력 받은 문장 한줄로 요약 왠만해선 50자이내 : \n{user_content}
            """

            try:
                client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)  # 최신 방식으로 클라이언트 생성
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "게시물 글 요약하는 AI"},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=100,
                    temperature=0.5
                )
                result = response.choices[0].message.content.strip()  # 요약 결과 저장
            except Exception as e:
                result = f"요약 실패: {str(e)}"  # 에러 메시지를 result에 저장

    return render(request, "board/post_detail.html", {"post": post, "result": result})  # result를 context로 전달