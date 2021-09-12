FROM python:3.9-alpine
ARG PROJECT_NAME=heroku_practice
COPY requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt
COPY src /app
WORKDIR /app

EXPOSE 3000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:3000", "app:api"]