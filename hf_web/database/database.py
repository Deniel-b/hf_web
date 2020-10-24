from peewee import *


db = SqliteDatabase("database/stat.db")
class User(Model):
    ID = PrimaryKeyField(unique=True, null=False, primary_key=True)
    Name = CharField(max_length=255)
    time = CharField(max_length=10)
    category = CharField(max_length=255)



    class Meta:
        database = db
        db_table = "User"