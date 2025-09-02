from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Comment
from .forms import CommentForm


def index(request):
    posts = Post.objects.all().order_by("-created")
    return render(request, "blog/index.html", {"posts": posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    return render(request, "blog/post_detail.html", {"post": post, "form": form})


def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return render(request, "blog/partials/comment.html", {"comment": comment})
    return HttpResponse(status=400)
