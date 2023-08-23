# **Feedback Platform**


![](https://github.com/FakaFakaYeah/feedback_platform/actions/workflows/yamdb_workflow.yml/badge.svg)

### Оглавление
<ol>
 <li><a href="#description">Описание проекта</a></li>
 <li><a href="#stack">Используемые технологии</a></li>
 <li><a href="#architecture">Архитектура проекта</a></li>
 <li><a href="#start_project">Как развернуть проект локально?</a></li>
 <li><a href="#superuser">Создание суперпользователя</a></li>
 <li><a href="#load_data">Заполнение базы начальными данными</a></li>
 <li><a href="#url">Ссылки проекта</a></li>
 <li><a href="#workflow">Workflow</a></li>
 <li><a href="#author">Авторы проекта</a></li>
</ol>

---
### Описание проекта:<a name="description"></a>
Открытое API для просмотра произведений, их оценки и комментариев.

---
### Используемые технологии<a name="stack"></a>
![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white)
![](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)
![](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
___
### Архитектура проекта<a name="architecture"></a>

| Директория  | Описание                                            |
|-------------|-----------------------------------------------------|
| `api_yamdb` | Код Django приложения                               |
| `infra`     | Файлы для запуска с помощью Docker, настройки Nginx |
| `test`      | Директория с тестами приложения                     |

___



### Как развернуть проект локально?<a name="start_project"></a>
* Запустите терминал и клонируйте репозиторий 
    ```
    git clone https://github.com/FakaFakaYeah/feedback_platform.git
    ```
* Создайте .env файл и заполните его

    ```
    DB_ENGINE=django.db.backends.postgresql   указываем, что работаем с postgresql
    DB_NAME=   имя базы данных
    POSTGRES_USER=   логин для подключения к базе данных
    POSTGRES_PASSWORD=   пароль для подключения к БД (установите свой)
    DB_HOST=db   название сервиса (контейнера)
    DB_PORT=  порт для подключения к БД
    ```
* Установите Docker по ссылке https://www.docker.com/products/docker-desktop

* Перейдите в директорию с Docker-compose.yaml
    ```
    cd infra
    ```

* Выполните команду по разворачиванию docker-compose
    ```
    docker-compose up -d
    ```

* Будет проведена сборка образа по Dockerfile и запуск проекта в трех контейнерах

* Выполните миграции по следующей команде:
    ```
    docker-compose exec web python manage.py migrate
    ```

___ 

### Создание суперпользователя<a name="superuser"></a>
    ```
    docker-compose exec web python manage.py createsuperuser
    ```
* Укажите имя пользователя, пароль и почту

___

### Заполнение базы начальными данными<a name="load_data"></a>


Для заполнения базы этими данными выполните следующие команды в терминале:
    ```
    docker-compose exec web python manage.py loaddata fixtures.json
    ```

---
### Ссылки проекта<a name="url"></a>
    ```
    http://51.250.101.39/api/v1/ - API сервис
    http://51.250.101.39/admin/ - админ панель
    http://51.250.101.39/redoc/ - документация, примеры запросов
    ```

API запросы можно протестировать через приложение Postman, которое можно скачать по ссылке: https://www.postman.com/downloads/

---
### Workflow<a name="workflow"></a>

В проекте есть готовый шаблон workflow, в котором есть тесты по PEP8, пуш образов
бэкенда и фронтеда на DockerHub, деплой на боевой сервер и информирование в telegram и discord.

В workflow используются следующие константы:

```
DB_ENGINE = "django.db.backends.postgresql"

DB_NAME = "имя базы данных postgres"

DB_USER = "пользователь бд"

DB_PASSWORD = "пароль"

DB_HOST = "db"

DB_PORT = "5432"

DOCKER_PASSWORD=<пароль от DockerHub>

DOCKER_USERNAME=<имя пользователя>

USER=<username для подключения к серверу>

HOST=<IP сервера>

PASSPHRASE=<пароль для сервера, если он установлен>

SSH_KEY=<ваш SSH ключ (для получения команда: cat ~/.ssh/id_rsa)>(Копировать полностью)

TELEGRAM_TO=<id чата, куда должны приходить уведомления>

TELEGRAM_TOKEN<= токен вашего бота-информатора в телеграмме>

DISCORD_WEBHOOK<= Вебхук из чата в Discord, для резервного информировани>
```

---

### Авторы проекта:<a name="author"></a>
Смирнов Степан
<div>
  <a href="https://github.com/FakaFakaYeah">
    <img src="https://github.com/FakaFakaYeah/FakaFakaYeah/blob/main/files/images/GitHub.png" title="GitHub" alt="Github" width="39" height="39"/>&nbsp
  </a>
  <a href="https://t.me/s_smirnov_work" target="_blank">
      <img src="https://github.com/FakaFakaYeah/FakaFakaYeah/blob/main/files/images/telegram.png" title="Telegram" alt="Telegram" width="40" height="40"/>&nbsp
  </a>
</div>