from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Model for Topic
class Topic(models.Model):
    topic_id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    topic_name = models.CharField(max_length=100)
    topic_owner = models.ForeignKey('auth.User', related_name='topics', on_delete=models.CASCADE)

    def __str__(self):
        # for representation
        return self.topic_name


# Model for Comment
class Comment(models.Model):
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    comment_on = models.ForeignKey(Topic, related_name='comments', on_delete=models.CASCADE)
    comment = models.TextField()
    reply = models.TextField(blank=True, null=True)

    def __str__(self):
        # for representation
        return self.comment
