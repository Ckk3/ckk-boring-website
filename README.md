# Ckk3's Boring Website

My personal portfolio, made to showcase my skills with Web Projects, from idea to deployment.

Made with Django and PostgreSQL.

Website: https://ckk3.dev


## How to develop

This project use [devcontainers](https://code.visualstudio.com/docs/devcontainers/containers), just press f1 on vscode and select "Reopen on DevContainer". 
Create a python enviroment and install all requiriments with `pip install -r requirements.txt` 

Run `make dev` to raises a development server

Create a admin user to change data
`python manage.py createsuperuser`

## How deploy

Run `docker compose up`, ngnix, postgres and django containers will be created.

After this, enter in ckkwebsite_app container and exec this commands:

Run all migrations
`python manage.py migrate`

get all static files
`python manage.py collectstatic`

Get backup data (Optional)
`make loadbackup`

If the server goes down just raise again with
`make run`

Create a admin user to change data
`python manage.py createsuperuser`
