FROM python:3.11-slim-buster
LABEL authors="alex"

RUN apt-get update && \
    apt-get install --no-install-recommends -y libpq-dev build-essential

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1


COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt && \
    python manage.py collectstatic --no-input
