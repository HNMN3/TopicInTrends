# Keep coding and change the world..And do not forget anything..Not Again..

# This file contains serializers for all models

from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Topic, Comment


class CommentSerializer(serializers.ModelSerializer):
    comment_date = serializers.ReadOnlyField()
    comment_owner = serializers.ReadOnlyField(source='topic_owner.username')
    comment_on = serializers.ReadOnlyField(source='comment_on.topic_name')
    pk = serializers.ReadOnlyField()

    class Meta:
        model = Comment
        fields = ('pk', 'comment', 'reply', 'comment_owner', 'comment_on', 'comment_date')


class TopicSerializer(serializers.ModelSerializer):
    topic_id = serializers.ReadOnlyField()
    topic_owner = serializers.ReadOnlyField(source='topic_owner.username')
    created = serializers.ReadOnlyField()

    class Meta:
        model = Topic
        fields = ('topic_id', 'topic_name', 'topic_owner', 'created')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')
