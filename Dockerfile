FROM python:3.12.2-slim-bookworm

WORKDIR /app

# RUN apt-get update

COPY docker-entrypoint.sh docker-entrypoint.sh
RUN chmod +x docker-entrypoint.sh

COPY requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /app
RUN pybabel compile -d locales -D messages;

ENTRYPOINT ["sh", "./docker-entrypoint.sh"]
