FROM python:3.6-slim

ENV PYTHONUNBUFFERED 1

RUN apt-get -y update && apt-get -y install gcc default-libmysqlclient-dev

COPY ./compose/requirements.pip /requirements.pip

RUN pip3.6 install -r /requirements.pip

ADD . /oauth

WORKDIR /oauth

ENTRYPOINT ["sh", "compose/gunicorn.sh"]