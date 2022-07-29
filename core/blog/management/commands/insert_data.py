from django.core.management.base import BaseCommand
from faker import Faker
from datetime import datetime
import random

from accounts.models import Profile, User
from blog.models import Category, Post


category_faker = Faker()
category_list = [
    "team",
    "job",
    "culture",
    "option",
    "across",
    "data",
    "reduce",
    "TV",
    "walk",
    "material",
]


class Command(BaseCommand):
    help = "Create dummy data"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):
        for i in range(20):
            if i % 2 == 0:
                first_name = self.fake.first_name_male()
            else:
                first_name = self.fake.first_name_female()
            last_name = self.fake.last_name()
            email = first_name.lower() + last_name.lower() + "@email.com"
            user = User.objects.create_user(email=email, password="testpass123")
            user.is_active = True
            user.is_verified = True
            user.save()
            profile = Profile.objects.get(user=user)
            profile.first_name = "Asghar"
            profile.last_name = last_name
            profile.description = self.fake.sentence(nb_words=10)
            profile.save()
            for name in category_list:
                Category.objects.get_or_create(name=name)
            for i in range(5):
                post = Post.objects.create(
                    author=profile,
                    title=self.fake.text(max_nb_chars=50),
                    content=self.fake.paragraph(nb_sentences=10),
                    status=random.choice([True, False]),
                    published_date=datetime.now(),
                )
                post.category.set(random.choices(list(Category.objects.all()), k=3))
                post.save()
