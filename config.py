from os import getenv

class Config:
    SECRET_KEY = getenv('app_secret_key') or 'super_secret_key'