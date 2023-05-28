# Shop

## Установка и запуск проекта

### Полностью через docker

- `docker-compose -f docker-compose.prod.yaml up` - сразу запустить всё

### Вручную

- `python3 -m venv .venv` - создать виртуальное окружение
- `poetry shell` - войти в виртуальное окружение
- `poetry install` - установить зависимости
- `pre-commit install` - установка pre-commit хуков для запуска линтеров перед коммитом
- `docker-compose up` - поднять базу данных PostgreSQL (если Вы не используете Docker, установите PostgreSQL
с официального сайта)
- `python src/manage.py migrate` - применить миграции к базе данных
- `python src/manage.py runserver` - запуск сервера для разработки
- ~~`./celery.sh` - запускает воркеры очереди сообщений (celery)~~
- ~~`celery -A testdjango flower` - запускает инструмент мониторинга очереди сообщений (celery flower)~~
