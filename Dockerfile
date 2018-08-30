FROM python:2.7.15-slim-stretch

COPY ./django /django
WORKDIR /django

RUN pip install -r requirements.txt

CMD python notejam/manage.py runserver 0.0.0.0:8000
