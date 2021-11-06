from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from .models import Comment, Post
from django.views.generic.base import TemplateView
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView, CreateView
from .forms import CommentForm
from django.views import View
from django.urls import reverse


new_all_posts = Post.objects.all().order_by("-date")

# def starting_page(request):
#     latest_posts = new_all_posts[0:2]
#     return render(request,"blog/index.html",{
#         "posts":latest_posts
#     })

class StartingPageView(TemplateView):
    template_name = "blog/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"]=new_all_posts[0:2]
        return context



# def posts(request):
#     return render(request,"blog/all_posts.html",{
#         "all_posts":new_all_posts
#     })


class PostsView(ListView):
    template_name = "blog/all_posts.html"
    model=Post
    ordering = ["-date"]
    context_object_name = "all_posts"



# def post_detail(request, slug):
#     # identified_post = next(post for post in new_all_posts if post['slug']== slug)
#     identified_post = get_object_or_404(Post,slug=slug)
#     print(identified_post)
#     return render(request,"blog/post_detail.html",{
#         "post":identified_post
#     })

class PostDetailView(View):
    def get(self,request,slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post":post,
            "post_tags":post.tag.all(),
            "comment_form":CommentForm
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
            "comment_form":comment_form
        } 
        return render(request,"blog/post-detail.html",context)


   

# class CommentView(CreateView):
#     form_class = CommentForm
#     model = Comment
#     template_name = "blog/post_detail.html"