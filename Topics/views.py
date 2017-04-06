# This file contains the different view for various operations

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, CreateAPIView, ListAPIView

from Topics.serializers import TopicSerializer, CommentSerializer
from .models import Topic, Comment
from .permissions import IsTopicOwnerOrNot, IsCommentOwnerOrNot
from rest_framework import permissions
from rest_framework.response import Response


# This class allows to view all topics and create new topic
class TopicList(ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsTopicOwnerOrNot,)

    def perform_create(self, serializer):
        serializer.save(topic_owner=self.request.user)


# This class allows to get topics created by a particular user
class TopicParticular(ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsTopicOwnerOrNot,)

    def get(self, request, *args, **kwargs):
        topics = Topic.objects.filter(topic_owner=request.user)
        s = TopicSerializer(topics, many=True)
        return Response(s.data)


# This class allows to create a new comment on a particular topic
class CommentCreate(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCommentOwnerOrNot,)

    def perform_create(self, serializer):
        serializer.save(comment_owner=self.request.user,
                        comment_on=Topic.objects.get(pk=self.request.data.get('topic_id')))


# This class allows to view comments on a particular topic
class CommentList(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCommentOwnerOrNot,)

    def get(self, request, *args, **kwargs):
        t = Topic.objects.get(pk=kwargs['topic_id'])
        s = CommentSerializer(Comment.objects.filter(comment_on=t), many=True)
        return Response(s.data)


# This class allows to update a comment to its owner
class CommentUpdate(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCommentOwnerOrNot,)


# This class allows any authorized user to reply on a particular comment
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
