from datetime import datetime
from django.test import TestCase
from django.contrib.auth import get_user_model

from ..models import Post, Category
from accounts.models import User, Profile



class TestPostModels(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="iman@email.com", password="testpass123")
        self.profile = Profile.objects.create(
            user=self.user,
            first_name="iman",
            last_name="daneshi",
            description="goodwriter"
        )

    def test_create_post_with_valid_data(self):
        
        category_object1 = Category.objects.create(name="test category")
        category_object12 = Category.objects.create(name="test category2")
        post = Post.objects.create(
            title = "test",
            author = self.profile,
            content = "description",
            status = True,
            published_date = datetime.now()
        )
        post.category.set([category_object1,category_object12])
        self.assertEqual(post.title, "test")
        self.assertTrue(Post.objects.filter(pk=post.id).exists())

    def test_create_post_with_invalid_data(self):
        
        category_object1 = Category.objects.create(name="test category")
        category_object12 = Category.objects.create(name="test category2")
        post = Post.objects.create(
            author = self.profile,
            content = "description",
            status = True,
            published_date = datetime.now()
        )
        post.category.set([category_object1,category_object12])
        self.assertNotEqual(post.title, "test")
        self.assertTrue(Post.objects.filter(pk=post.id).exists())