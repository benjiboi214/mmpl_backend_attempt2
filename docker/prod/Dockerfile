FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update \
  # psycopg2 dependencies
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  # Pillow dependencies
  && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
  # CFFI dependencies
  && apk add libffi-dev py-cffi \
  && pip install pipenv

RUN addgroup -S django \
    && adduser -S -G django django

RUN mkdir /app
WORKDIR /app


COPY ./Pipfile.lock ./Pipfile.lock

RUN pipenv --bare install --ignore-pipfile --dev
RUN pipenv install psycopg2-binary

COPY ./docker/production/entrypoint.sh entrypoint.sh
RUN sed -i 's/\r$//g' entrypoint.sh
RUN chmod +x entrypoint.sh

COPY ./docker/production/start.sh start.sh
RUN sed -i 's/\r$//g' start.sh
RUN chmod +x start.sh

COPY /api ./api

WORKDIR /app/api

ENTRYPOINT ["/app/entrypoint.sh"]

