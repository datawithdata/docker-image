FROM python:3.7-buster
RUN apt-get update
COPY requirements.txt .
COPY . .
RUN pip install -r requirements.txt
RUN mkdir /files
CMD gunicorn --workers=2 --bind=0.0.0.0:5000 --timeout=50 app:app
