FROM python:3.10.4

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app
COPY . /app

EXPOSE 8000

RUN python manage.py collectstatic --noinput
RUN python manage.py migrate
