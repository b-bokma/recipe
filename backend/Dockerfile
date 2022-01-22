FROM python:3.9 as requirements-stage

WORKDIR /tmp
RUN pip install poetry
COPY pyproject.toml poetry.lock* /tmp/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.9 as production-stage

WORKDIR /app

RUN apt-get -y update && \
    apt-get -y upgrade

RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add && \
    echo "deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main" | tee /etc/apt/sources.list.d/pgdg.list && \
    apt-get update && apt-get -y install postgresql-client-12

COPY --from=requirements-stage /tmp/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY alembic.ini .
COPY .env .
COPY app/ ./app/

ENV LOG_LEVEL info
ENV PYHTON_PATH /app/

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
