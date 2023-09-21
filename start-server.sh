#!/usr/bin/env sh
gunicorn --workers 3 --bind 0.0.0.0:9000 challenge_skelton.wsgi:application
