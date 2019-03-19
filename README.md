# tt_mess
Для запуска склонировать репозиторий и выполнить команду `python3 run.py`

## 2 семестр

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
