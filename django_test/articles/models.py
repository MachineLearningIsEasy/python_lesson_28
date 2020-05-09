from django.db import models
from datetime import datetime
import os
from django.conf import settings
from django.utils.functional import cached_property
from users.models import ArticlesUser

# Create your models here.

#https://djbook.ru/rel1.9/topics/db/models.html#model-inheritance - наследование моделей

class AvtiveManager(models.Manager):

    def get_queryset(self):
        all_objects = super().get_queryset()
        return all_objects.filter(is_active = True)

class IsActiveMixin(models.Model):
    objects = models.Manager()
    active_objects = AvtiveManager()
    is_active = models.BooleanField(default = False)
    class Meta:
        abstract = True


class Tag(IsActiveMixin,models.Model):
    tag_name = models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.tag_name}'

class Article(IsActiveMixin, models.Model):
    article_name = models.CharField(max_length = 100, null = True)
    article_text = models.CharField(max_length = 1000, null = True)
    article_date = models.DateTimeField(default = datetime.now())
    article_rating = models.IntegerField(null = True)
    article_tag  = models.ManyToManyField(Tag)
    article_img = models.ImageField(upload_to = 'articles', null = True, blank = True)
#    article_author = models.ForeignKey(ArticlesUser, blank = True, on_delete=models.CASCADE)
#    article_rating = models.PositiveSmallIntegerField(default=1)

    def tag_number(self):
        return len(self.article_tag.all())

    @cached_property
    def get_all_tags(self):
        tags = Tag.objects.all()
        return tags


    def is_tag_one(self):
        if len(self.article_tag.all()) == 1:
            return True
        return False
    '''
    DataField - дата
    TimeField - время
    
    Числовые типы:
    IntegerField
    PositeveIntegerField
    FloatField
    
    Логические типы:
    BooleanField
    
    Байтовый тип:
    BinaryField
    
    Email:
    EmailField
    
    URL:
    URLField
    
    Image:
    ImageField
    '''

    def __str__(self):
        return f'{self.article_name}, published: {self.article_date}'

