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
        "post_form":form,
        "greet":"Hello",
        'success_message':message
    }
    return render(request, 'post.html', context)


def create_comment(request):
    form = CommentForm
    if request.method == "POST":
        form = CommentForm(request.POST or None)
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
    if request.method == "POST":
        form = ReelForm(request.POST or None)
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

def view_post_and_comment(request,ID, title):
    message = None
    query_post = Post.objects.get(id=int(ID))
    query_comment = Comment.objects.filter(to_post_id=int(ID))
    form = CommentForm
    if request.method == "POST":
        form = CommentForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author_id = request.user.id
            instance.to_post_id = query_post.id
            instance.save()
            message = f"Your comment on{query_post.title}has been published"
            return redirect(f"/post/{ID}/{title}/")
    context = {
        "message":message,
        "query_post":query_post,
        "query_comment":query_comment,
        "comment_form":form
    }
    return render(request,"view_full_post.html", context)