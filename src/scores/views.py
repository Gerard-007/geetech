from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.core.urls import reverse_lazy
from .models import MusicScore
from .forms import MusicScoreForm

# Create your views here.


class MusicScoreListView(ListView):
    model = MusicScore
    template_name = 'scores/scores.html'
    context_object_name = 'scores'


class UploadMusicScoreView(CreateView):
    model = MusicScore
    form_class = MusicScoreForm
    success_url = reverse_lazy('')
    template_name = 'upload_score.html'