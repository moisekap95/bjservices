from django.db import models
from django.core.urlresolvers import reverse # For update and create views
from apps.categories.models import Category

class Enquiry(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True, blank=True)
    subject = models.CharField(max_length=150)
    message = models.TextField()
    category = models.ForeignKey(Category, related_name='+', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('enquiries:detail', kwargs={'pk':self.pk}) # For update and create views

    class Meta:
            verbose_name_plural = "Enquiries"