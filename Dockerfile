FROM ubuntu:14.04
MAINTAINER Sergio Torrado

# ES Locale
RUN locale-gen es_ES.UTF-8
ENV LANG es_ES.UTF-8
ENV LC_ALL es_ES.UTF-8

# Logs locations
RUN mkdir /logs
RUN mkdir /logs/gunicorn
RUN mkdir /logs/supervisor

# Install packages
RUN apt-get update
RUN apt-get install -y git
RUN apt-get install -y build-essential
RUN apt-get install -y libmysqlclient-dev
RUN apt-get install -y python3-dev
RUN apt-get install -y python3-setuptools
RUN apt-get install -y python-mysqldb
RUN apt-get install -y python3-urllib3
RUN apt-get install -y python3-pip
RUN apt-get install -y supervisor
RUN apt-get install -y gunicorn

ADD . /src
WORKDIR /src
RUN pip3 install -r requirements.txt

EXPOSE 8000

COPY /supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD ["/usr/bin/supervisord"]