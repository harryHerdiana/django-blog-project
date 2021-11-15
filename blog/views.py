from typing import List
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from .models import Comment, Post
from django.views.generic.base import TemplateView
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView, CreateView
from .forms import CommentForm
from django.views import View
from django.urls import reverse


new_all_posts = Post.objects.all().order_by("date")



class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering=["-date"]
    context_object_name = "posts"
    def get_queryset(self):
        queryset= super().get_queryset()
        data=queryset[:2]
        return data


class PostsView(ListView):
    template_name = "blog/all_posts.html"
    model=Post
    ordering = ["-date"]
    context_object_name = "all_posts"


class PostDetailView(View):
    def is_stored_posts(self,request,post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later=False
        return is_saved_for_later

    def get(self,request,slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post":post,
            "post_tags":post.tag.all(),
            "comment_form":CommentForm,
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_posts(request,post.id),
        }
        return render(request,"blog/post_detail.html",context)

    def post(self,request,slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post_detail_page",args=[slug]))
        context = {
            "post":post,
            "post_tags":post.tag.all(),
            "comment_form":comment_form,
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_posts(request,post.id),
        } 
        return render(request,"blog/post_detail.html",context)


class ReadLaterView(View):

    def get(self,request):
        stored_posts = request.session.get("stored_posts")
        context = {}
        if stored_posts is None or len(stored_posts)==0:
            context["posts"]=[]
            context["has_posts"]=False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"]=posts
            context["has_posts"]=True
        return render(request,"blog/stored_post.html",context)

    def post(self,request):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is None:
            stored_posts = []
        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
            request.session["stored_posts"] = stored_posts

        else:
            stored_posts.remove(post_id)
            request.session["stored_posts"] = stored_posts
        return HttpResponseRedirect("/")