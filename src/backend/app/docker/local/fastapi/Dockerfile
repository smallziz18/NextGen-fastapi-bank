ARG PYTHON_VERSION=3.13
FROM python:${PYTHON_VERSION}-slim-bookworm AS python

# ================================
# Stage 1 : build wheels
# ================================
FROM python AS python-build-stage

RUN apt-get update && apt-get install -y \
    --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY ./backend/requirements.txt .

RUN pip wheel \
    --wheel-dir /usr/src/app/wheels \
    -r requirements.txt \
    --no-cache-dir


# ================================
# Stage 2 : runtime
# ================================
FROM python AS python-run-stage

ARG APP_HOME=/src
ARG APP_USER=fastapi
ARG APP_GROUP=fastapi

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR ${APP_HOME}

RUN apt-get update && apt-get install -y \
    --no-install-recommends \
    sudo \
    git \
    nano \
    ssh \
    libpq5 \
    gettext \
    bash-completion \
    && apt-get purge -y --auto-remove \
    && rm -rf /var/lib/apt/lists/*

# User non-root
RUN groupadd -r ${APP_GROUP} \
    && useradd -r -g ${APP_GROUP} -d ${APP_HOME} -m ${APP_USER}

# Logs
RUN mkdir -p ${APP_HOME}/backend/app/logs \
    && chown -R ${APP_USER}:${APP_GROUP} ${APP_HOME} \
    && chmod 775 ${APP_HOME}/backend/app/logs

# Install deps
COPY --from=python-build-stage /usr/src/app/wheels /wheels/

RUN pip install \
    --no-cache-dir \
    --no-index \
    --find-links=/wheels \
    /wheels/* \
    && rm -rf /wheels

# Scripts
COPY --chown=${APP_USER}:${APP_GROUP} backend/app/docker/local/fastapi/entrypoint.sh /entrypoint.sh
COPY --chown=${APP_USER}:${APP_GROUP} backend/app/docker/local/fastapi/start.sh /start.sh

RUN sed -i 's/\r$//g' /entrypoint.sh /start.sh \
    && chmod +x /entrypoint.sh /start.sh

# Code
COPY --chown=${APP_USER}:${APP_GROUP} . ${APP_HOME}

USER ${APP_USER}

ENTRYPOINT ["/entrypoint.sh"]
