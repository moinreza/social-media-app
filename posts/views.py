# posts/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post
from .forms import PostForm

# View for homepage (global feed)
def home(request):
    posts = Post.objects.all()

    # Filtering
    date_filter = request.GET.get('date')
    if date_filter == 'newest':
        posts = posts.order_by('-created_at')
    elif date_filter == 'oldest':
        posts = posts.order_by('created_at')

    media_filter = request.GET.get('media')
    if media_filter == 'image':
        posts = posts.filter(image__isnull=False)
    elif media_filter == 'text':
        posts = posts.filter(image__isnull=True)

    user_filter = request.GET.get('user')
    if user_filter:
        posts = posts.filter(owner__username=user_filter)

    # Search
    search_query = request.GET.get('search')
    if search_query:
        posts = posts.filter(text__icontains=search_query)

    return render(request, 'posts/home.html', {'posts': posts})

# User Profile View
@login_required
def profile(request):
    posts = Post.objects.filter(user=request.user)
    return render(request, 'posts/profile.html', {'posts': posts, 'user': request.user})

# Create a new post
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            messages.success(request, "Post created successfully!")
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'posts/post_form.html', {'form': form})

# Edit an existing post
@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.owner != request.user:
        messages.error(request, "You are not authorized to edit this post.")
        return redirect('home')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully!")
            return redirect('home')
    else:
        form = PostForm(instance=post)

    return render(request, 'posts/post_form.html', {'form': form})

# Delete a post
@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.owner != request.user:
        messages.error(request, "You are not authorized to delete this post.")
        return redirect('home')

    if request.method == 'POST':
        post.delete()
        messages.success(request, "Post deleted successfully!")
        return redirect('home')

    return render(request, 'posts/delete_confirmation.html', {'post': post})
