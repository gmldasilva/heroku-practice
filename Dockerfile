FROM python:3.9-alpine
ARG PROJECT_NAME=heroku_practice
RUN apk update \
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  && pip3 install psycopg2 \
  && apk del build-deps
COPY requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt
COPY src /app
WORKDIR /app

EXPOSE 3000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:3000", "app:api", "--timeout", "102"]