# To Do App v1.0.0

This is a Todo Web Application for managing tasks with an [API Calculator WSDL](http://www.dneonline.com/calculator.asmx) and [Zeep SOAP client](https://python-zeep.readthedocs.io/en/master/) which add worked time and calculates difference between estimated time and worked time on a specific task and a basic CRUD implementation using [MVC Django framework](https://www.djangoproject.com/) to create, read and update tasks.

This README would normally document whatever steps are necessary to get the
application up and running.

Things you may want to cover:

## Python version

python 3.7.0

## System dependencies

This application runs on django 2.2.3, zeep 3.4.0, lxml 4.2.5, jQuery 3.3.1, Bootstrap CDN 4.3.1.

## Configuration

This application runs on development environment from a localhost server and port 8000

Database server configuration is defined for SQLite3, for modifying parameters and details check [database configuration file](todolistapp/settings.py)

## Database creation and initialization

Check if you are on project root directory and run on your console or CLI next command:

* python manage.py migrate

## Deployment instructions

Before database creation and initialization, check if you are on project root directory and run on your console or CLI next command for installing dependencies:

* python -m pip install django
* python -m pip install lxml==4.2.5 zeep

After database creation and initialization, check if you are on project root directory and run on your console or CLI next commands for checking dependencies and running server:

* python -m pip freeze
* python manage.py runserver

Check on your console or CLI if your localhost server is running, after that, type [localhost:8000](http://localhost:8000) on your browser and check if you can view home page.

## Routing dependencies

Please check [URLs app configuration file](todo_list/urls.py)

You can view all routes, running on your console or CLI next command from project root directory:
rails routes

## Next improvements and changes

* Deployment on Heroku for local and cloud environment
