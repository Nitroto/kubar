release: python backend/manage.py migrate
web: cd backend && gunicorn kubar.wsgi --preload --log-file -
