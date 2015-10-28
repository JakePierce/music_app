#!/usr/bin/env python 
import requests
import os, sys 

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from main.models import Genres


response = requests.get('https://freemusicarchive.org/api/get/genres.json?api_key=VYW1FXVP9PS3R1BX')

response_dict = response.json()

print response_dict.keys()

for data in response_dict['dataset']:
    new_genre, created = Genres.objects.get_or_create(genre_title=data['genre_title'])

    new_genre.genre_handle = data['genre_handle']
    new_genre.genre_id = data['genre_id']
    new_genre.genre_parent_id = data['genre_parent_id']

    print data['genre_title']
    new_genre.save()
