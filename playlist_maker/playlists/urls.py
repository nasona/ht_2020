from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #ex: /playlists/results/27-19
    path("/results/<int:song_id_1>-<int:song_id_2", views.results, name="results"),
]
