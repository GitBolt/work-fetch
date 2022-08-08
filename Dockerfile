FROM python:3

COPY /src /root 

WORKDIR /root

RUN pip install fastapi uvicorn requests beautifulsoup4

CMD uvicorn main:app --host 0.0.0.0 --port ${PORT}