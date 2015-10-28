#!/usr/bin/env python 
import requests
import os, sys 

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from main.models import Album

response = requests.get('https://freemusicarchive.org/api/get/albums.json?api_key=VYW1FXVP9PS3R1BX')

response_dict = response.json()

print response_dict.keys()

for data in response_dict['dataset']:
    new_album, created = Album.objects.get_or_create(album_id=data['album_id'])

    new_album.artist_name = data['artist_name']
    new_album.album_handle = data['album_handle']
    # new_album.album_id = data['album_id']
    new_album.album_title = data['album_title']
    new_album.album_url = data['album_url']
    new_album.album_producer = data['album_producer']
    new_album.album_engineer = data['album_engineer']
    new_album.album_information = data['album_information']
    new_album.album_date_released = data['album_date_released']
    new_album.album_comments = data['album_comments']
    new_album.album_favorites = data['album_favorites']
    new_album.album_tracks = data['album_tracks']
    new_album.album_listens = data['album_listens']
    #new_album.album_data_created = data['album_data_created']
    new_album.album_image_file = data['album_image_file']
    new_album.album_images = data['album_images']

    print data['album_id']
    print data.get('album_images', None)
    new_album.save()



