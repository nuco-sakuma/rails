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