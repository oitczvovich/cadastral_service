FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip


WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
# Копирование файла с переменными окружения в контейнер
COPY . /app/.
# Установка переменных окружения из файла


CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8080", "other_server_main:app", "--proxy-headers"]