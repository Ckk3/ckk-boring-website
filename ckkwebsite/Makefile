# run:
# 	gunicorn command

dev:
	python manage.py runserver

savebackup:
	python manage.py dumpdata core --exclude auth.permission --exclude contenttypes > backup.json

loadbackup:
	python manage.py loaddata backup.json
