web: export FLASK_APP=app:create_app \
    && flask database create \
    && flask database populate \
    && flask translate compile \
    && gunicorn wsgi:app
