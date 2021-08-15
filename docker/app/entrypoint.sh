#!/bin/bash

set -e

exec gunicorn -c docker/app/gunicorn_conf.py "app.manage:flask_app" --reload
