# Dockerfile
FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# deps para compilar paquetes si hiciera falta
RUN apk add --no-cache gcc musl-dev libffi-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copia todo el proyecto
COPY . .

EXPOSE 8000

# comando por defecto: dev server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

RUN apk add --no-cache gcc musl-dev libffi-dev ca-certificates

