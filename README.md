## Технологии в проекте

🔹 Python
🔹 Fastapi
🔹 Fastapi-Admin
🔹 SQLite
🔹 Docker-Compose
🔹 SQLAlchemy
## Описание
1. Сервис, который принимает запрос с указанием кадастрового номера, широты и долготы, эмулирует отправку запроса на внешний сервер, который может обрабатывать запрос до 60 секунд. Затем должен отдавать результат запроса. Внешний сервер может ответить 1 - `true` или 0 - `false`.

2. Данные запроса на сервер и ответ с внешнего сервера сохраняютс в БД. 

После сборки, приложения доступны по адресам: 
    
    - Основное cadastral_service:  
    `0.0.0.0:8000/api/`   

    - Эмулятор внешнего сервера:
    `0.0.0.0:8080/`
_______

Документация доступна по по адресу /docs/   

Эндпоинты на основной сервис 0.0.0.0:8000/api/
   - "/query" - POST - для получения запроса.

   - “/result" GET - возвращает ответ из БД от внешнего сервера.

   - "/ping" GET - проверка, что  сервер запустился.

   - “/history” GET - для получения истории запросов.

Эндпоинты на внешнем сервере  0.0.0.0:8080/

   - "/need_result" GET - возвращает 1 - `true` или 0 - `false`. Время ответа от 1 до 60 секунд.   
   - "/ping" GET - проверка, что  сервер запустился


## Установка
1. Скачать образ проекта.
```bash
git clone https://github.com/oitczvovich/cadastral_service
```

## ТЕСТИРОВАНИЕ

Активируйте venv и установите зависимости:

``` bash
python3 -m venv venv

source venv/bin/activate

pip install -r requirements_by_test.txt
```

Вызвать тесты в папке проекты где лежит файл pytest.ini

```bash
pytest
```

Дождаться результатов продолжить интсаляцию проекта.
_________

P.S. Убедитесь, что на рабочей машине есть Docker и Docker-compose, иначе установите их.

```bash
sudo apt install docker.io 
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

2. Запуститье сборку.
```bash
docker-compose up -d
```

3. Войдите в контейнер  cadastral.
```bash
docker-compose exec cadastral bash
```

4. Инициализировать миграцию.
```bash
alembic upgrade head
```

5. Подключиться к БД для создания суперпользователя. 
```bash
sqlite3 data/cadastral.db
```

6. Создать супер пользователя
```bash
BEGIN;
INSERT INTO user (username, password, is_superuser, is_active) VALUES ('admin', '<password>', 1, 1);
COMMIT;
```

## Логирование
В папке app_cadastral создается файл cadastral_log куда записываются логи c уровня INFO 


## Приложение
Документация:

`0.0.0.0:8000/docs/`   

`0.0.0.0:8080/docs/`  


## Авторы проекта
### Скалацкий Владимир
e-mail: skalakcii@yandex.ru<br>
https://github.com/oitczvovi<br>
Telegramm: @OitcZvovich
