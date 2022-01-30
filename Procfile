release: python manage.py migrate
web: daphne backend.asgi --port $PORT --bind 0.0.0.0
worker: python manage.py runworker channel_layer