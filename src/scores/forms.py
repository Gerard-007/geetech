from django import forms
from .models import MusicScore


class MusicScoreForm(forms.ModelForm):
    class Meta:
        model = MusicScore
        fields = ("title", "description", "document", "cover_picture", "composer", "price")