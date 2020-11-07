from peewee import *


db = SqliteDatabase("database/stat.db")


class User(Model):
    name = TextField()
    time = TimeField()
    category = TextField()

    class Meta:
        database = db
        db_table = "Users"