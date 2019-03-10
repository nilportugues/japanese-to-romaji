FROM python:3.7.2-slim-stretch

RUN apt-get update
RUN apt-get -y install python3 python-dev python3-dev \
     build-essential libssl-dev libffi-dev \
     libxml2-dev libxslt1-dev zlib1g-dev \
     python-pip

RUN apt install -y  python3-setuptools
RUN apt install -y mecab
#RUN apt install -y mecab-python3
RUN apt install -y mecab-naist-jdic
RUN apt install -y libmecab-dev
RUN apt install -y python3-pip
