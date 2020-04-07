FROM python:slim-buster

RUN pip install flask gpiozero gunicorn

RUN mkdir /app

WORKDIR /app

COPY main.py wsgi.py gunicorn.conf.py /app/

CMD ["gunicorn", "wsgi:app"]
