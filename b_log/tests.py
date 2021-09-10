from django.contrib.auth import get_user_model
from django.http import response
from django.test import TestCase
from django.urls import reverse

from .models import Post
# Create your tests here.

class BlogTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user( username ='testUser'
                                                         , email='test@email.com'
                                                         , password='password')
        self.post = Post.objects.create( title = 'My good title'
                                        , body='body content'
                                        , author=self.user)
        
    def test_string_representation(self):
        post = Post(title='sample title')
        self.assertEqual(str(post), post.title)
        
    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'My good title')
        self.assertEqual(f'{self.post.author}','testUser')
        self.assertEqual(f'{self.post.body}', 'body content')
        
    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'body content')
        self.assertTemplateUsed(response, 'home.html')
    
    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('post/314/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'My good title')
        self.assertTemplateUsed(response, 'post_detail.html')