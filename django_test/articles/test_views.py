from django.test import Client
from django.test import TestCase
from mixer.backend.django import mixer
from .models import Article, Tag
from users.models import ArticlesUser



class ViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.article = mixer.blend(Article)
        Tag.objects.create(tag_name = 'test')
        ArticlesUser.objects.create_superuser(username='test', email='test123@test.ru', password='123456')

    # пример проверки статуса ответа по запросу
    def test_status_main_page(self):

        response = self.client.get('/')
        #print(response.status_code)
        self.assertEqual(response.status_code,200)

    # пример проверки статуса ответа по запросу

    def test_status_detail_tag(self):

        response = self.client.get('/articles/tag-create/')
        #print(response.status_code)
        self.assertEqual(response.status_code, 302)

    # пример тестирования доступа без авторизованным пользователем

    def test_status_create_tag(self):
        response = self.client.get('/articles/tag-one/1/')
        #print(response.status_code)
        self.assertEqual(response.status_code, 302)

    # пример тестирования доступа с авторизованным пользователем

    def test_status_detail_tag(self):
        self.client.login(username = 'test', password = '123456')
        response = self.client.get('/articles/tag-one/1/')
        print(response.status_code)
        self.assertEqual(response.status_code, 200)


    # пример тестирования доступа с авторизованным пользователем

    def test_status_detail_tag(self):
        self.client.login(username = 'test', password = '123456')
        response = self.client.get('/articles/tag-one/1/')
        print(response.status_code)
        self.assertEqual(response.status_code, 200)


    # post запрос

    def test_status_post_tag(self):

        self.client.login(username = 'test', password = '123456')
        response = self.client.post('/articles/tag-create/', {'tag_name' : 'testtest'})
        '''
        все работает верно, так как после добавления нового тега 
        происходит редирект и код ответа сервера равен 302
        '''
        print(response.status_code)

        self.assertEqual(response.status_code, 302)
