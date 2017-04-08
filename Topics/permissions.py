# Keep coding and change the world..And do not forget anything..Not Again..
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsTopicOwnerOrNot(BasePermission):
    # This Permission checks whether the current
    # Logged in User is Owner of the Topic Instance
    # To Which he/she is trying to manipulate
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.topic_owner == request.user


class IsCommentOwnerOrNot(BasePermission):
    # This permission is same as above
    # rather it checks same thing for
    # Comment instance
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.comment_owner == request.user
