from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, username, password, is_staff, is_superuser):
        now = timezone.now()

        if username != None:
            email = username
            
        if not email:
            raise ValueError("Email must be sent")
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff,
                          is_active=True,
                          is_superuser=is_superuser,
                          last_login=now,
                          date_joined=now
                          )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, username=None, password=None, **extra_fields):
        return self._create_user(email, username, password, False, False, **extra_fields)

    def create_superuser(self, email, username, password, **extra_fields):
        return self._create_user(email, username, password, True, True, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', max_length=255, unique=True)
    first_name = models.CharField('first name', max_length=30, blank=True, null=True)
    last_name = models.CharField('last name', max_length=30, blank=True, null=True)
    is_staff = models.BooleanField('staff status', default=False)
    is_active = models.BooleanField('active', default=True)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.email)

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])


class Genres(models.Model):
    genre_id = models.IntegerField(null=True, blank=True)
    genre_parent_id = models.IntegerField(null=True, blank=True)
    genre_title = models.CharField(max_length=50, null=True, blank=True)
    genre_handle = models.CharField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return self.genre_title


class Artist(models.Model):
    artist_name = models.CharField(max_length=250, null=True, blank=True)
    artist_id = models.IntegerField(null=True, blank=True)
    artist_handle = models.CharField(max_length=50, null=True, blank=True)
    artist_url = models.CharField(max_length=200, null=True, blank=True)
    artist_bio = models.TextField(max_length=250, null=True, blank=True)
    artist_members = models.CharField(max_length=250, null=True, blank=True)
    artist_website = models.CharField(max_length=250, null=True, blank=True)
    artist_wikipedia_page = models.CharField(max_length=250, null=True, blank=True)
    artist_donation_url = models.CharField(max_length=250, null=True, blank=True)
    artist_contact = models.CharField(max_length=250, null=True, blank=True)
    artist_active_year_begin = models.CharField(max_length=250, null=True, blank=True)
    artist_active_year_end = models.CharField(max_length=250, null=True, blank=True)
    artist_related_projects = models.CharField(max_length=250, null=True, blank=True)
    artist_associated_labels = models.CharField(max_length=250, null=True, blank=True)
    artist_comments = models.CharField(max_length=250, null=True, blank=True)
    artist_favorites = models.CharField(max_length=250, null=True, blank=True)
    artist_date_created = models.CharField(max_length=250, null=True, blank=True)
    artist_flattr_name = models.CharField(max_length=250, null=True, blank=True)
    artist_paypal_name = models.CharField(max_length=250, null=True, blank=True)
    artist_latitude = models.CharField(max_length=250, null=True, blank=True)
    artist_longitude = models.CharField(max_length=250, null=True, blank=True)
    artist_image_file = models.CharField(max_length=250, null=True, blank=True)
    artist_location = models.CharField(max_length=250, null=True, blank=True)
    artist_images = models.CharField(max_length=250, null=True, blank=True)
    
    def __unicode__(self):
        return self.artist_name


class Album(models.Model):
    artist_name = models.CharField(max_length=250, null=True, blank=True)
    album_id = models.IntegerField(null=True, blank=True)
    album_title = models.CharField(max_length=250, null=True, blank=True)
    album_handle = models.CharField(max_length=250, null=True, blank=True)
    album_url = models.CharField(max_length=250, null=True, blank=True)
    album_producer = models.CharField(max_length=250, null=True, blank=True)
    album_engineer = models.CharField(max_length=250, null=True, blank=True)
    album_information = models.TextField(null=True, blank=True)
    album_date_released = models.CharField(max_length=250, null=True, blank=True)
    album_comments = models.CharField(max_length=250, null=True, blank=True)
    album_favorites = models.CharField(max_length=250, null=True, blank=True)
    album_tracks = models.CharField(max_length=250, null=True, blank=True)
    album_listens = models.CharField(max_length=250, null=True, blank=True)
    #album_date_created = models.CharField(max_length=250, null=True, blank=True)
    album_image_file = models.CharField(max_length=250, null=True, blank=True)
    album_images = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return "%s" % self.album_id 


class Tracks(models.Model): 
    track_id = models.IntegerField(null=True, blank=True)
    track_title = models.CharField(max_length=50, null=True, blank=True)
    track_url = models.CharField(max_length=200, null=True, blank=True)
    track_image_field = models.TextField(null=True, blank=True)
    artist_id = models.IntegerField(null=True, blank=True)
    artist_name = models.CharField(max_length=50, null=True, blank=True)
    artist_url = models.CharField(max_length=250, null=True, blank=True)
    license_url = models.CharField(max_length=250, null=True, blank=True)
    track_code_language = models.TextField(null=True, blank=True)
    track_duration = models.TextField(null=True, blank=True)
    track_number = models.IntegerField(null=True, blank=True)
    track_disc_number = models.IntegerField(null=True, blank=True)
    track_explicit = models.CharField(max_length=200, null=True, blank=True)
    track_explicit_notes = models.CharField(max_length=200, null=True, blank=True)
    track_copyright_c = models.CharField(max_length=200, null=True, blank=True)
    track_copyright_p = models.CharField(max_length=200, null=True, blank=True)
    track_composer = models.CharField(max_length=200, null=True, blank=True)
    track_lyricist = models.CharField(max_length=200, null=True, blank=True)
    track_publisher = models.CharField(max_length=200, null=True, blank=True)
    track_instrumental = models.IntegerField(null=True, blank=True)
    track_information = models.CharField(max_length=200, null=True, blank=True)
    track_date_recorded = models.TextField(null=True, blank=True)
    track_comments = models.TextField(null=True, blank=True)
    track_date_recorded = models.TextField(null=True, blank=True)
    track_file = models.TextField(null=True, blank=True)
    license_image_file = models.TextField(null=True, blank=True)
    license_image_file_large = models.TextField(null=True, blank=True)
    license_parent_id = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return "%s" % self.track_id