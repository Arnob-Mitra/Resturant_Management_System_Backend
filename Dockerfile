FROM python:slim-buster

WORKDIR /app

COPY requirements.txt /app/

COPY script.sh /app/

RUN python3 -m pip install --upgrade pip

RUN python3 -m pip install -r requirements.txt

COPY . /app/