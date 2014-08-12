# encoding: utf-8
from  django.db import connection
cursor = connection.cursor
print cursor