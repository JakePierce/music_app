from django.contrib import admin

from main.models import Genres, Artist, Album, Tracks
# Register your models here.

admin.site.register(Genres)
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Tracks)