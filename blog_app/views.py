from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm, ReelForm
from .models import Post, Comment, Reel

# Create your views here.

#post
def create_post(request):
    form = PostForm
    message = None
    if request.method == "POST":
        form = PostForm(request.POST or None)
        if form.is_valid():
            get_post_name = form.cleaned_data.get('title')
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            message = f"The post {get_post_name} was created successfully"
    context = {
        "comment_form":form,
        "greet":"Hello",
        'success_message':message
    }
    return render(request, 'post.html', context)


def create_comment(request):
    form = CommentForm
    if request.method == "COMMENT":
        form = CommentForm(request.COMMENT or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user.is_valid
            instance.save()
    context = {
        "comment_form":form,
        "greet":"Hello"
    }
    return render(request, 'comment.html', context)

def create_reel(request):
    form = ReelForm
    if request.method == "REEL":
        form = ReelForm(request.REEL or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
    context = {
        "reel_form":form,
        "greet": "Hello"
    }
    return render(request, 'reel.html', context)


#View post
def view_post(request):
    get_post = Post.objects.all()
    context = {
        'post':get_post
    }
    return render(request, 'users_post.html', context)

#Delete
def delete_post(request, id):
    query_post = Post.objects.get(id=id)
    query_post.delete()
    return redirect('/all_post/')