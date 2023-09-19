FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    sqlite3

WORKDIR app_cadastral/

COPY ../requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
# Копирование файла с переменными окружения в контейнер
COPY .env /.env
COPY . .
# Установка переменных окружения из файла
ENV ENV_FILE=/app_cadastral/.env
RUN alembic upgrade head

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "main:app"]