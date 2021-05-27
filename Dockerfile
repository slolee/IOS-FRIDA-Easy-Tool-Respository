FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /ch4njun_web

COPY . .

RUN pip install -r requirements.txt