FROM python:2.7.15-slim-stretch
COPY ./django /django
WORKDIR /django
RUN pip install -r requirements.txt

# TODO: Validate these get accepted at runtime
# ENV MYSQL_HOST=$MYSQL_HOST
# ENV MYSQL_DB=$MYSQL_DB
# ENV MYSQL_USER=$MYSQL_USER
# ENV MYSQL_PASS=$MYSQL_PASS

CMD python notejam/manage.py runserver 0.0.0.0:8000
