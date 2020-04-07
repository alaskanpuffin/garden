FROM python:slim-buster

RUN pip install gpiozero

RUN mkdir /app

WORKDIR /app

COPY main.py /app

CMD ["python", "main.py"]
