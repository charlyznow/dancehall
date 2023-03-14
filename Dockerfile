FROM python:3.9-slim-buster 

WORKDIR /app

COPY . /app/

EXPOSE 5000

CMD bash -c "while true; do sleep 1; done"