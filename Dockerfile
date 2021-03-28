FROM python:3.8-slim-buster as base
RUN pip install elasticsearch-dsl>=7.0.0
WORKDIR /app
COPY . .
# VOLUME . .
CMD [ "bash" ]