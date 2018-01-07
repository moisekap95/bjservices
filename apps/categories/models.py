from django.db import models
from django.core.urlresolvers import reverse # For update and create views

class Category(models.Model):
    name =  models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='img', null=True, blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
