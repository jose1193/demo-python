# Dockerfile
FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Set environment variable
ENV PYTHONUNBUFFERED 1

CMD ["python", "app.py"]
