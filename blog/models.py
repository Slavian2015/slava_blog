from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    following = models.ManyToManyField(User, related_name='following', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def profiles_posts(self):
        return self.post_set.all()

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ('-created',)


class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.body)[:30]

    class Meta:
        ordering = ('-created',)
