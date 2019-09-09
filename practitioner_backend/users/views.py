from django.shortcuts import render
from rest_framework_mongoengine import generics
from .serializers import UsersSerializer
from .models import Users
from .pagination import UsersPagination
from rest_framework.response import Response
from django.shortcuts import get_list_or_404, get_object_or_404
from mongo_auth import permissions


class UsersList(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [permissions.AuthenticatedOnly]
    def perform_create(self, serializer):
        serializer.is_valid()
        serializer.save(user=self.request.user)

class UserSingle(generics.RetrieveUpdateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    lookup_field='email'

    def get_object(self, queryset=None):
        email = self.kwargs.get('email')
        obj = Users.objects.get(email=email)
        return obj
