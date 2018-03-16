#!/usr/bin/env bash

# Local
rm run/datastore/sql.db
python3 setup/schema.py
python3 setup/seed.py
python3 run/wsgi.py
rm -rf __pycache__
rm -rf run/application/__pycache__
rm -rf run/application/views/__pycache__

# Staging and production
#nohup python3 run/wsgi.py &
