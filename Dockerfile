FROM python:3.8-slim

WORKDIR /app
COPY . /app

RUN pip install poetry && \
  poetry config virtualenvs.create false && \
  poetry install --no-interaction --no-ansi --only main

CMD exec uvicorn app.server:app --host 0.0.0.0 --port 8001
