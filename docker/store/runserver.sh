#!/usr/bin/env sh

set -o errexit
set -o nounset

if [ -z "$DJANGO_ENV" ]; then
  echo "ERROR: DJANGO_ENV is Empty"
  echo 'Application will not start.'
  exit 1
fi

echo "ENV is $DJANGO_ENV"
if [ "$DJANGO_ENV" = 'dev' ]; then
  echo "Run manage.py migrate"
  python /app/manage.py migrate --noinput
  echo "Run server"
  exec  python -Wd manage.py runserver 0.0.0.0:8001
else
  echo "ERROR: DJANGO_ENV isn't valid"
  echo 'Application will not start.'
  exit 1
fi
