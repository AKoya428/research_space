# ベースイメージを指定
FROM python:3.11-slim

WORKDIR /app
COPY /app /app

RUN apt-get update && apt-get install -y \
    texlive-full \
    fonts-ipaexfont \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
