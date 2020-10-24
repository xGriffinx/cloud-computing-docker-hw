FROM python:3.7-slim

WORKDIR /cloud-docker
COPY . .

CMD ["python", "./main.py"]