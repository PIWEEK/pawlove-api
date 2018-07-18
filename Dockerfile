FROM ubuntu:17.10
FROM python:3.6-jessie
LABEL maintainer="Kaleidos hello@kaleidos.net"
WORKDIR /

# Install dependencies
RUN apt-get update
RUN apt-get install -y -qq curl vim postgresql-client

# Install requirements
COPY requirements.txt /pawlove-api/
RUN pip install --upgrade pip
RUN pip install -r /pawlove-api/requirements.txt

# Setup the application
COPY . /pawlove-api

WORKDIR /pawlove-api
