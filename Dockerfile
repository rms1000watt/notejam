FROM python:2.7.15-slim-stretch
COPY ./django /django
WORKDIR /django

# TODO: Remove the manage.py stuff
RUN pip install -r requirements.txt && \
  echo "no\n" | python notejam/manage.py syncdb && \
  python notejam/manage.py migrate

CMD python notejam/manage.py runserver 0.0.0.0:8000
