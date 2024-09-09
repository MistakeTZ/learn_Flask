from datetime import datetime
from database.model import DB
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from social import login, open_session_users


class User(UserMixin):
    id: int
    username: str
    email: str
    password_hash: str

    posts = []

    def __init__(self, id, username, email = "", password_hash = "") -> None:
        super().__init__()
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = password_hash


    def __repr__(self):
        return self.username


    def set_password_hash(self, password):
        self.password_hash = generate_password_hash(password)
        DB.commit("update user_info set password_hash=%s where username=%s", [self.password_hash, self.username])

    
    def check_password_hash(self, password):
        return check_password_hash(self.password_hash, password)


class Post():
    id: int
    user_id: int
    body: str
    timestamp: datetime


    def __repr__(self):
        return self.body



@login.user_loader
def load_user(user_id):
    return DB.get("select from user_info where user_id=%s", [user_id], True)


def get_user(user_id: str | int) -> User:
    if isinstance(user_id, str):
        username = user_id.lower()
        res = DB.get("select user_id, username, email, password_hash from user_info where lower(username) LIKE %s", [username], True)
        if not res:
            return None
    elif isinstance(user_id, int):
        res = DB.get("select user_id, username, email, password_hash from user_info where user_id=%s", [user_id], True)
        if not res:
            return None
    else:
        return None
    
    if not str(res[0]) in open_session_users:
        open_session_users[str(res[0])] = User(*res)
    return open_session_users[str(res[0])]
