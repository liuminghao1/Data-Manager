# _*_ coding:utf-8 _*_

from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
	'''
	允许查看和编辑user的 API endpoint
	'''
	queryset = User.objects.all()
	serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
	'''
	the same
	'''
	queryset = Group.objects.all()
	serializer_class = GroupSerializer
	
