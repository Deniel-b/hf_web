from peewee import *


db = SqliteDatabase("database/stat.db")
class News(Model):
    ID = PrimaryKeyField(unique=True, null=False, primary_key=True)
    New = CharField(max_length=255)
    # time = CharField(max_length=10)
    # category = CharField(max_length=255)



    class Meta:
        database = db
        db_table = "News"