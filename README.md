# Инструкции по настройке проекта

## Установка окружения

1. Создайте виртуальное окружение:
   ```bash
   python -m venv venv

2. Активируйте виртуальное окружение:
    # Для Windows:
    venv\Scripts\activate
    # Для macOS/Linux:
    source venv/bin/activate

3. Установите зависимости из файла requirements.txt:
    pip install -r requirements.txt

Настройка базы данных.
1. Создайте файл .env в корневой папке и укажите данные вашего локального сервера базы данных PostgreSQL:
    DB_HOST=localhost
    DB_PORT=5432
    DB_NAME=postgres
    DB_USER=postgres
    DB_PASS=<Ваш пароль>

2. Инициализируйте данные миграции:
    alembic init migrations

3. Создайте или выполните миграции для создания таблиц в базе данных:
    alembic revision --autogenerate -m " ВАШЕ НАЗВАНИЕ"

4. Выполните миграции:
    alembic upgrade head

<b>Создание пользователя и добавление данных о зарплате</b>

1. Запустите исполняющий(main.py) файл:
    uvicorn main:app --reload

2. Перейдите по ссылке http://127.0.0.1:8000/docs и создайте пользователя, чтобы получить JWT токен, который будет действителен в течение 1 часа.

3. Добавьте данные о зарплате сотрудника в базу данных вручную. Например, выполните запрос:

    INSERT INTO salary (user_id, current_salary, next_raise_date) 
    VALUES (1, 50000, '2024-09-05');

4. После успешного добавления данных, выполните GET запрос с помощью Postman для получения информации о сотруднике.
    Результат должен быть примерно, таким
    ![alt text](foto.png)



