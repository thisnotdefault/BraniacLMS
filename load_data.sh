#!/bin/bash

python3 manage.py migrate
python3 manage.py loaddata data.json