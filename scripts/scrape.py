#!/usr/bin/env python

import urllib
import urllib2
from lxml import etree
import StringIO
import re, sys, os

sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile