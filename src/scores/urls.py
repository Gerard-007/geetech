from django.core.urls import path
from . import views

urlpatterns = [
    path('music_scores', views.MusicScoreListView.as_view(), name="music_score_list"),
    path('music_scores/upload', views.UploadMusicScoreView.as_view(), name="upload_music_score"),
]