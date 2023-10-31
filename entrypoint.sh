#!/bin/sh

python manage.py migrate
python manage.py createsuperuser --noinput --name ${DJANGO_SUPERUSER_USERNAME} --email ${DJANGO_SUPERUSER_USERNAME}@${DJANGO_SUPERUSER_USERNAME}.com --dob 2001-01-01 --profile 3
python manage.py runserver 0.0.0.0:${PORT}
