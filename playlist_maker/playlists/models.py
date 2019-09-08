from django.db import models

#maybe add an in movie criteria

class Album(models.Model):
    #id field is added automatically by django
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=4)

    def __str__(self):
        return self.title

class Song(models.Model):
    #id field is added automatically by django
    artist = models.CharField(max_length=200)
    song_title = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True)
    track_number = models.IntegerField(null=True)
    deluxe_only = models.CharField(max_length=1)
    single = models.CharField(max_length=1)
    genre = models.CharField(max_length=50)
    key = models.CharField(max_length=50)
    bpm = models.IntegerField(default=0)
    camelot = models.CharField(max_length=3)

    def __str__(self):
        return self.song_title + " by " + self.artist

class CuratedPlaylist(models.Model):
    #id field is added automatically by django
    name = models.CharField(max_length=200)
    platform = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " on " + self.platform
    
class SongToSetlist(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    tour_setlist = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.song + " on the " + tour_setlist + " tour"

class SongToCuratedPlaylist(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    playlist = models.ForeignKey(CuratedPlaylist, on_delete=models.CASCADE)

    def __str__(self):
        return self.song + " on the " + self.playlist + " playlist"
    
