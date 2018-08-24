FROM python:3.6.5

ARG FLASK_PORT

ADD ./requirements.txt /

RUN pip install -r /requirements.txt && apt update && \
    apt install -y nano python3-dev curl && useradd flask -m

USER flask
WORKDIR /home/app

EXPOSE $FLASK_PORT

CMD ["python", "app.py"]
