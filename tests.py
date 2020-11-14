import json
from database.exotics_db import Exotics

data = dict()
meta = dict()
for weapon in Exotics.select():
    '''meta["Name"] = weapon.Name
    meta["Type"] = weapon.Type
    meta["Energy"] = weapon.Energy
    meta["Unclock"] = weapon.Unlock
    meta["Description"] = weapon.Description
    meta["PicLink"] = weapon.PicLink
    data[weapon.ID] = meta'''
    meta.update({"Name": weapon.Name})
    meta.update({"Type": weapon.Type})
    meta.update({"Energy": weapon.Energy})
    meta.update({"Unlock": weapon.Unlock})
    meta.update({"Description": weapon.Description})
    meta.update({"PicLink": weapon.PicLink})
    data[weapon.ID] = meta
    # print(data)
    # meta.clear()
jsonDB = json.dumps(data, ensure_ascii=False)
print(jsonDB)