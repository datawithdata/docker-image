FROM python:3.7-buster
RUN apt-get update
COPY requirements.txt .
COPY . .
RUN pip install -r requirements.txt
RUN mkdir /files
CMD gunicorn --workers=10 --bind=0.0.0.0:9999 --timeout=3 app:app