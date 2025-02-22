FROM debian:latest

RUN apt update && apt install python3 -y
RUN apt install pip flask requests

WORKDIR /app

COPY . .
