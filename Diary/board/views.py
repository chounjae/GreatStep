# views.py
from django.shortcuts import render , redirect, get_object_or_404
from .models import Post
from .forms import PostForm
# 게시글 목록을 템플릿에 전달
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'board/post_list.html', {'posts': posts})

# 게시글 상세 보기
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'board/post_detail.html', {'post': post})

# 새 게시글 작성
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('board:post_list')
    else:
        form = PostForm()
    return render(request, 'board/post_form.html', {'form': form})

# 게시글 수정
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

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':  # POST 요청일 때만 삭제 처리
        post.delete()
        return redirect('board:post_list')  # 삭제 후 게시글 목록으로 리디렉션
    
    return render(request, 'board/post_confirm_delete.html', {'post': post})