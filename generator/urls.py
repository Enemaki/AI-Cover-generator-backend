from django.urls import path
from .views import CoverLetterGeneratorView

urlpatterns = [
    # This is the single endpoint for the application.
    # A POST request here will trigger the AI generation.
    path('cover-letter/', CoverLetterGeneratorView.as_view(), name='cover-letter-generator'),
]

