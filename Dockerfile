FROM python:3.12-bullseye

RUN mkdir /app
WORKDIR /app
COPY . /app

COPY Pipfile Pipfile.lock /tmp/

RUN cd /tmp && pip install pipenv \
  && pipenv requirements > requirements.txt

RUN pip install -r /tmp/requirements.txt