from dotenv import load_dotenv
from os import getenv
from datetime import datetime, timezone
from database.model import DB
import users_app
import social as social_app


def main():
    print("Starting app...")

    # Загрузка файлов окружения
    load_dotenv()

    # Загрузка базы данных
    DB.load_database()
    DB.create_tables()

    # DB.commit("INSERT INTO posts (user_id, body, timestamp) VALUES (%s, %s, %s)", [1, "I still here)", datetime.now(timezone.utc)])
    # print(DB.get_dict("SELECT * FROM posts"))
    # print(DB.select(1))

    # Запуск сервера
    social_app.run_server()

    # Выгрузка базы данных
    DB.unload_database()


if __name__ == "__main__":
    main()
