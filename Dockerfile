FROM python:3.7-alpine

RUN mkdir /code
WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY . /code

RUN chmod 755 start-server.sh && pip install -r requirements.txt && python manage.py makemigrations && python manage.py migrate
CMD  ["/code/start-server.sh"]