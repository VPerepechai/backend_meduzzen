#  Backend meduzzen application

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/VPerepechai/backend_meduzzen
$ cd backend_meduzzen
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r /backend/requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `venv`.

When `pip' finishes loading dependencies, create an .env file in /backend directory. Copy the contents of .env.sample and fill in depending on your variables.

To run the project:
```sh
(env)$ cd backend
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

To make migrations:
```sh
(env)$ python manage.py makemigrations
```
To make migrations for users application:
```sh
(env)$ python manage.py makemigrations users
```
To apply migrations:
```sh
(env)$ python manage.py migrate
```
To сreate super user:
```sh
(env)$ python manage.py createsuperuser
```

## Launch the app within Docker

The first thing to do is to clone the repository:
```sh
$ git clone https://github.com/VPerepechai/backend_meduzzen
$ cd backend_meduzzen/backend
```
Create an .env file in /backend directory. Copy the contents of .env.sample and fill in depending on your variables.

Before running the container, you need to create an image
```sh
$ docker build .
```

We collect an image for two containers: a database and an application:
```sh
$ docker-compose build
```

Start the containers by implicitly sourcing an environment variables file through the docker-compose command:
```sh
$ docker-compose --env-file backend/.env  up -d
```
And navigate to `http://127.0.0.1:8000/`.

To check the operation of containers:
```sh
$ docker-compose --env-file backend/.env logs -f
```

To make migrations:
```sh
$ docker-compose --env-file backend/.env exec web python manage.py makemigrations
```
To make migrations for users application:
```sh
$ docker-compose --env-file backend/.env exec web python manage.py makemigrations users
```
To apply migrations:
```sh
$ docker-compose --env-file backend/.env exec web python manage.py migrate
```
To сreate super user:
```sh
$ docker-compose --env-file backend/.env exec web python manage.py createsuperuser
```

To disable containers:
```sh
$ docker-compose down
```