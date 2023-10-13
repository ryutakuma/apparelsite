FROM python:3.9
USER root

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
RUN apt-get -y install tzdata gdal-bin libgdal-dev
RUN apt-get install -y vim less
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm
ENV HOST 0.0.0.0

ARG CPLUS_INCLUDE_PATH=/usr/include/gdal
ARG C_INCLUDE_PATH=/usr/include/gdal

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/

# setuptools のバージョンを下げないと GDAL のインストールが失敗する
# https://qiita.com/nkmr_RL/items/85edc2ee68c01ec5582e
RUN pip install setuptools==57.4.0
RUN pip install GDAL==$(gdal-config --version) --global-option=build_ext --global-option="-I/usr/include/gdal"

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
RUN pip install PyMySQL
RUN pip install djangorestframework
RUN pip install cryptography

ENV DJANGO_SETTINGS_MODULE=app.settings.localhost

RUN django-admin startproject app

#ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
