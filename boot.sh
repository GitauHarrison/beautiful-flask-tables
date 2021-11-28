#!/bin/bash
source official_personal_website/bin/activate
flask db upgrade
exec gunicorn -b :5000 --access-logfile - --error-logfile - table:app