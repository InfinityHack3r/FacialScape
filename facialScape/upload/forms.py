# File location: myapp/forms.py
from django import forms
from .models import AnalysisResults

class ZipUploadForm(forms.ModelForm):
    class Meta:
        model = AnalysisResults
        fields = ['zip_file']
