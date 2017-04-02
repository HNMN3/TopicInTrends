# This file contains the different view for various operations

from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, CreateAPIView, ListAPIView
from rest_framework.views import APIView

from Topics.serializers import TopicSerializer, CommentSerializer, UserSerializer
from .models import Topic, Comment
from .permissions import IsTopicOwnerOrNot, IsCommentOwnerOrNot
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework.response import Response


# Create your views here.

class TopicList(ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsTopicOwnerOrNot,)

    def perform_create(self, serializer):
        serializer.save(topic_owner=self.request.user)


class TopicParticular(ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsTopicOwnerOrNot,)

    def get(self, request, *args, **kwargs):
        topics = Topic.objects.filter(topic_owner=request.user)
        s = TopicSerializer(topics, many=True)
        return Response(s.data)


class CommentCreate(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCommentOwnerOrNot,)

    def perform_create(self, serializer):
        serializer.save(comment_owner=self.request.user,
                        comment_on_topic=Topic.objects.get(pk=self.request.data.get('topic_id')))


class CommentList(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCommentOwnerOrNot,)

    def get(self, request, *args, **kwargs):
        t = Topic.objects.get(pk=kwargs['topic_id'])
        s = CommentSerializer(Comment.objects.filter(comment_on=t), many=True)
        return Response(s.data)


class CommentUpdate(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCommentOwnerOrNot,)


class DoReply(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def put(self, request, *args, **kwargs):
        c = Comment.objects.get(pk=kwargs['comment_id'])
        if c.reply:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        c.reply = request.data.get('reply')
        c.save()
        s = CommentSerializer(c)
        return Response(s.data)
