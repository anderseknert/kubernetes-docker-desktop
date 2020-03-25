FROM ubuntu:latest

COPY webhook-server.py /opt/webhook-server.py

RUN apt-get update && apt-get install -y python3

CMD ["/opt/webhook-server.py"]