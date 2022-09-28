from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets, mixins
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from api.permissions import IsAuthOrAuth
from api.serializers import (CommentSerializer,
                             FollowSerializer,
                             GroupSerializer,
                             PostSerializer)
from posts.models import Group, Post


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthOrAuth,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthOrAuth,)

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())

    def get_queryset(self):
        return self.get_post().comments.all()


class CreateRetrieveViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    pass


@permission_classes([IsAuthenticated])
class FollowViewSet(CreateRetrieveViewSet):
    serializer_class = FollowSerializer
#    permission_classes = (IsAuthOrAuth,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
