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

## Launch the app within Docker

The first thing to do is to clone the repository:
```sh
$ git clone https://github.com/VPerepechai/backend_meduzzen
$ cd backend_meduzzen/backend
```

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
$ docker-compose logs -f
```

To disable containers:
```sh
$ docker-compose down
```