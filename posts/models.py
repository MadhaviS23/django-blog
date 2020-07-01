from tinymce import HTMLField
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your models here.
User = get_user_model()


class Author(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField()

    def _str_(self):
        return self.user.username()


class Category(models.Model):
    title= models.CharField(max_length = 20)
    

    def _str_(self):
        return self.title()

    
  
    




class post(models.Model):

    title = models.CharField(max_length = 100)
    overview = models.TextField()
    content =HTMLField()
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField(default=True)
    prev_post = models.ForeignKey('self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey('self', related_name= 'next', on_delete=models.SET_NULL, blank=True, null=True)

    def _str_(self):
        return self.title, self.categories, self.author


    def get_absolute_url(self):
        return reverse('single-detail', kwargs={
            'id' : self.id 

        })






