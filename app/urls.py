from django.urls import path
from .views import *

urlpatterns = [
    path('', NewsList.as_view(), name='news'),
    path('<int:pk>/', NewsDetail.as_view()),
    path('create/', NewsCreate.as_view()),
    path('user/', UserAPI.as_view()),
    path('user/<int:pk>/', UserDetail.as_view()),
]