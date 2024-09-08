from datetime import datetime
from database.model import DB

class User():
    id: int
    username: str
    email: str
    password_hash: str

    posts = []


class Post():
    id: int
    user_id: int
    body: str
    timestamp: datetime