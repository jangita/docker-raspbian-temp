FROM python:alpine

RUN apk update && pip install pipenv==2020.8.13

WORKDIR /app
COPY . .

ENTRYPOINT ["pipenv run run.py"]

CMD []