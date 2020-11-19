from peewee import *


db = SqliteDatabase("database/exotics.db")
class Exotics(Model):
    Name = TextField(null=False, unique=True)
    Type = TextField(null=False)
    Unlock = TextField(null=False, unique=True)
    ID = PrimaryKeyField(null=False, unique=True, primary_key=True)
    Energy = TextField(null=False)
    PicLink = TextField(null=False)
    Description = TextField()



    class Meta:
        database = db
        db_table = "Exotics"