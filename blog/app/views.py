from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from app.form import PostFrom, CommentForm, CategoryForm
from app.models import Post, Category, Comment


# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return redirect('register')

    if request.method == 'POST':
        form = PostFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    ctx = {
        'posts': Post.objects.all(),
        'user': request.user,
        'categories': Category.objects.all(),
        'form': PostFrom()
    }
    return render(request, 'app/index.html', ctx)


def post(request, post_id):
    if not request.user.is_authenticated:
        return redirect('register')
    if request.method == 'POST':
        form = PostFrom(request.POST, instance=Post.objects.get(id=post_id))
        if form.is_valid():
            form.save()
            return redirect('post', post_id)

    post = Post.objects.get(id=post_id)
    ctx = {
        'post': post,
        'comments': Comment.objects.filter(post=post_id),
        'categories': Category.objects.all(),
        'comment_form': CommentForm(),
        'post_form': PostFrom(instance=post),
    }

    return render(request, 'app/post.html', ctx)


def add_comment(request):
    if not request.user.is_authenticated:
        return redirect('register')
    if (request.method != 'POST'
            or request.POST.get('comment') == ''):
        return redirect('post', post_id=request.POST.get('post_id'))
    comment = Comment()
    comment.author = request.user
    comment.text = request.POST.get('comment')
    comment.post = Post.objects.get(id=request.POST.get('post_id'))
    comment.save()
    return redirect('post', post_id=request.POST.get('post_id'))


def categories(request):
    if not request.user.is_authenticated:
        return redirect('register')
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    ctx = {
        'categories': Category.objects.all(),
        'form': CategoryForm()
    }
    return render(request, 'app/categories.html', ctx)


def delete_category(request, category_id):
    if not request.user.is_authenticated:
        return redirect('register')
    category = Category.objects.get(id=category_id)
    category.delete()
    return redirect('categories')


def authors(request):
    if not request.user.is_authenticated:
        return redirect('register')
    ctx = {
        'authors': User.objects.all(),
    }
    return render(request, 'app/authors.html', context=ctx)
