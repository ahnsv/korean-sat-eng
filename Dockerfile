FROM python:3.8-slim-buster as base
RUN apt-get update && \
    apt-get install gcc -y && \
    apt-get clean
RUN pip install -r requirements.txt
WORKDIR /app
COPY . .
# VOLUME . .
CMD [ "bash" ]