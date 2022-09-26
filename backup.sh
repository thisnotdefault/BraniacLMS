#!/bin/bash

now=`date +%F`

python3 manage.py dumpdata > backup/$now.json
python3 manage.py dumpdata > backup/data.json
