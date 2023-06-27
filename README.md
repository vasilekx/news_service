# news_service
Тестовое задание на должность python backend developer. Сервер авторизации и новостей с комментариями и лайками на Django с использованием Django REST framework


[Описание тестовое задания для Django проекта](Тестовое_задание_python_django.docx)


## Применяемые технологии
[![Python](https://img.shields.io/badge/Python-3.11.3-blue?style=flat-square&logo=Python&logoColor=3776AB&labelColor=d0d0d0)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-3.2.19-blue?style=flat-square&logo=Django&logoColor=092E20&labelColor=d0d0d0)](https://www.djangoproject.com/)
[![gunicorn](https://img.shields.io/badge/gunicorn-20.1.0-blue?style=flat-square&logo=gunicorn&logoColor=499848&labelColor=d0d0d0)](https://gunicorn.org/)
[![Postgres](https://img.shields.io/badge/Postgres-14.8-blue?style=flat-square&logo=PostgreSQL&logoColor=4169E1&labelColor=d0d0d0)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/Nginx-1.24-blue?style=flat-square&logo=NGINX&logoColor=009639&labelColor=d0d0d0)](https://nginx.org/ru/)
[![Docker](https://img.shields.io/badge/Docker-24.0.2-blue?style=flat-square&logo=Docker&logoColor=2496ED&labelColor=d0d0d0)](https://www.docker.com/)
[![Docker-Compose](https://img.shields.io/badge/Docker%20Compose-2.18.1-blue?style=flat-square&logo=Docker&logoColor=2496ED&labelColor=d0d0d0)](https://www.docker.com/)

## Установка сервиса
Проверьте установлен ли у вас Docker 
```bash
docker version
```
Если Docker отсутствует, то необходимо его [установить](https://docs.docker.com/engine/install/). Вместе с Docker также устанавливается Docker Compose. После установки, проверьте установлена ли у вас Docker Compose версии 2.5.0 или новее:
```bash
docker compose version
```
Если версия Docker Compose ниже 2.5.0 необходимо [обновить Docker Compose](https://docs.docker.com/compose/install/).


Клонировать репозиторий:
```bash
git clone git@github.com:vasilekx/news_service.git
```
Перейти в папку infra 
```bash
cd infra
```
Создать в директории файл .env со следующими параметрами:
```python
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
POSTGRES_DB=postgres_db_1 # имя базы данных
POSTGRES_USER=postgres_user_1 # логин для подключения к базе данных
POSTGRES_PASSWORD=qawsed123456 # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
DJANGO_SECRET_KEY='DJANGO_SECRET_KEY' # секретный ключ Django
DJANGO_ALLOWED_HOSTS='web localhost 127.0.0.1 [::1]' # cписок хостов/доменов, для которым доступен проект
HOST_NAME=localhost # Имена сервера для NGINX
```
Создать и запустить контейнеры: 
```bash
docker-compose up --build -d
```
[***Обзор команд*** ](https://docs.docker.com/compose/reference/)*для работы с docker-compose.*

[//]: # (Выполнить миграции:)

[//]: # (```bash)

[//]: # (docker compose exec web python manage.py migrate)

[//]: # (```)

[//]: # (Создать суперпользователя:)

[//]: # (```bash)

[//]: # (docker compose exec web python manage.py createsuperuser)

[//]: # (```)

[//]: # (Собирать статические файлы:)

[//]: # (```bash)

[//]: # (docker compose exec web python manage.py collectstatic --no-input)

[//]: # (```)


## Административная панель

[http://localhost/admin/](http://localhost/admin/)


## Тестовые пользователи

| Пользователь   | Логин | Пароль      |
|----------------|-------|-------------|
| Администратор  | admin | noadmin2023 |
| Пользователь 1 | user1 | 1resu1      |
| Пользователь 2 | user2 | 2resu2      |

## Примеры запросов к API

