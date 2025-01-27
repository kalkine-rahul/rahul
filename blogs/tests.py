
# Create your tests here.
# BlogModelTestCase: Tests the creation of a blog object and its fields.
# BlogSerializerTestCase: Tests the serialization of a blog object and its fields.
# BlogViewTestCase: Tests the blog page view and the blog list view, including the data returned by the list view.
# tests.py

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .models import Blogs
from .serializers import BlogsSerializer
from django.core.files.uploadedfile import SimpleUploadedFile

class BlogSerializerTestCase(TestCase):
    def test_serializer_fields(self):
        image = SimpleUploadedFile(name='test_image.jpg', content=b'file_content', content_type='image/jpeg')
        serializer = BlogsSerializer(data={
            'title': 'Test Blog',
            'image': image,
            'description': 'This is a test blog',
            'date': '2022-01-01'
        })
        self.assertTrue(serializer.is_valid())
        data = serializer.validated_data
        self.assertEqual(set(data.keys()), set(['title', 'image', 'description', 'date']))

    def test_serializer_values(self):
        image = SimpleUploadedFile(name='test_image.jpg', content=b'file_content', content_type='image/jpeg')
        serializer = BlogsSerializer(data={
            'title': 'Test Blog',
            'image': image,
            'description': 'This is a test blog',
            'date': '2022-01-01'
        })
        self.assertTrue(serializer.is_valid())
        data = serializer.validated_data
        self.assertEqual(data['title'], 'Test Blog')
        self.assertEqual(data['description'], 'This is a test blog')
        self.assertEqual(data['date'], '2022-01-01')