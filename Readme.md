## Общее
- `news/` - приложение с новостями
- `weather/` - приложение с погодой
- `weather_service/` - наносервис на FastAPI для прогноза погоды
- `utils/` - вспомогательные функции
- `run` - bash скрипт для запуска сервера в Docker
- `Makefile` - полезные команды для разработки
- `.pylintrc` - конфигурация Pylint
## Запуск
Суперпользователь генерируется по .env файлу
```shell
make env

# Вручную заполнить .env файл

docker compose up -d
```
## Функционал и вопросы
Реализовал весь функционал из задания, отрефакторить не успел, также, хотел бы добавить тесты и Openapi

Добавил проверку кода `pylint` и в CI
- Превью для изображения решил уменьшать до 200px по БОЛЬШЕЙ стороне, это кажется логичным с точки зрения интерфейсов,
так все стороны изображения будет не более 200px
- Чтобы не замедлять обработку запросов возможно лучше делать масштабирование изображения в другом процессе
- В целях масштабирования и репликации возможно стоит пересмотреть идею локального хранения файлов
- При большом объеме новостей возможно стоит добавить `Nginx`
- Для xlsx импорта подключил `django-import-export`, также сделал ручку для экспорта `api/weather/weather_report/export`
с query-параметрами `place` и `date`. Добавил rate limiter, но если расчитывать на большое кол-во операций, возможно
стоит ограничить объемы экспорта, (чтобы не было переполнения RAM) + реализовать паттерн отложенных операций в API.
- Написал простой сервис рандомной погоды на `FastAPI` в `weather_service/`