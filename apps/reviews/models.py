from django.db import models

class Review(models.Model):
    content = models.TextField()
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=150)
    position = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name

class Meta:
    verbose_name_plural = 'Reviews'
