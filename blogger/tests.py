from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User


class TestPostsModel(TestCase):
    def test_create_model(self):
        user = User.objects.create(username="testuser", title="Testuser", password="testpassword123", email="test@gmail.com")
