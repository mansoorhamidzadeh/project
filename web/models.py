from django.contrib.auth.models import User
from django.utils import timezone


from django.db import models


# Create your models here.

class Article(models.Model):
    STATUS = (
        ('d', 'draft'),
        ('p', 'publish'),
        ('i', 'investigation'),
        ('b', 'back')
    )
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    content = models.TextField()
    category = models.ManyToManyField('ArticleCategory',null=True,blank=True)
    # image=models.ImageField(upload_to='images')
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now=True)
    is_special = models.BooleanField(default=False)
    status = models.CharField(max_length=1, choices=STATUS)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['-created']

    def __str__(self):
        return self.title


class ArticleCategory(models.Model):
    title = models.CharField(max_length=150)
    status = models.BooleanField(default=True, verbose_name='Active?')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
