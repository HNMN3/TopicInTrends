from django.db import models
from django.contrib.auth.models import User


# Model for Topic
class Topic(models.Model):
    topic_id = models.AutoField(primary_key=True)  # unique id of topic
    created = models.DateTimeField(auto_now_add=True)  # time and date on which topic was created
    topic_name = models.CharField(max_length=100)  # Name of topic
    topic_owner = models.ForeignKey('auth.User', related_name='topics',
                                    on_delete=models.CASCADE)  # Foreign key to the owner of the topic

    def __str__(self):
        return self.topic_name  # for representation of the Topic


# Model for Comment
class Comment(models.Model):
    comment_date = models.DateTimeField(auto_now_add=True)  # date and time the comment was done.
    comment_owner = models.ForeignKey('auth.User', related_name='comments',
                                      on_delete=models.CASCADE)  # the person who commented
    comment_on = models.ForeignKey(Topic, related_name='comments',  # Reference to the Topic
                                   on_delete=models.CASCADE)  # by which this comment is related to
    comment = models.TextField()  # The text of comment
    reply = models.TextField(blank=True, null=True)  # Reply to the comment initially null

    def __str__(self):
        return self.comment  # for representation of the Comment
