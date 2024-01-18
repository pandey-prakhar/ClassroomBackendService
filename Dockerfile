# Dockerfile
FROM python:3.8.8

WORKDIR /app

COPY . /app/
RUN pip install -r requirements.txt
EXPOSE 5000

CMD bash -c '$env:FLASK_APP = "core/server.py" && Remove-Item "core/store.sqlite3" && flask db upgrade -d core/migrations/ && flask run'
