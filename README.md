# tt_mess
Для запуска склонировать репозиторий и выполнить команду `python3 run.py`

## 2 семестр
---
### 1 задание 

1. Наполнить БД тестовыми данными и сделать дамп базы
* Скрипт для создания тестовых данных лежит по адресу `app\utils\data_generator.py`
* Дамп базы лежит по адресу `sql\002_fake_data.sql`

2. Использовать memcached
* Кэширование добавлено к методу `get_chats` в файле `app\model.py`
* В случае если происходит срабатывания метода `add_new_chat` кэш для данного юзера обнуляется

3. Использование профайлера
* Профайлер был добавлен в `app\__init__.py`
* Результаты для профайлера при запросах `get_chats`, `get_messages` и `get_users`, соответственно, лежит в файле `profiler_result.txt`

---
### 2 задание

1. Утилита для сравнения двух json-объектов
* Сначала делаю предварительную сортировку, а затем уже сравниваю
* Функция `equals_json` лежит в `app\utils\json_comparer.py`
* Тест лежит в `python tests\general_tests\json_comparer_test.py`
2. Selenium тест
* Тест лежит по адресу `test\general_tests\selenium_test.py`
* Запускать по команде `python tests\general_tests\selenium_test.py`
3. Тест с mock-объектом
* Тест лежит по адресу `test\general_tests\mock_test.py`
* Mock на запрос `get_participants_of_chat`
* Запускать по команде `python tests\general_tests\mock_test.py`
4. Степень покрытия тестами с помощью coverage
* Результат в форматах .txt и .html лежит в `coverage`
* Суммарный результат покрытия тестами `51%`

---
### 3 задание 

1. Переписать БД на ORM
* ORM cкрипт БД из первого семестра написанный лежит в `app\db_struct.py`
* Для создания использовал `db.create_all()`
* Проверил правильность исполнения кода с помощью визуального интерфейса 
* Дамп базы лежит по адресу `sql\003_sqlalchemy.sql`
2. Сделать миграцию
* Добавил `Migrate` и `Manager` в `__init__`
* Используя команды `python run.py db init` и `python run.py db migrate` сгенерировал папку `\migrate`
3. Методы, пишущие в БД, через ORM
* Добавил в `app\db.py` методы-обертки для ORM модели
* Переписал через ORM `add_new_chat`,`add_new_user`,`add_new_message`,`add_new_attach` в файле `app\model.py`

---
### 4 задание 

1. Получение данных из БД через ORM
* Методы `get_messages`,`get_users` и `get_chats` теперь написаны через ORM
2. Обновление и удаление данных из БД через ORM
* Методы `remove_message`,`remove_all_messages` и `change_message_content` теперь написаны через ORM
3. Форма для валидации значений
* Форма для валидации значений User лежит в `app\forms.py`
* Добавил тест `tests\model_tests\form_validate_test.py` для проверки работы валидатора
4. Дополнительно:
* Добавил скрипт `data_generator_orm.py` для генерации данных для ORM модели

---
### 5 задание

1. Таск, отправляющий письмо пользователю о создании чата
2. Периодический таск
3. Flower для мониторинга задач
4. Redis как брокер
