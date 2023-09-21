FROM python:3.11-slim

RUN apt-get update && apt-get install -y sqlite3

WORKDIR app_cadastral/

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
COPY .env /.env
COPY . .

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "main:app"]