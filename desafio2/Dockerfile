FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY app/app.py ./app.py

VOLUME ["/data"]

CMD ["python", "app.py"]

