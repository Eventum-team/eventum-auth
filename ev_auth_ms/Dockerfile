FROM python:2

ENV PYTHONUNBUFFERED 1

RUN mkdir /src
COPY . /src
RUN pip install -r /src/requirements.txt
RUN python /src/manage.py makemigrations \
 && python /src/manage.py migrate 

WORKDIR /src

ENTRYPOINT /usr/local/bin/gunicorn main.wsgi -b 0.0.0.0:8000
