FROM python:3.7-alpine
MAINTAINER Jorge Mtz

ENV PHYTHONBUFFERED 1
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D jorgeme0996
USER jorgeme0996