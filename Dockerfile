FROM python:alpine

RUN apk update && pip install pipenv==2020.8.13

WORKDIR /app
COPY . .
RUN pipenv install

ENTRYPOINT ["pipenv", "run", "python", "run.py"]

CMD []  