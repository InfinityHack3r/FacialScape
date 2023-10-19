# File location: myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_and_analyze, name='upload_and_analyze'),
    path('results/<int:analysis_results_id>/', views.display_results, name='display_results'),
]
