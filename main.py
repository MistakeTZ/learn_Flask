from dotenv import load_dotenv
from os import getenv
from database.model import DB
from users_app import run_server


def main():
    # Загрузка файлов окружения
    load_dotenv()

    # Загрузка базы данных
    DB.load_database()
    DB.create_table()

    # DB.commit("INSERT INTO users (name, value) VALUES (%s, %s)", ["Alex", False])
    # print(DB.get("SELECT * FROM users"))
    # print(DB.select(1))

    # Запуск сервера
    run_server()

    # Выгрузка базы данных
    DB.unload_database()


if __name__ == "__main__":
    main()
