#!/bin/sh
# gunicorn -w 1 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 app:app --reload
gunicorn --conf conf_gunicorn.py  app:app --reload

# Keep the script running to keep the container alive
tail -f /dev/null