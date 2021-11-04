from django.core import validators
from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator
# Create your models here.



class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=100)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    caption = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.caption}"

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL,related_name="posts",null=True)
    excerpt = models.CharField(max_length=100,null=True)
    title = models.CharField(max_length=50)
    image_name = models.CharField(max_length=50)
    date = models.DateField(auto_now=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    tag = models.ManyToManyField(Tag)
    def __str__(self):
        return f"{self.title} by {self.author}"
    def get_absolute_url(self):
        return reverse("post_detail_page", args=[self.slug])

