release: python manage.py migrate
web: daphne backend.asgi:application -v2
worker: python manage.py runworker channels --settings=backend.settings -v2