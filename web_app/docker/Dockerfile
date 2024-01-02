FROM ruby:3.1.0-slim

ENV APP_ROOT /web_app
RUN mkdir -p $APP_ROOT

COPY $APP_ROOT $APP_ROOT/

WORKDIR $APP_ROOT

ADD ./web_app/Gemfile $APP_ROOT/Gemfile
ADD ./web_app/Gemfile.lock $APP_ROOT/Gemfile.lock


ENV RUNTIME_PACKAGES="\
      default-libmysqlclient-dev\
      build-essential\
    " \
    LANG=C.UTF-8 \
    TZ=Asia/Tokyo
RUN apt-get update && apt-get install -y ${RUNTIME_PACKAGES}

RUN bundle install --jobs=4

CMD rails s -b 0.0.0.0 -p 3000



FROM mysql:8.0

ADD ./web_app/docker/mysql/my.cnf /etc/mysql/conf.d/my.cnf


FROM python:3
USER root

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get install -y vim less
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN python -m pip install jupyterlab

RUN python -m pip install nba_api
RUN python -m pip install mysql-connector-python