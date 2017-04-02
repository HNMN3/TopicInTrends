# Keep coding and change the world..And do not forget anything..Not Again..
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsTopicOwnerOrNot(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.topic_owner == request.user


class IsCommentOwnerOrNot(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.comment_owner == request.user
