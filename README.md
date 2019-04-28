# tt_mess
Для запуска склонировать репозиторий и выполнить команду `python3 run.py`


Текущий уровень покрытия тестами(по данным coverage) : `38%`
## 2 семестр

---
### 1 задание 
#### Откатиться до коммита: 

1. Наполнить БД тестовыми данными и сделать дамп базы
* Скрипт для создания тестовых данных лежит по адресу `app/utils/data_generator.py`
* Дамп базы лежит по адресу `sql/002_fake_data.sql`

2. Использовать memcached
* Кэширование добавлено к методу `get_chats` в файле `app/model.py`
* В случае если происходит срабатывания метода `add_new_chat` кэш для данного юзера обнуляется

3. Использование профайлера
* Профайлер был добавлен в `app/__init__.py`
* Результаты для профайлера при запросах `get_chats`, `get_messages` и `get_users`, соответственно, лежит в файле `profiler_result.txt`

---
### 2 задание
#### Откатиться до коммита: 

1. Утилита для сравнения двух json-объектов
* Сначала делаю предварительную сортировку, а затем уже сравниваю
* Функция `equals_json` лежит в `app/utils/json_comparer.py`
* Тест лежит в `python tests/general_tests/json_comparer_test.py`
2. Selenium тест
* Тест лежит по адресу `test/general_tests/selenium_test.py`
* Запускать по команде `python tests/general_tests/selenium_test.py`
3. Тест с mock-объектом
* Тест лежит по адресу `test/general_tests/mock_test.py`
* Mock на запрос `get_participants_of_chat`
* Запускать по команде `python tests/general_tests/mock_test.py`
4. Степень покрытия тестами с помощью coverage
* Результат в форматах .txt и .html лежит в `coverage`
* Суммарный результат покрытия тестами `51%`

---
### 3 задание 
#### Откатиться до коммита: 

1. Переписать БД на ORM
* ORM cкрипт БД из первого семестра написанный лежит в `app/db_struct.py`
* Для создания использовал `db.create_all()`
* Проверил правильность исполнения кода с помощью визуального интерфейса 
* Дамп базы лежит по адресу `sql\003_sqlalchemy.sql`
2. Сделать миграцию
* Добавил `Migrate` и `Manager` в `__init__`
* Используя команды `python run.py db init` и `python run.py db migrate` сгенерировал папку `/migrate`
3. Методы, пишущие в БД, через ORM
* Добавил в `app/db.py` методы-обертки для ORM модели
* Переписал через ORM `add_new_chat`,`add_new_user`,`add_new_message`,`add_new_attach` в файле `app/model.py`

---
### 4 задание 
#### Откатиться до коммита: 

1. Получение данных из БД через ORM
* Методы `get_messages`,`get_users` и `get_chats` теперь написаны через ORM
2. Обновление и удаление данных из БД через ORM
* Методы `remove_message`,`remove_all_messages` и `change_message_content` теперь написаны через ORM
3. Форма для валидации значений
* Форма для валидации значений User лежит в `app/forms.py`
* Добавил тест `tests/model_tests/form_validate_test.py` для проверки работы валидатора
4. Дополнительно:
* Добавил скрипт `data_generator_orm.py` для генерации данных для ORM модели

---
### 5 задание
#### Откатиться до коммита: 

1. Таск, отправляющий письмо пользователю о создании чата
* Запуск `celery -A app.celery worker --loglevel=info`
* В `app/utils/send_mail.py` лежит функция, которая отправляет письмо по указанному адресу
* Таск `send_mail_on_chat` отправляет письмо пользователю при добавлении нового чата
2. Периодический таск
* Таск `send_mail_periodic` отправляет на введенный email письмо каждые 20 сек
* В дополнение нужно запустить команду `celery -A app.celery beat --loglevel=info`
3. Flower для мониторинга задач
* Для запуска использовать `flower -A app.celery --port=5555`
* Фотография работы flower `public/flower.png`
4. Redis как брокер
* Для запуска использовать `redis-server /usr/local/etc/redis.conf`
---
### Рефакторинг
#### Теперь структура проекта выглядит так:

1. Все инициализации остались в `app/__init__.py`
2. Конфиги переехали в приватные классы и разделились на `development` и `production` 
3. Появились БД для `development` и `production`, а также структура БД была разделена на разные файлы в папке `models`
4. Запуск через `flask run` теперь работает правильно
5. Появились тесты, которые проверяют базовый функционал `tests/app_tests/db_query_test.py`, но пока они запускаются вручную. В будущем добавлю тестовый менеджер вроде `Tox` или добавлю `Travis CI`.
6. Исправил проблему с `circular imports`, но следует переписать все вызовы `app` через `app factory`  

---
### 6 задание
#### Откатиться до коммита: 

1. Создать виртуальную машину и инстанс для БД
* При переключении в `ProductionConfig` все работает на виртуальной машине
2. Создать поддомен и привязать его к внешнему IP. Получить `https` сертификат
* Сделал поддомен `turkovmatvei.chickenkiller.com`
* Получил `https`, теперь при переходе на `turkovmatvei.chickenkiller.com` происходит редирект на страницу с сертификатом.
* Оказалось, для доменов с `_` есть некоторые проблемы при использовании `certbot`
3. Развернуть на виртуальной машине nginx, настроить и наладить процесс обновления
* Настроил nginx и gunicorn как reverse proxy
4. Подключить удаленный инстанс БД во flask-приложении 
* Выполнил через `flask migrate`

---
### 7 задание
#### Откатиться до коммита: 

1. Функция, считающая расстояние Левенштейна между двумя словами
2. Развернуть и наполнить тестовыми данными Elasticsearch
3. Реализовать поиск по пользователям, чатам и сообщениям

---
### 8 задание
#### Откатиться до коммита: 

1. Развернуть проект в Docker и Docker-Compose
2. Привязать Elasticsearch к Docker-Compose
3. Создать Makefile для проекта 

---
### 9 задание
#### Откатиться до коммита: 

1. Микросервис, добавляющий дополнительный функционал сервису
2. Сделать вызов микросервиса асинхронным
3. Добавить микросервис в docker

---
### 10 задание
#### Откатиться до коммита: 

1. Сделать капчу для входа
2. Защититься от CSRF

