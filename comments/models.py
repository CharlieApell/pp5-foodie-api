from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Comment(models.Model):

    rating_choices = [
        (1, 'Bad'),
        (2, 'Not good'),
        (3, 'Neutral'),
        (4, 'Good'),
        (5, 'Really good'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    rating = models.IntegerField(choices=rating_choices, default=3)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
