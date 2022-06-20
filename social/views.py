from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import CommentForm, PostForm

# Create your views here.
def home_view(request):
    return render(request, 'home.html')


@login_required
def post_view(request):
    posts = Post.objects.filter(
        user__profile__in=request.user.profile.following.all()
    ).order_by("-timestamp")


    comments = Comment.objects.filter(
        user__posts__in=request.user.posts.all()
    )

    if request.method == 'POST':
        data = request.POST
        post_id = data.get('id')
        post = Post.objects.get(pk=post_id)
        action = data.get('like')
        if action == 'like':
            post.likes.add(request.user)
        elif action == 'unlike':
            post.likes.remove(request.user)

    context = {
        'posts': posts,
        'comments': comments
    }

    return render(request, 'social/post_view.html', context=context)

@login_required
def post_detail_view(request, pk):
    post = Post.objects.get(pk=pk)
 
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if 'like' in request.POST:
            action = request.POST.get('like')
            if action == 'like':
                post.likes.add(request.user)
            elif action == 'unlike':
                post.likes.remove(request.user)
            post.save()
            return redirect('post_detail_view', pk)
        else:
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.post = post
                comment.save()
                return redirect('post_detail_view', pk)
    else:
        form = CommentForm()

    context = {
        'post': post,
        'form': form,
    }

    return render(request, 'social/post_detail.html', context=context)

@login_required
def create_post_view(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.image = form.cleaned_data.get('image')
            post.user = request.user
            post.save()
            return redirect('post_view')
    else:
        form = PostForm()

    context = {
        'form': form,
    }

    return render(request, 'social/create_post.html', context=context)
