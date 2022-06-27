FROM python:latest

WORKDIR /code

COPY . .

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD gunicorn rpg_generator.wsgi:application --bind 0.0.0.0:8001
