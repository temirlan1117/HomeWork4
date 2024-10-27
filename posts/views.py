from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import PostForm, CommentForm
from .models import Post
from django.shortcuts import redirect


def http_response(request):
    return HttpResponse("Hello World, from http")

def html_response(request):
    return render(request, "index.html")
@login_required(login_url='/login/')
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})
@login_required(login_url='/login/')
def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    form = CommentForm()

    return render(request, 'posts/post_detail.html', {'post': post,'form': form} )
@login_required(login_url='/login/')
def post_create_view(request ):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'posts/post_create.html' , {'form': form} )
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if not form.is_valid():
           return render(request,'posts/post_create.html' , {'form': form} )
        post = form.save()
        post.user = request.user
        post.save()
        return redirect('/posts/')

def comment_create_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()
    return render(request, 'posts/post_detail.html', {'post': post, 'form': form})