from django.contrib import admin
from .models import Song, Album, CuratedPlaylist

# Register your models here.
admin.site.register(Song)
admin.site.register(Album)
admin.site.register(CuratedPlaylist)
