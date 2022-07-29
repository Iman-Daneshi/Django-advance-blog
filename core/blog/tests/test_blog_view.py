from datetime import datetime
from django.test import TestCase, Client
from django.urls import reverse

from accounts.models import User, Profile
from ..models import Post, Category


class TestBlogViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            email="ali@email.com", password="Test@pass123"
        )
        self.profile = Profile.objects.create(
            user=self.user,
            first_name="TestU",
            last_name="UserT",
            description="goodwriter",
        )
        category_object = Category.objects.create(name="test category")
        self.post = Post.objects.create(
            title="test",
            author=self.profile,
            content="description",
            status=True,
            published_date=datetime.now(),
        )
        self.post.category.set([category_object])

    def test_blog_index_url_successful_response(self):
        url = reverse("blog:index")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTrue(str(response.content).find("index"))
        self.assertTemplateUsed(response, "index.html")
        self.assertContains(response, "Django")

    def test_blog_post_detail_logged_in_response(self):
        self.client.force_login(self.user)
        url = reverse("blog:post-detail", kwargs={"pk": self.post.id})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_blog_post_detail_anonymouse_response(self):
        url = reverse("blog:post-detail", kwargs={"pk": self.post.id})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)
