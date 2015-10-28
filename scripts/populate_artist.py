#!/usr/bin/env python 
import requests
import os, sys 

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from main.models import Artist

response = requests.get('https://freemusicarchive.org/api/get/artists.json?api_key=VYW1FXVP9PS3R1BX')

response_dict = response.json()

print response_dict.keys()

for data in response_dict['dataset']:
    new_artist, created = Artist.objects.get_or_create(artist_name=data['artist_name'])

    new_artist.artist_handle = data['artist_handle']
    new_artist.artist_url = data['artist_url']
    new_artist.artist_bio = data['artist_bio']
    new_artist.artist_members = data['artist_members']
    new_artist.artist_website = data['artist_website']
    #new_artist.artist_wikipedia_page = data['wikipedia_page']
    new_artist.artist_donation_url = data['artist_donation_url']
    new_artist.artist_contact = data['artist_contact']
    new_artist.artist_active_year_begin = data['artist_active_year_begin']
    new_artist.artist_active_year_end = data['artist_active_year_end']
    new_artist.artist_related_projects = data['artist_related_projects']
    new_artist.artist_associated_labels = data['artist_associated_labels']
    new_artist.artist_comments = data['artist_comments']
    new_artist.artist_favorites = data['artist_favorites']
    new_artist.artist_date_created = data['artist_date_created']
    new_artist.artist_flattr_name = data['artist_flattr_name']
    new_artist.artist_paypal_name = data['artist_paypal_name']
    new_artist.artist_latitude = data['artist_latitude']
    new_artist.artist_longitude = data['artist_latitude']
    new_artist.artist_image_file = data['artist_image_file']
    new_artist.artist_location = data['artist_location']
    #new_artist.artist_images = data['artist_images']

    print data['artist_name']
    print data.get('artist_images', None)
    new_artist.save()

