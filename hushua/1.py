import os
import sys

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hushua.settings")
import django
from django.db import connection
c = connection.cursor
print 'xou:'



# import sys
# sys.path = sys.path[1:]
# import django
# print django.__path__
# print 'xoug'
from polls.models import Poll, Choice 
print Poll.objects.all()
print 'xge'