FROM python:3.8-slim-buster as base
RUN apt-get update && \
    apt-get install gcc -y && \
    apt-get clean
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
# VOLUME . .
CMD [ "python", "feed.py", "seed/raw.txt" ]