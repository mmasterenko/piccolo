#!/var/www/o99-1/data/www/piccolospb.octet.spb.ru/versilia/venv/bin/python
import os
import sys

os.chdir("/var/www/o99-1/data/www/piccolospb.octet.spb.ru/versilia")
sys.path.insert(0, os.path.abspath(os.curdir))

#print sys.path
#exit()

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "versilia.settings"
os.environ['DATABASE_URL'] = "sqlite:///db.sqlite3"

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
