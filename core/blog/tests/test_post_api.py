from rest_framework.test import APIClient
from datetime import datetime
from django.urls import reverse
import pytest
from accounts.models import User, Profile
from blog.models import Post


@pytest.mark.django_db     # allow pytest to have access to db
class TestPostApi():
    client = APIClient()
    """user = User.objects.create_user(
        email="iman@email.com", password="testpass123"
    )
    profile = Profile.objects.create(
        user=user,
        first_name="iman",
        last_name="daneshi",
        description="goodwriter",
    )
    post = Post.objects.create(
        title="test",
        author=profile,
        content="description",
        status=True,
        published_date=datetime.now(),
    )"""
    def test_get_post_response_200_status(self):
        url = reverse('blog:api-v1:post-list')
        respose = self.client.get(url)
        assert respose.status_code == 200

    def test_create_post_response_401_status(self):
        url = reverse('blog:api-v1:post-list')
        data = {
            "title" : "test",
            "content":"description",
            "status" : True,
            "published_date":datetime.now(),
        }
        response = self.client.post(url,data)
        assert response.status_code == 401
