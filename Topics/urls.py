# Keep coding and change the world..And do not forget anything..Not Again..
from django.conf.urls import url
from .views import TopicList, CommentList, CommentUpdate, CommentCreate, TopicParticular, DoReply

urlpatterns = [
    url(r'^topic_list/$', TopicList.as_view(), name='all_topics'),  # To create new topic and see all topics available
    url(r'^my_topics/$', TopicParticular.as_view(), name='my_topics'),  # To see topics created by logged in user
    url(r'^comment_list/(?P<topic_id>[0-9]+)$',  # To see comment list for a particular topic
        CommentList.as_view(), name='comment_list'),
    url(r'^comment_create/$', CommentCreate.as_view(),
        name='comment_create'),  # To create a comment on a particular topic
    url(r'^comment_update/(?P<pk>[0-9]+)$', CommentUpdate.as_view(),
        name='comment_update'),  # To update a comment
    url(r'^do_reply/(?P<comment_id>[0-9]+)$', DoReply.as_view(),
        name='do_reply'),  # to do a reply on particular comment
]
