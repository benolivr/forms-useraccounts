from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",email="test@email.com", password="secret"
            )
    

        cls.post = Post.objects.create(
            title='A good title',
            body='Nice body content',
            author=cls.user,
        )

    def test_post_model(self):
        post = self.post
        self.assertEqual(post.title, 'A good title')
        self.assertEqual(post.body, 'Nice body content')
        self.assertEqual(self.post.author.username, 'testuser')
        self.assertEqual(self.post.author.email, 'test@email.com')
        self.assertEqual(str(self.post), "A good title")
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")


    def test_home_page_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_url_name(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_content(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertContains(response, "A good title")


    def test_post_detail_status_code(self):
        url = reverse('post_detail', args=[self.post.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post_detail_url_name(self):
        url = reverse('post_detail', args=[self.post.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post_detail_template(self):
        url = reverse('post_detail', args=[self.post.id])
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_post_detail_page_content(self):
        url = reverse('post_detail', args=[self.post.id])
        response = self.client.get(url)
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.body)
