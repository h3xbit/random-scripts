echo "copying to sd - 0 or updating edited db- 1?"
read opt
if [ $opt = 0 ]; then 
    su -c "cp /data/data/com.android.launcher/databases/launcher.db /sdcard/"    
    echo "copied now run python clean script" 
else
    su -c "cp /sdcard/launcher.db /data/data/com.android.launcher/databases/ ;am force-stop com.android.launcher"
    rm /sdcard/launcher.db
    
fi
echo "finshed"
#su
#put file in a place the script can access
#cp /data/data/com.android.launcher/databases/launcher.db /sdcard/
#... run script ...
#update launcher with new database
#cp /sdcard/launcher.db /data/data/com.android.launcher/databases/ 
#kill launcher process to reload the db