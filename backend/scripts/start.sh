#!/bin/bash

export FLASK_APP=/usr/src/server.py
flask run --reload --debugger --host 0.0.0.0 --port 6060

