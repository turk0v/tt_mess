FROM ubuntu:16.04

COPY . /app

RUN adduser flask --disabled-password --disabled-login
RUN apt-get update && apt-get -y install python3 python3-pip python3-venv git virtualenv libpq-dev python-dev

RUN python3 -m venv venv

RUN ./venv/bin/pip install --upgrade pip
RUN ./venv/bin/pip install -r app/requirements.txt
RUN ./venv/bin/pip install gunicorn

USER flask

ENV FLASK_APP app/wsgi.py

WORKDIR /app

EXPOSE 5000

ENTRYPOINT ["sh","/usr/src/app/boot.sh"]
