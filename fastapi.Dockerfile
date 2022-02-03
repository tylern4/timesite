FROM python:3.10

RUN mkdir /app
COPY requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt

COPY src/* /app

ENTRYPOINT [ "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--workers", "2"]

