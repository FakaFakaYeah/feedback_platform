## **feedback_platform**
API предназначено для регистрации произведений, их оценки и комментариев

## **Статус workflow**
![](https://github.com/FakaFakaYeah/feedback_platform/actions/workflows/yamdb_workflow.yml/badge.svg)

## **Используемые технологии**
![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white)
![](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)
![](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)

## **Ссылки**
```
http://51.250.101.39/api/v1/ - API сервис
http://51.250.101.39/admin/ - админ панель
http://51.250.101.39/redoc/ - документация, примеры запросов
```

## **Как развернуть проект локально?**
Запустите терминал и клонируйте репозиторий 
```
https://github.com/FakaFakaYeah/feedback_platform.git
```
Создайте .env файл и заполните его

Шаблон наполнения env файла
```
DB_ENGINE=django.db.backends.postgresql   указываем, что работаем с postgresql
DB_NAME=   имя базы данных
POSTGRES_USER=   логин для подключения к базе данных
POSTGRES_PASSWORD=   пароль для подключения к БД (установите свой)
DB_HOST=db   название сервиса (контейнера)
DB_PORT=  порт для подключения к БД
```
Установите Docker по ссылке https://www.docker.com/products/docker-desktop

Перейдите в директорию с Docker-compose.yaml
```
cd infra
```

Выполните команду по разворачиванию docker-compose
```
docker-compose up -d
```

Будет проведена сборка образа по Dockerfile и запуск проекта в трех контейнерах

Выполните миграции по следующей команде:
```
docker-compose exec web python manage.py migrate
```

## Создание суперпользователя
По следующей команде вы можете создать суперпользователя, если вам нужен доступ в админ зону
```
docker-compose exec web python manage.py createsuperuser
```
Потребуется ввести имя пользователя, почту и пароль

После успешного создания суперпользователя и ввода логин/пароль на страницу http://127.0.0.1/admin/ 

## Заполнение базы начальными данными

Начальные данные хранятся в файле fixtures.json.
Для заполнения базы этими данными выполните следующие команды в терминале:
```
docker-compose exec web python manage.py loaddata fixtures.json
```
После этого загрузятся начальные данные

API запросы можно протестировать через приложение Postman, которое можно скачать по ссылке: https://www.postman.com/downloads/