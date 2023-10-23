FROM python:3.8

RUN pip install Flask pymongo

WORKDIR /app

COPY . /app

EXPOSE 8080

CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]

