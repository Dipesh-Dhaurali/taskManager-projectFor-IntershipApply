web: gunicorn --bind=0.0.0.0:8080 --workers=4 taskManager.wsgi
release: python manage.py migrate && python manage.py collectstatic --noinput
