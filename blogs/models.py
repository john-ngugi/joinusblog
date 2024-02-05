from telnetlib import STATUS
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

STATUS=(
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.TextField(max_length=200, unique=True,null=True)
    slug = models.SlugField(max_length=200, unique=True)
    # author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = RichTextField (null=True)
    bgimage=models.ImageField(upload_to ='pics',null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    titleBreak=models.TextField(max_length=200)
    pic_owner=models.CharField(max_length=200)
    preview=models.CharField(max_length=500,null=True)
    hyperlink=models.CharField(max_length=200,null=True)


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title



