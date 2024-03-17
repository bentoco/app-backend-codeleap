from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Post


class CareerListCreateAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_list(self):
        response = self.client.get('/careers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        data = {
            'username': 'test_user',
            'title': 'Test Title',
            'content': 'Test Content'
        }
        response = self.client.post('/careers/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class CareerRetrieveUpdateDestroyAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.post = Post.objects.create(username='test_user', title='Test Title', content='Test Content')

    def test_patch_post(self):
        data = {
            'title': 'Updated Title',
            'content': 'Updated Content'
        }
        response = self.client.patch(f'/careers/{self.post.pk}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_post(self):
        response = self.client.delete(f'/careers/{self.post.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
