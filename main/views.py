from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from main.models import Genres, Artist, Album, Tracks

from main.models import CustomUser
from main.forms import UserSignUp, UserLogin

from django.contrib.auth import authenticate, login, logout

from django.db import IntegrityError


def signup(request):

    context = {}

    form = UserSignUp()

    context['form'] = form

    if request.method == 'POST':

        form = UserSignUp(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                new_user = CustomUser.objects.create_user(email, password)

                auth_user = authenticate(email=email, password=password)

                login(request, auth_user)

                return HttpResponseRedirect('/')

            except IntegrityError, e:
                context['valid'] = "A User With That Name Already Exists"

        else:
            context['valid'] = form.errors

    return render_to_response('signup.html', context, context_instance=RequestContext(request))


def logout_view(request):

    logout(request)

    return HttpResponseRedirect('/')


def login_view(request):
    context = {}

    context['form'] = UserLogin()

    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():
            print "form is valid"

            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            auth_user = authenticate(email=email, password=password)

            if auth_user is not None:
                login(request, auth_user)

                print "auth_user is not None"

                return HttpResponseRedirect('/')
            else:
                context['valid'] = "Invalid User"

        else:
            context['valid'] = "Please enter a User Name"

    return render_to_response('login.html', context, context_instance=RequestContext(request))


class GenreListView(ListView):
    model = Genres
    template_name = 'genres_list.html'
    #context_object_name = 'genres'


class GenreDetailView(DetailView):
    model = Genres
    slug_field = 'genre_handle'
    template_name = 'genres_detail.html'


class GenreCreateView(CreateView):
    model = Genres
    fields = '__all__'
    template_name = 'genres_create.html'
    success_url = '/genres_list/'


class ArtistListView(ListView):
    model = Artist
    template_name = 'artist_list.html'
    context_object_name = 'artists'


class ArtistDetailView(DetailView):
    model = Artist
    slug_field = 'artist_handle'
    template_name = 'artist_detail.html'


class ArtistCreateView(CreateView):
    model = Artist
    fields = '__all__'
    template_name = 'artist_create.html'
    success_url = '/artist_list/'


class AlbumListView(ListView):
    model = Album
    template_name = 'album_list.html'
    context_object_name = 'album'


class AlbumDetailView(DetailView):
    model = Album
    slug_field = 'album_handle'
    template_name = 'album_detail.html'


class AlbumCreateView(CreateView):
    model = Album
    fields = '__all__'
    template_name = 'album_create.html'
    success_url = '/album_list/'


class TracksListView(ListView):
    model = Tracks
    template_name = 'tracks_list.html'
    context_object_name = 'tracks'


class TracksDetailView(DetailView):
    model = Tracks
    slug_field = 'track_id'
    template_name = 'tracks_detail.html'


class TracksCreateView(CreateView):
    model = Tracks
    fields = '__all__'
    template_name = 'tracks_create.html'
    success_url = '/tracks_list/'
