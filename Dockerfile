FROM python:3.12.2-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=utf-8 \
    DEBIAN_FRONTEND=noninteractive \
    POETRY_VERSION=1.7.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false

WORKDIR /src

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    gettext \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 - && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry

RUN adduser --disabled-password --gecos "" tgbot_app

COPY docker-entrypoint.sh /src

COPY pyproject.toml poetry.lock* ./
RUN poetry install --no-root --no-interaction --no-ansi

COPY ./app /src/app

RUN pybabel compile -d /src/app/locales -D messages

RUN chown -R tgbot_app:tgbot_app /src
USER tgbot_app

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1


ENTRYPOINT ["/src/docker-entrypoint.sh"]
