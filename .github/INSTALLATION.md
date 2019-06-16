# Installation

A point-by-point set of instructions on how to onboard yourself or another developer with the
software setup for a project.

1. Go to your Python venv directory:
    1. `cd /Users/rommel/Documents/python_venvs`
2. Create a new virtualenv:
    1. `python3 -m venv pnk_server`
    2. `source pnk_server/bin/activate`
3. Go to your project directory: 
    1. `cd /Users/rommel/Documents/github/work/romza`
4. Install cookiecutter
    1. `pip install cookiecutter`
5. Scaffold the project: 
    1. `cookiecutter gh:agconti/cookiecutter-django-rest`
6. Go to your project: 
    1. `cd pnk_server`
7. Install requirements:
    1. `pip install -r requirements.txt`
8. Create PostgreSQL database
    1. `createdb pnk_server -U postgres --password <password>`
9. Set the environment variables for your database(s):
    1. `export DATABASE_URL=postgres://postgres:<password>@127.0.0.1:5432/<DB name given to createdb>`
10. Add `SECRET_KEY` to OS environment
    1. export DJANGO_SECRET_KEY="<SECRET_KEY>"
11. Create superuser:
    1. python manage.py createsuperuser
12. Apply migrations
    1. `python manage.py migrate`
12. Run: 
    1. `python manage.py runserver`


When installing for the first time on the production server, follow some of these instructions: 
https://docs.webfaction.com/software/django/getting-started.html 


If running on the production server,
> workon pnk  
> pip3.7 install -r requirements.txt


Running the server  
> python manage.py runserver 


Creating a new app
> python manage.py startapp myapp