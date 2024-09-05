from dotenv import load_dotenv
from os import getenv
from database.model import DB


db: DB = None


def main():
    # Загрузка файлов окружения
    load_dotenv()

    # Загрузка базы данных
    db = DB()
    db.load_database()


if __name__ == "__main__":
    main()
