#!/usr/local/bin/python2.7
import sys
sys.path += ['/home/smalan/smalan/src']
from fcgi import WSGIServer
from django.core.handlers.wsgi import WSGIHandler
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'smalan.settings'
WSGIServer(WSGIHandler()).run()
