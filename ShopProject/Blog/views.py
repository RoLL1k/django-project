from django.http import Http404, HttpResponseRedirect

from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import View

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post, Tag
from .utils import *
from .forms import TagForm, PostForm, CommentForm

from django.db.models import Q


def posts_list(request):
    search_query = request.GET.get('search', '')

    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        posts = Post.objects.all()

    return render(request, 'blog/index.html', context={'posts': posts})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = PostForm
    template = 'blog/post_create.html'
    raise_exception = True


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_update.html'
    raise_exception = True


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete_form.html'
    model_url = 'posts_list_url'
    raise_exception = True


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = TagForm
    template = 'blog/tag_create.html'
    raise_exception = True


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update.html'
    raise_exception = True


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete_form.html'
    model_url = 'tags_list_url'
    raise_exception = True


class CommentCreate(View):
    def get(self, request, slug):
        form = CommentForm()
        return render(request, 'comments/comment_create.html', context={'form': form})

    def post(self, request, slug):
        bound_form = CommentForm(request.POST)

        if bound_form.is_valid():
            post = Post.objects.get(slug=slug)
            comment = bound_form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(reverse('post_detail_url', kwargs={'slug': slug}))
        return render(request, 'comments/comment_create.html', context={'form': bound_form})

        # if bound_form.is_valid():                               # NOT NULL constraint failed: blog_comment.post_id
        #     post = Post.objects.get(slug=slug)                  # How to fix that???
        #     comment = Comment(bound_form, post_id=post.id)      # Ask teacher...
        #     comment.save()      # int() argument must be a string, a bytes-like object or a number, not 'CommentForm'
        #     return redirect(reverse('post_detail_url'))         # This variant don't work
