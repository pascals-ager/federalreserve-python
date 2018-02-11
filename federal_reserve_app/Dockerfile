FROM python:3.6.3-jessie
MAINTAINER Advith Nagappa <advith.nagappa@gmail.com>

RUN  apt-get update &&  apt-get install -qq -y build-essential libpq-dev postgresql-client-9.4 --fix-missing --no-install-recommends


ENV INSTALL_PATH /home/advith/federal_reserve_app

ENV ENV_SETTINGS 'DevelopmentConfig'

RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD gunicorn -c "python:gunicorn" --reload --access-logfile - "app:create_app()"