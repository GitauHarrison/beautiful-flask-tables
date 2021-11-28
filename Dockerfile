FROM python:alpine

RUN adduser -D table

WORKDIR /home/software_development/python/current_projects/official_personal_website

COPY requirements.txt requirements.txt

RUN python -m venv official_personal_website

RUN official_personal_website/bin/python -m pip install --upgrade pip

RUN \
    apk update && \
    apk add build-base && \ 
    apk add postgresql-dev gcc python3-dev musl-dev && \
    official_personal_website/bin/pip3 install -r requirements.txt && \
    official_personal_website/bin/pip3 install gunicorn

COPY app app
COPY migrations migrations
COPY create_fake_users.py create_facke_users.py
COPY table.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP table.py

RUN chown -R table:table ./
USER table

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]