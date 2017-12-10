FROM python:3.6-slim

RUN apt-get update \
    && apt-get install --yes git \
    && apt-get install --yes supervisor \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD . /app
WORKDIR /app

RUN pip install -r requirements.txt
CMD supervisord -c /app/supervisord.conf