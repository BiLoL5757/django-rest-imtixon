from rest_framework import serializers
from .models import News
from django.contrib.auth import get_user_model

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = News

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = get_user_model()