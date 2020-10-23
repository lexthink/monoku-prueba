# lexthink/monoku-prueba

## Requirements

* **Python** >= 3.8
* **Django** >= 3.1.x
* **django-dotenv** >= 1.4.x
* **djangorestframework** >= 3.12.x
* **djangorestframework-simplejwt** >= 4.4.x

## Installation

Install it by `git clone https://github.com/lexthink/monoku-prueba` or download zip file.

```shell
$ git clone https://github.com/lexthink/monoku-prueba
$ cd monoku-prueba
$ virtualenv venv && source venv/bin/activate # optional
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py loaddata fixtures # load fake data (default users, courses, lessons, etc.)
$ python manage.py runserver
```
The development web-server is running by default in http://localhost:8000.

> NOTE: This project includes 'django-dotenv', so you can just rename the .env.dist to .env and override any variable if necessary

> NOTE: add rest_framework.renderers.BrowsableAPIRenderer to REST_FRAMEWORK.DEFAULT_RENDERER_CLASSES in config/settings.py file, to use the browsable api provided by djangorestframework

## Basic usage

You can easily test if the endpoint is working by doing the following in your terminal. (Default users with the usernames **user** and **admin** both with password **password123**)

```shell
$ curl -X POST http://localhost:8000/api/token/ -d "username=user&password=password123"
```

Alternatively, you can use all the content types supported by the Django REST framework to obtain the auth token. For example:

```shell
$ curl -X POST http://localhost:8000/api/token/ -H "Content-Type: application/json" -d '{ "username": "user", "password": "password123" }'
```

Now in order to access protected api urls you must include the `Authorization: Bearer <your_token>` header.

```shell
$ curl http://localhost:8000/protected-url/ -H "Authorization: Bearer <your_token>"
```

When this short-lived access token expires, you can use the longer-lived refresh token to obtain another access token:

```shell
$ curl -X POST "http://localhost:8000/api/token/refresh/" -H "accept: application/json" -d '{ "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImNvbGRfc3R1ZmYiOiLimIMiLCJleHAiOjIzNDU2NywianRpIjoiZGUxMmY0ZTY3MDY4NDI3ODg5ZjE1YWMyNzcwZGEwNTEifQ.aEoAYkSJjoWH1boshQAaTkf8G3yn0kapko6HFRt7Rh4" }'
```

## Documentation

Detailed documentation of all features can be found [here](docs/index.md).