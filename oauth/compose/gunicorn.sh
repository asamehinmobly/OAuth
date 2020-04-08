#!/usr/bin/env bash

# Run application
gunicorn app:app -w 4 -b 0.0.0.0:80 --timeout=10 --limit-request-line=0