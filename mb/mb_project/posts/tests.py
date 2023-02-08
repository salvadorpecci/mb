# posts/tests.py
from django.test import TestCase
from django.urls import reverse  #new
from .models import Post


class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(text='just a test')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'just a test')
class HomePageViewTest(TestCase):                       # new

        def setUp(self):                                    # new
            Post.objects.create(text='this is another test')# new

        def test_view_url_exists_at_proper_location(self):  # new
            resp = self.client.get('/')                     # new
            self.assertEqual(resp.status_code, 200)         # new

        def test_view_url_by_name(self):                   # new
            resp = self.client.get(reverse('home'))         # new
            self.assertEqual(resp.status_code, 200)         # new

        def test_view_uses_correct_template(self):          # new
            resp = self.client.get(reverse('home'))         # new
            self.assertEqual(resp.status_code, 200)         # new
            self.assertTemplateUsed(resp, 'home.html')      # new
