from django.shortcuts import render
from .serializers import *
from .models import News
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from django.contrib.auth import get_user_model

# Create your views here.


class NewsCreate(ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDetail(RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class NewsList(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer 

class UserAPI(ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer  