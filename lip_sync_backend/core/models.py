from django.db import models

# Create your models here.

# core/models.py
from django.db import models

class LipSyncRequest(models.Model):
    image = models.ImageField(upload_to='images/')
    script = models.TextField()
    audio = models.FileField(upload_to='audio/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
