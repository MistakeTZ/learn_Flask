from dotenv import load_dotenv
from os import getenv
from database.model import DB


def main():
    # Загрузка файлов окружения
    load_dotenv()

    # Загрузка базы данных
    DB.load_database()
    # DB.create_table()

    print(DB.select(1))

    # Выгрузка базы данных
    DB.unload_database()


if __name__ == "__main__":
    main()
