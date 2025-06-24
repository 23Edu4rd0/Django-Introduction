from django.db import models

# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    legend = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    photo = models.CharField(max_length=200, null=False, blank=False)
    credits = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return f'Fotorgrafia [nome={self.name},\n legenda={self.legend},\n descrição={self.description},\n foto={self.photo}]'

