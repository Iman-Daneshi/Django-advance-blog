from django.db import models


# Create your models here.
class Post(models.Model):
    '''
    This is a class representing posta for the blog app.
    '''
    image = models.ImageField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = ('Categories')

    def __str__(self):
        return self.name