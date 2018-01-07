from django.db import models
from django.core.urlresolvers import reverse # For update and create views
from apps.categories.models import Category

# Create your models here.
class Work(models.Model):

    category = models.ForeignKey(Category, related_name='+', on_delete=models.CASCADE)
    before_photo_1 = models.ImageField(upload_to='img', null=True, blank=True)
    before_photo_2 = models.ImageField(upload_to='img', null=True, blank=True)
    after_photo_1 = models.ImageField(upload_to='img', null=True, blank=True)
    after_photo_2 = models.ImageField(upload_to='img', null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    client = models.CharField(max_length=100, null=True, blank=True)
    link = models.CharField(max_length=150, null=True, blank=True)
    more_photo_1 = models.ImageField(upload_to='img', null=True, blank=True)
    more_photo_2 = models.ImageField(upload_to='img', null=True, blank=True)
    more_photo_3 = models.ImageField(upload_to='img', null=True, blank=True)
    more_photo_4 = models.ImageField(upload_to='img', null=True, blank=True)
    more_photo_5 = models.ImageField(upload_to='img', null=True, blank=True)


    def __str__(self):
        return self.title
