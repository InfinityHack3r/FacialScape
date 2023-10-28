# File location: myapp/models.py

from django.db import models
from django.conf import settings

class AnalysisResults(models.Model):
    zip_file = models.FileField(upload_to='uploads/')
    analysis_data = models.JSONField(null=True, blank=True)
    total_images = models.IntegerField(default=0)  # Total images count field
    analyzed_images = models.IntegerField(default=0)  # Analyzed images count field
    webp_images = models.JSONField(default=list)

class ImageAnalysis(models.Model):
    image_hash = models.CharField(max_length=32, unique=True)  # A hash of the image file to check for duplicates
    analysis_data = models.JSONField(null=True, blank=True)  # Analysis data for this image
    webp_image_path = models.FilePathField(path=settings.MEDIA_ROOT)  # Path to the webp version of this image
 