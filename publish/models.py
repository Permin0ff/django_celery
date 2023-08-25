from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created = models.DateTimeField('Created Date', default=timezone.now)
    title = models.CharField('Title', max_length=200)
    content = models.TextField('Content')
    slug = models.SlugField('Slug')
    view_count = models.IntegerField("View Count", default=0)

    def get_absolute_url(self):
        return reverse("home", args=[str(self.id)])

    def __str__(self):
        return '"%s" by %s' % (self.title, self.author)
