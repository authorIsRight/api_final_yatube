# TODO:  Напишите свой вариант
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.views import PermissionDenied
from rest_framework import mixins
from .permissions import IsAuthorOrReadOnlyPermission, IsAuthOrAuth
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Group, Post
from .serializers import CommentSerializer, GroupSerializer, PostSerializer, FollowSerializer




class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthorOrReadOnlyPermission,) #??

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnlyPermission,) #??    
    pagination_class = LimitOffsetPagination
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(PostViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        instance.delete()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnlyPermission,) #??
    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())

    def get_queryset(self):
        post = self.get_post()
        return post.comments.all()

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(CommentViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        instance.delete()

class FollowViewSet(viewsets.ModelViewSet):
    # queryset = Post.objects.all()
    serializer_class = FollowSerializer        
    permission_classes = (IsAuthOrAuth,) #??    
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('following',) 

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
