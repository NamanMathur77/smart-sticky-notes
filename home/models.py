import datetime
from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now()-date.timedelta(days=1)
    
    def get_absolute_url(self):
        return reverse('index')


class Notes(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000, blank=False)
    text = models.TextField(blank=True)
    additional_info = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


