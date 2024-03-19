FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ./ckkwebsite/requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8000