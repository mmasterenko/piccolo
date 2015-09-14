#!/var/www/o99-1/data/www/piccolospb.octet.spb.ru/versilia/venv/bin/python
import os
# import sys

# Add a custom Python path.
# sys.path.insert(0, "/home/user/python")

# Switch to the directory of your project. (Optional.)
os.chdir("/var/www/o99-1/data/www/piccolospb.octet.spb.ru/versilia")

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "versilia.settings"
# os.environ['DATABASE_URL'] = "postgres://mmasterenko:qwerty@localhost:5432/piccolo"

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
