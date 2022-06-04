#!/bin/bash

cd scheduler_backend
. .venv/bin/activate
export FLASK_APP=backend
if [[ "$1" == "initdb" ]]
then
	flask initdb
fi
flask run
