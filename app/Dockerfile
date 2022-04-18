FROM python:3.8.8-slim 

RUN mkdir /app
WORKDIR /app
RUN mkdir ../data

COPY app/ /app
COPY ../data data

RUN pip install -r requirements.txt --no-cache-dir


EXPOSE 8000
CMD uvicorn --host=0.0.0.0 main:app --log-level critical

