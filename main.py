from dotenv import load_dotenv
from os import getenv
from database.model import DB
import users_app
import social.app as social_app


def main():
    print("Starting app...")

    # Загрузка файлов окружения
    load_dotenv()

    # Загрузка базы данных
    DB.load_database()
    DB.create_tables()

    # DB.commit("INSERT INTO users (name, value) VALUES (%s, %s)", ["Alex", False])
    # print(DB.get_dict("SELECT * FROM dishes"))
    # print(DB.select(1))

    # Запуск сервера
    social_app.run_server()

    # Выгрузка базы данных
    DB.unload_database()


if __name__ == "__main__":
    main()
