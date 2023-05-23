class Config:
    SECRET_KEY = 'B!1w8NAt1T^%kvhUI*S^'

class DevConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'O5m2T7v4--W'
    MYSQL_DB = 'registro'
    
config = { 'development': DevConfig }