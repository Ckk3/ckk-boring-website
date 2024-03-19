FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

RUN pip install --upgrade pip

COPY ./ckkwebsite /app

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app

USER appuser

RUN pip install -r requirements.txt

RUN python manage.py collectstatic --noinput

EXPOSE 8000