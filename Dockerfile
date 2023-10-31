FROM python:3.10-alpine

ENV WORKDIR="/app"

WORKDIR ${WORKDIR}

RUN apk update && apk add g++ gcc unixodbc-dev curl

#Download the desired package(s)
RUN curl -O https://download.microsoft.com/download/e/4/e/e4e67866-dffd-428c-aac7-8d28ddafb39b/msodbcsql17_17.10.5.1-1_amd64.apk && \
curl -O https://download.microsoft.com/download/e/4/e/e4e67866-dffd-428c-aac7-8d28ddafb39b/mssql-tools_17.10.1.1-1_amd64.apk

#Install the package(s)
RUN apk add --allow-untrusted msodbcsql17_17.10.5.1-1_amd64.apk && \
apk add --allow-untrusted mssql-tools_17.10.1.1-1_amd64.apk

RUN pip3 install poetry

COPY pyproject.toml manage.py ${WORKDIR}/

RUN poetry export -f requirements.txt -o requirements.txt --without-hashes && pip3 install -r requirements.txt

ARG port=8000

ENV PORT=${port}

EXPOSE ${port}

ARG username="admin"
ARG password="admin"

ARG db_name="gpapp"
ARG db_user="sa"
ARG db_pass="h4Gl*IdRO+"
ARG db_host="localhost"
ARG db_port="1433"

ENV DJANGO_SECRET_KEY="some_secret_key" \
    DJANGO_SUPERUSER_USERNAME=${username} \
    DJANGO_SUPERUSER_PASSWORD=${password} \
    DJANGO_DB_NAME=${db_name} \
    DJANGO_DB_USER=${db_user} \
    DJANGO_DB_PASS=${db_pass} \
    DJANGO_DB_HOST=${db_host} \
    DJANGO_DB_PORT=${db_port}

COPY entrypoint.sh ${WORKDIR}/

COPY gpapp ${WORKDIR}/gpapp/

ENTRYPOINT ["./entrypoint.sh"]
