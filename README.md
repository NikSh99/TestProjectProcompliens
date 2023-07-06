# TestProjectProcompliens
 Тестовое задание от Procompliens

Приложение, разработанное с использованием фреймворка Flask, которое позволяет загружать файлы,
получать информацию о загруженных файлах и выполнять фильтрацию и сортировку данных из файлов.
Реализована загрузка данных в формате csv (в качестве примера - датасет с Kaggle). 
Структура файлов неизвестна и может изменяться от файла к файлу.
Для проекта написанно 6 тестов. 

Приложение будет запущено на локальном сервере по адресу http://localhost:5000

Аутентификация и выдача JWT-токена
Метод: POST
Путь: /login
Формат запроса: JSON
Параметры запроса:
username (строка) - имя пользователя
password (строка) - пароль пользователя
{
  "username": "admin",
  "password": "password"
}

Запрос для тестирования в ручную через Git Bash:
curl -X POST -H "Content-Type: application/json" -d '{"username":"admin", "password":"password"}' http://localhost:5000/login

Загрузка файла
Метод: POST
Путь: /upload
Формат запроса: multipart/form-data
Параметры запроса:

file - файл для загрузки
Пример запроса (cURL):curl -X POST -H "Authorization: Bearer <JWT-токен>" -F "file=@<путь_к_файлу>" http://localhost:5000/upload

Получение списка файлов
Метод: GET
Путь: /files
Заголовок запроса:

Authorization - JWT-токен
Пример запроса (cURL): curl -H "Authorization: Bearer <JWT-токен>" http://localhost:5000/files

Получение данных из файла
Метод: GET
Путь: /data/<filename>
Заголовок запроса:

Authorization - JWT-токен
Параметры запроса (необязательные):
column1=value1 - фильтрация по значению в колонке column1
sort_by=column2 - сортировка по колонке column2
Пример запроса (cURL):curl -H "Authorization: Bearer <JWT-токен>" http://localhost:5000/data/<filename>?column1=value1&sort_by=column2


Тестирование
Для запуска тестов необходимо открыть консоль из корневой папки проекта и выполнить команду: pytest
При тестировании должны успешно пройти все 6 тестов.

Обратная связь - очень жду Ваше решение на почту shoshin.nikita@mail.ru или по телефону 89108655381. 

На выполнение задачи ушло около 4 часов. 