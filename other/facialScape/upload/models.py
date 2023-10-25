# File location: myapp/models.py
# File location: myapp/models.py
from django.db import models

class AnalysisResults(models.Model):
    zip_file = models.FileField(upload_to='uploads/')
    analysis_data = models.JSONField(null=True, blank=True)
    total_images = models.IntegerField(default=0)  # Total images count field
    analyzed_images = models.IntegerField(default=0)  # Analyzed images count field
