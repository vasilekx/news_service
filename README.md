# API NEWS Service
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
docker compose up --build -d
```

[***Обзор команд*** ](https://docs.docker.com/compose/reference/)*для работы с docker-compose.*


Создать суперпользователя:
```bash
docker compose exec web python manage.py createsuperuser
```

## Административная панель

[http://5.23.53.242/admin/](http://5.23.53.242/admin/)


## Тестовые пользователи

| Пользователь   | Логин | Пароль      |
|----------------|-------|-------------|
| Администратор  | admin | noadmin2023 |
| Пользователь 1 | user1 | 1resu1      |
| Пользователь 2 | user2 | 2resu2      |

## Примеры запросов к API

### Получение токена для пользователя:

###### Доступно без токена

**POST**-запрос:

```http
http://5.23.53.242/api/v1/token/
```

Тело запроса:

```json
{
    "username": "user1",
    "password": "1resu11resu1"
}
```

Ответ:

```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4Nzk3MTA0NCwiaWF0IjoxNjg3ODg0NjQ0LCJqdGkiOiJjZDhhMGMxNjU5MmM0NmNkODA3MWU2ZGJhNGQ5ODhlNSIsInVzZXJfaWQiOjJ9.Wpys3sUnPHKyHsvLd3q3tUNJir8KMcRKCrYfs13WiUU",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg4MTAwNjQ0LCJpYXQiOjE2ODc4ODQ2NDQsImp0aSI6IjAwNTJhYTQyMjY0NjQxMzI5NGRkOWE1NjAxMWNhYjkyIiwidXNlcl9pZCI6Mn0.maKM0oryiinxH0WzPjhm0uQSBZVbBeGllc9evwzIzo8"
}
```

### Создание новости:

###### Требуется токен

**POST**-запрос:

```http
http://5.23.53.242/api/v1/news/
```

Тело запроса:

```json
{
    "text": "Главный тренер сборной Франции по баскетболу Венсан Колле заявил, что центровой «Филадельфии» Джоэл Эмбиид не сыграет на чемпионате мира 2023 года, так как еще не принял решение, за какую национальную команду буде выступать. Эмбиид по итогам сезона‑2022/23 был признан самым ценным игроком лиги. Баскетболист имеет американский и французский паспорта."
}
```

Ответ:

```json
{
    "id": 2,
    "author": "user1",
    "text": "Главный тренер сборной Франции по баскетболу Венсан Колле заявил, что центровой «Филадельфии» Джоэл Эмбиид не сыграет на чемпионате мира 2023 года, так как еще не принял решение, за какую национальную команду буде выступать. Эмбиид по итогам сезона‑2022/23 был признан самым ценным игроком лиги. Баскетболист имеет американский и французский паспорта.",
    "pub_date": "2023-06-27T16:57:38.574072",
    "liked": false,
    "likes_quantity": 0,
    "comment_quantity": 0,
    "comments": []
}
```

### Создание комментария:

###### Требуется токен

**POST**-запрос:

```http
http://5.23.53.242/api/v1/news/2/comments/
```

Тело запроса:

```json
{
    "text": "Вот это новость, надо будет лайкнуть её)"
}
```

Ответ:

```json
{
    "id": 1,
    "author": "user2",
    "text": "Вот это новость, надо будет лайкнуть её)",
    "created": "2023-06-27T17:04:42.710540"
}
```

### Поставить лайк новости:

###### Требуется токен

**POST**-запрос:

```http
http://5.23.53.242/api/v1/news/2/like/
```

Ответ:

```json
{
    "detail": "Новость лайкнута."
}
```


### Получение списка всех новостей:

###### Доступно без токена

**GET**-запрос:

```http
http://5.23.53.242/api/v1/news/
```

Ответ:

```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "author": "user1",
            "text": "Итальянский специалист Андреа Пирло стал главным тренером «Сампдории», сообщается на сайте итальянского клуба.\r\n44‑летний специалист подписал контракт до 30 июня 2025 года.\r\nРанее Пирло возглавлял «Ювентус», с которым в первый год работы выиграл Суперкубок и Кубок Италии. В июне 2022 года итальянец возглавил турецкий «Фатих Карагюмрюк», за который выступает россиянин Магомед Оздоев. В конце мая Пирло покинул должность главного тренера команды.\r\nВ минувшем сезоне «Сампдория» заняла последнее место в Серии А и вылетела в Серию В.",
            "pub_date": "2023-06-27T16:46:35.810156",
            "likes_quantity": 0,
            "comment_quantity": 0,
            "comments": []
        },
        {
            "id": 2,
            "author": "user1",
            "text": "Главный тренер сборной Франции по баскетболу Венсан Колле заявил, что центровой «Филадельфии» Джоэл Эмбиид не сыграет на чемпионате мира 2023 года, так как еще не принял решение, за какую национальную команду буде выступать. Эмбиид по итогам сезона‑2022/23 был признан самым ценным игроком лиги. Баскетболист имеет американский и французский паспорта.",
            "pub_date": "2023-06-27T16:57:38.574072",
            "likes_quantity": 1,
            "comment_quantity": 1,
            "comments": [
                {
                    "id": 1,
                    "author": "user2",
                    "text": "Вот это новость, надо будет лайкнуть её)",
                    "created": "2023-06-27T17:04:42.710540"
                }
            ]
        }
    ]
}
```

