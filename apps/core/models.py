from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, null=True, blank=True)
    phone = models.CharField(max_length=100)
    description = models.TextField()
    slider_img_1 = models.ImageField(upload_to='img', null=True, blank=True)
    slider_img_2 = models.ImageField(upload_to='img', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Companies"
