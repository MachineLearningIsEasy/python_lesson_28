#  Простейшие запросы
# https://docs.djangoproject.com/en/3.0/ref/models/querysets/ - документация с примерами

from django.core.management.base import BaseCommand
from articles.models import Article, Tag


class Command(BaseCommand):

    def handle(self, *args, **options):
         '''
         Получить список всех объектов
         '''
         articles = Article.objects.all()
         print(articles)

         '''
         articles - type = QuerySet
         '''
         print(articles.first())

         '''
         get
         '''
         art = articles.filter(article_name = 'Lion') # не нужно так делать!
         print(art, type(art))
         art = articles.get(article_name = 'Lion') # не нужно так делать!
         print(art, type(art))

         '''
         filter /exclude
         '''
         art = articles.filter(article_name = 'Lion') # не нужно так делать!
         art_exc = articles.exclude(article_name='Lion')  # не нужно так делать!
         print('Filter: ', art)
         print('Exclude: ', art_exc)

#  Не простейшие запросы
         '''
         больше/меньше
         '''
         articles = Article.objects.filter(article_rating__gt = 9) # gte
         print('Статьи с рейтингом более 9ти: ', articles)

         articles = Article.objects.filter(article_rating__lt = 9) # lte
         print('Статьи с рейтингом менее 9ти: ', articles)

         '''
         запросы с условиями на текстовые данные
         '''
         articles = Article.objects.filter(article_name__startswith = 'C') # gte
         print('Статьи с названием на букву C: ', articles)

         articles = Article.objects.filter(article_name__contains = 'L') # gte
         print('В название статьи входит символ L: ', articles)

# Запросы к связанным моделям

         '''
         Способ 1
         '''
         tags = Tag.objects.filter(tag_name__startswith = 'C')
         articles = Article.objects.filter(article_tag = tags[0])
         print('Статьи с определенным тегом: ', articles)

         '''
         Способ 2
         '''
         articles = Article.objects.filter(article_tag__tag_name__startswith = 'C')
         print('Статьи с определенным тегом 2: ', articles)