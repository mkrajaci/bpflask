FROM ubuntu:latest
MAINTAINER Mario Krajacic

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

COPY ./app
ENV HOME=/app
WORKDIR /app

RUN pip install -r requirements.txt

ENV FLASKAPP=anonpost.py

EXPOSE 5000

ENTRYPOINT ["guniconr", "-b", "0.0.0.0:5000", "-w", "-4", "wsgi:app"]