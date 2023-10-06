run:
	gunicorn ckkwebsite.wsgi:application --bind 0.0.0.0:8000 --reload

dev:
	python manage.py runserver -v2

savebackup:
	python manage.py dumpdata core --exclude auth.permission --exclude contenttypes > backup.json

loadbackup:
	python manage.py loaddata backup.json
