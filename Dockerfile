FROM python:alpine

RUN adduser -D table

WORKDIR /home/software_development/python/current_projects/beautiful_flask_tables

COPY requirements.txt requirements.txt

RUN python -m venv beautiful_flask_tables

RUN beautiful_flask_tables/bin/python -m pip install --upgrade pip

RUN \
    apk update && \
    apk add build-base && \ 
    apk add postgresql-dev gcc python3-dev musl-dev libffi-dev && \
    beautiful_flask_tables/bin/pip3 install -r requirements.txt && \
    beautiful_flask_tables/bin/pip3 install gunicorn pymysql cryptography

COPY app app
COPY migrations migrations
COPY create_fake_users.py create_fake_users.py
COPY table.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP table.py

RUN chown -R table:table ./
USER table

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]