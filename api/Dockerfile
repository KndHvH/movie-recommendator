FROM python:3.10.11-slim

WORKDIR /app

EXPOSE 8000

COPY . .

RUN pip install --no-cache-dir -r requirements.txt


CMD ["python", "run.py"]