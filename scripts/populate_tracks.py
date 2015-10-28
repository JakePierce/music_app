#!/usr/bin/env python 
import requests
import os, sys 

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from main.models import Tracks

response = requests.get('https://freemusicarchive.org/api/get/tracks.json?api_key=VYW1FXVP9PS3R1BX')

response_dict = response.json()

print response_dict.keys()

for data in response_dict['dataset']:
    new_tracks, created = Tracks.objects.get_or_create(track_title=data['track_title'])

    #new_tracks.track_title = data['track_title']
    new_tracks.track_url = data['track_url']
    #new_tracks.track_image_field = data['track_image_field']
    new_tracks.artist_id = int(data['artist_id'])
    new_tracks.artist_name = data['artist_name']
    new_tracks.artist_url = data['artist_url']
    new_tracks.license_url = data['license_url']
    #new_tracks.track_code_language = data['track_code_language']
    new_tracks.track_duration = data['track_duration']
    new_tracks.track_number = int(data['track_number'])
    new_tracks.track_disc_number = int(data['track_disc_number'])
    new_tracks.track_explicit = data['track_explicit']
    new_tracks.track_explicit_notes = data['track_explicit_notes']
    new_tracks.track_copyright_c = data['track_copyright_c']
    new_tracks.track_copyright_p = data['track_copyright_p']
    new_tracks.track_composer = data['track_composer']
    new_tracks.track_lyricist = data['track_lyricist']
    new_tracks.track_publisher = data['track_publisher']
    new_tracks.track_instrumental = int(data['track_instrumental'])
    new_tracks.track_information = data['track_information']
    new_tracks.track_date_recorded = data['track_date_recorded']
    new_tracks.track_file = data['track_file']
    new_tracks.license_image_file = data['license_image_file']
    new_tracks.license_image_file_large = data['license_image_file_large']
    if data['license_parent_id'] != None:

        new_tracks.license_parent_id = int(data.get('license_parent_id', 1))

    print data['track_id']
    print data.get('artist_name', None)
    new_tracks.save()
