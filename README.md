# Yandex-Backend
Тестовое задание для поступления в Яндекс школу бэкенд-разработки
## Использование сервера
Сервер доступен по адресу **84.201.135.43:8080** и функционирует в соответсвтвии с [документацией](https://disk.yandex.ru/d/TbWKTZbnOST80Q?w=1 "документацией")

- Сервер использует часовой пояс UTC

## Алгоритм запуска сервера

Для развёртывания и запуска сервера необходимо:

- Установить [Docker](https://docs.docker.com/get-docker/)
- Установить [Docker-Compose](https://docs.docker.com/compose/install/)
- Скопировать репозиторий командой
`git clone https://github.com/Shureck/Yandex-Backend.git`
- Выполнить из корневой папки проекта команду
`docker-compose up -d --build`
- Дождаться завершения сборки и запуска

В случае возникновения ошибки выполнения файла entrypoint.sh:
> ERROR: for web Cannot start service web: OCI runtime create failed: container_linux.go: starting container process caused: exec: "/usr/src/app/entrypoint.sh": permission denied: unknown

Выполнить в корне папки **djangoProject** команду
`chmod +x ./entrypoint.sh`

## Тестирование

Для тестирования написан скрипт tests.py

Тестирование выполняется во время запуска сервера. Увидеть его результаты можно в логах docker-compose. Для запуска docker-compose с возможностью просмотра логов используйте команду `docker-compose up --build`

Для одтельного запуска тестов необходимо в корне проекта выполнить команду
`docker-compose exec web python manage.py test`

## Использованые инструменты

В данном проекте были использованы:

- Docker и Docker Compose для сборки проекта
- Фреймворк Django
- PostgreSQL в качестве базы данных
- Cerberus для валидации данных
