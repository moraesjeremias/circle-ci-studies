FROM python:3.9-alpine3.14
WORKDIR /app
ADD . /app
RUN pip install . --no-cache-dir
EXPOSE 8080
ENTRYPOINT uvicorn src.main:app
