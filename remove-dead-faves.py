"""
usage instructions:
    su
    #put file in a place the script can access
    cp /data/data/com.android.launcher/databases/launcher.db /sdcard/
    #... run script ...
    #update launcher with new database
    cp /sdcard/launcher.db /data/data/com.android.launcher/databases/ 
    #kill launcher process to reload the db
"""

import sqlite3
import os.path

conn = sqlite3.connect("/sdcard/launcher.db")

c = conn.cursor()

deadAppIds = []

for row in c.execute("select intent,_id from favorites;"):                 
    try:
        package = row[0].split(";")[4].split("=")[1].split("/")[0]
        if("." in package and len(package) > 3):        
            if(os.path.isdir("/data/data/"+package)):
                pass
            else:
                deadAppIds.append(row[1])
    except Exception as e:
        pass

for _id in deadAppIds:
    c.execute("DELETE FROM favorites WHERE _id = ?;",(_id,) )
    print("deleted ",_id)

conn.commit()
conn.close()

print("changes written")
print("finished! removed",len(deadAppIds),"dead app icons")