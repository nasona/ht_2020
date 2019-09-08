from django.shortcuts import render
from django.http import HttpResponse
from .models import Song

def index(request):
    #context is a dictionary mapping template variable names to Python objects
    context = {}
    return render(request, "playlists/index.html", context)

def results(request, song_id_1, song_id_2):
    try:
        song1 = Song.objects.get(pk=song_id_1)
        song2 = Song.objects.get(pk=song_id_2)
    except Song.DoesNotExist:
        raise Http404("One of the songs desired does not exist")
    context = {"song1": song1, "song2": song2}
    #response = "You're looking at the playlists between %s and %s."
    #return HttpResponse(response % song_id_1 % song_id_2)
    return render(request, "playlists/results.html", context)
