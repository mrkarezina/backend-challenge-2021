FROM python:3.7.5

RUN mkdir /app
WORKDIR /app

ADD requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

ADD . /app

EXPOSE 8096
EXPOSE 80
