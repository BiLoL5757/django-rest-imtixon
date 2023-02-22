from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class News(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField()
    data = models.DateTimeField()

    def __str__(self):
        return self.title
