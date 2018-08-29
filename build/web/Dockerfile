FROM python:3.6.5

ARG FLASK_PORT

ADD ./requirements.txt /
ADD ./entrypoint.sh /

RUN pip install -r /requirements.txt && apt update && \
    apt install -y nano python3-dev curl && useradd flask -m

USER flask
WORKDIR /home/app/src

EXPOSE $FLASK_PORT

ENTRYPOINT ["/entrypoint.sh"]

CMD ["runserver"]
