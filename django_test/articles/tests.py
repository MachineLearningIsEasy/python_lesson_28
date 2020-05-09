from django.test import TestCase
from faker import Faker
from .models import Article, Tag
from mixer.backend.django import mixer

import pandas as pd

# Create your tests here.

# faker https://faker.readthedocs.io/en/latest/index.html
# mixer http://klen.github.io/mixer.html

# class ArticleTestCase(TestCase):
#
#     def setUp(self):
#         data_generator = Faker(['ru_Ru'])
#         tag1 = Tag.objects.create(tag_name = data_generator.name())
#         tag2 = Tag.objects.create(tag_name = data_generator.name())
#         self.article = Article.objects.create(article_name = data_generator.name(),article_text = data_generator.text())
#         self.article.article_tag.add(tag1, tag2)
#         print(tag1.tag_name,tag2.tag_name)
#         print(self.article.article_name,self.article.article_text)
#
#     def test_how_many(self):
#         self.assertEqual(self.article.tag_number(), 2)
#
#     def test_is_one(self):
#         self.assertFalse(self.article.is_tag_one())


# class ArticleTestCase_mixer(TestCase):
#
#     def setUp(self):
#         tag1 = mixer.blend(Tag, tag_name = 'Cars')
#         tag2 = mixer.blend(Tag, tag_name = mixer.random)
#         self.article = mixer.blend(Article, article_name = mixer.fake)
#         self.article.article_tag.add(tag1, tag2)
#
#         print(tag1.tag_name,tag2.tag_name)
#         print(self.article.article_name,self.article.article_text)
#
#     def test_how_many(self):
#         self.assertEqual(self.article.tag_number(), 2)
#
#     def test_is_one(self):
#         self.assertFalse(self.article.is_tag_one())

class ArticleTestCase_csv(TestCase):

    def setUp(self):

        data = pd.read_csv('data_test.csv', sep = '__')
        for _ , row in data.iterrows():
            Article.objects.create(article_name = row['article_name'], article_text = row['article_text'])

        tag1 = mixer.blend(Tag, tag_name = 'Cars')
        tag2 = mixer.blend(Tag, tag_name = mixer.random)
        self.article = mixer.blend(Article, article_name = mixer.fake)
        self.article.article_tag.add(tag1, tag2)


    def test_how_many(self):
        articles = Article.objects.all()
        print(len(articles))

        self.assertEqual(self.article.tag_number(), 2)

    def test_is_one(self):
        self.assertFalse(self.article.is_tag_one())