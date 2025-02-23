from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post
from .forms import PostForm

# Homepage: Display all posts with sorting, filtering, and search options
def homepage(request):
    # Get filter parameters from the GET request
    date_filter = request.GET.get('date', None)
    media_filter = request.GET.get('media', None)
    user_filter = request.GET.get('user', None)
    search_query = request.GET.get('search', None)

    # Apply filters based on query parameters
    if date_filter == 'newest':
        posts = Post.objects.all().order_by('-created_at')
    elif date_filter == 'oldest':
        posts = Post.objects.all().order_by('created_at')
    else:
        posts = Post.objects.all()

    if media_filter == 'images':
        posts = posts.filter(image__isnull=False)
    elif media_filter == 'text':
        posts = posts.filter(image__isnull=True)

    if user_filter:
        user = User.objects.get(username=user_filter)
        posts = posts.filter(user=user)

    if search_query:
        posts = posts.filter(text__icontains=search_query)

    return render(request, 'posts/homepage.html', {'posts': posts})


# Profile page: Display only the logged-in user's posts
@login_required
def profile(request):
    user_posts = Post.objects.filter(user=request.user)
    return render(request, 'posts/profile.html', {'posts': user_posts})


# Post creation: Allows users to create posts
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  # Associate the post with the logged-in user
            post.save()
            return redirect('homepage')  # Redirect to the homepage after creating the post
    else:
        form = PostForm()

    return render(request, 'posts/create_post.html', {'form': form})


# Edit post: Allows users to edit their own posts
@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Check if the logged-in user is the owner of the post
    if post.user != request.user:
        return redirect('homepage')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = PostForm(instance=post)

    return render(request, 'posts/edit_post.html', {'form': form, 'post': post})


# Delete post: Allows users to delete their own posts
@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Check if the logged-in user is the owner of the post
    if post.user != request.user:
        return redirect('homepage')

    if request.method == 'POST':
        post.delete()
        return redirect('homepage')  # Redirect to the homepage after deletion

    return render(request, 'posts/delete_post.html', {'post': post})
