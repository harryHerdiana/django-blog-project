from django.shortcuts import get_object_or_404, render
from datetime import date
from .models import Post

#Dummy Data

# all_posts = [
#     {
#         "slug":"hike-in-the-mountains",
#         "image":"mountains.jpg",
#         "author":"Harry Herdiana",
#         "date":date(2021,12,10),
#         "title":"Mountain Hiking",
#         "excerpt":"This is the best view ever, I forget all of my problem when I stayed here",
#         "content":"""
#         Lorem ipsum dolor sit amet consectetur adipisicing elit. 
#         Nulla perferendis labore accusamus, totam assumenda ipsam at? 
        
#         Tempora, quisquam quaerat, voluptas odio iusto doloribus debitis sint ex
#         recusandae eos accusamus maxime mollitia rerum! 
#         Perferendis ex, eius qui harum enim ut libero illum expedita iste fugit facilis laboriosam modi, quam aut deleniti.
#         """
#     },
#         {
#         "slug":"programming-is-fun",
#         "image":"coding.jpg",
#         "author":"Harry Herdiana",
#         "date":date(2021,10,25),
#         "title":"Programming is Great",
#         "excerpt":"One of the challenging yet rewarding skills is Programming, many failed and many success on this field.",
#         "content":"""
#         Lorem ipsum dolor sit amet consectetur adipisicing elit. 
#         Nulla perferendis labore accusamus, totam assumenda ipsam at? 
        
#         Tempora, quisquam quaerat, voluptas odio iusto doloribus debitis sint ex
#         recusandae eos accusamus maxime mollitia rerum! 
#         Perferendis ex, eius qui harum enim ut libero illum expedita iste fugit facilis laboriosam modi, quam aut deleniti.
#         """
#     },
#         {
#         "slug":"fresh-mountain-landscape",
#         "image":"woods.jpg",
#         "author":"Harry Herdiana",
#         "date":date(2022,5,12),
#         "title":"Foresting",
#         "excerpt":"Breathe deep the fresh air, escape the pollution of the City to the nature",
#         "content":"""
#         Lorem ipsum dolor sit amet consectetur adipisicing elit. 
#         Nulla perferendis labore accusamus, totam assumenda ipsam at? 
        
#         Tempora, quisquam quaerat, voluptas odio iusto doloribus debitis sint ex
#         recusandae eos accusamus maxime mollitia rerum! 
#         Perferendis ex, eius qui harum enim ut libero illum expedita iste fugit facilis laboriosam modi, quam aut deleniti.
#         """
#     },
#      {
#         "slug":"mountain-biking",
#         "image":"mountain-biking.jpeg",
#         "author":"Harry Herdiana",
#         "date":date(2022,2,10),
#         "title":"Mountain Biking",
#         "excerpt":"Rush your adrenaline with the most scenic view on the deep of mountain forest!",
#         "content":"""
#         Lorem ipsum dolor sit amet consectetur adipisicing elit. 
#         Nulla perferendis labore accusamus, totam assumenda ipsam at? 
        
#         Tempora, quisquam quaerat, voluptas odio iusto doloribus debitis sint ex
#         recusandae eos accusamus maxime mollitia rerum! 
#         Perferendis ex, eius qui harum enim ut libero illum expedita iste fugit facilis laboriosam modi, quam aut deleniti.
#         """
#     },
        
# ]
new_all_posts = Post.objects.all().order_by("date")


def starting_page(request):
    latest_posts = new_all_posts[0:2]
    return render(request,"blog/index.html",{
        "posts":latest_posts
    })

def posts(request):
    return render(request,"blog/all_posts.html",{
        "all_posts":new_all_posts
    })


def post_detail(request, slug):
    # identified_post = next(post for post in new_all_posts if post['slug']== slug)
    identified_post = get_object_or_404(Post,slug=slug)
    print(identified_post)
    return render(request,"blog/post_detail.html",{
        "post":identified_post
    })