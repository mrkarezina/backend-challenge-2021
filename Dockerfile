FROM python:3.7.5

RUN mkdir /app
WORKDIR /app

ADD requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

ADD . /app

ENV USE_S3=false

EXPOSE 8096
EXPOSE 80
