FROM python:3.6
RUN apt-get update && apt-get install -y python python-pip python-dev libldap2-dev libsasl2-dev
ENV PYTHONUNBUFFERED 1
RUN mkdir /src
WORKDIR /src
ADD . /src/
RUN pip install -r requirements.txt
