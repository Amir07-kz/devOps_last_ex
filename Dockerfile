#FROM python:3.9
#
#ENV PYTHONUNBUFFERED 1
#
#RUN pip install poetry==1.3.2 && poetry config virtualenvs.create false
#
#WORKDIR /app
#COPY pyproject.toml .
#COPY poetry.lock .
#RUN poetry install
#
#COPY . /app/
#
#EXPOSE 8000
#
#WORKDIR /app/src

#CMD python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000

#CMD gunicorn shop.wsgi --bind 0.0.0.0:8000

# pull official base image
FROM python:3.10

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install poetry==1.3.2 && poetry config virtualenvs.create false

COPY pyproject.toml .
COPY poetry.lock .
RUN poetry install

COPY . .

#ENV HOME=/app/
ENV APP_HOME=/app
#RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/src/staticfiles

WORKDIR /app/src
