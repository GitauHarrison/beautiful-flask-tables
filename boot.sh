#!/bin/sh
source beautiful_flask_tables/bin/activate
flask db upgrade
exec gunicorn -b :5000 --access-logfile - --error-logfile - table:app