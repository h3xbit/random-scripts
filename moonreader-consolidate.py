import subprocess
import time
import sqlite3
import os.path
import shutil

dbLocation = "/data/data/com.flyersoft.moonreaderp/databases/mrbooks.db"
dbName = "mrbooks.db"
libraryLocation = "/sdcard/Library/"

def init():
	#create backup database - with timestamp in name
	subprocess.call(["su", "-c" ,"cp",dbLocation,dbLocation+str(time.time())])
	#copy in local copy to sdcard to avoid permission issues
	subprocess.call(["su", "-c" ,"cp",dbLocation,"/sdcard/"+dbName])
	if not os.path.exists(libraryLocation):
		os.makedirs(libraryLocation)
	
def getAllBooksFromDB():
	books = []
	#load all files from DB with query
	conn = sqlite3.connect("/sdcard/"+dbName)
	crs = conn.cursor()
	crs.execute("select filename from books")
	results = crs.fetchall()
	crs.close()
	del crs
	conn.close()
	for row in results:
		books.append(row[0])
		#["name"]
	
	#print(results)
	return books
	
def consolidateBooks(books):
	updatedBooks = []
	i = 0
	for book in books:
		i+=1
		fileName = os.path.basename(book)
		if not os.path.isfile(libraryLocation+fileName) and os.path.isfile(book) :
			#shutil.copyfile(book, libraryLocation)
			subprocess.call(["cp",book,libraryLocation])
			updatedBooks.append(book)
			if(i == int(len(books)*0.25)): print("25% complete")
			elif(i == int(len(books)*0.5)): print("50% complete")
			elif(i == int(len(books)*0.75)): print("75% complete")
	return updatedBooks
	
def quoteStr(stringToQuote):
	return "\""+stringToQuote+"\""

def updateDB(books):
	conn = sqlite3.connect("/sdcard/"+dbName)
	crs = conn.cursor()
	for book in books:
		fileName = os.path.basename(book)
		newFileLocation = libraryLocation+fileName
		sqlCmd = " set filename={0},lowerFilename={1} where filename={2}"
		sqlCmd = sqlCmd.format(quoteStr(newFileLocation),quoteStr(newFileLocation.lower()),quoteStr(book))
		
		crs.execute("update books"+sqlCmd)
		crs.execute("update notes"+sqlCmd)
		
		sqlCmd = "update statistics set filename={0} where filename={1}"
		sqlCmd = sqlCmd.format(quoteStr(newFileLocation),quoteStr(book))
	
		crs.execute(sqlCmd)
		
	
	conn.commit()
	
	crs.close()
	del crs
	conn.close()

def overwriteDB():
	subprocess.call(["su", "-c" ,"mv","/sdcard/"+dbName,dbLocation])
	
	
def getSizeOfBooks(books):
	size = 0.0
	for book in books:
		if os.path.isfile(book):
			size+=os.path.getsize(book)/1024/1024 
	return int(size)
	
print("Creating backup copy of database")
init()
books = getAllBooksFromDB()
print(len(books),"books found in moon reader DB")
size = getSizeOfBooks(books)
print("This is a total of ",size, "MB")
if not input("Continue?") == "y":
	exit()
#TODO show size of all books and ask to continue
#copy all files found in the DB to a folder called Library
print("Consolidating ebooks")
updatedBooks = consolidateBooks(books)
print("Updating database")
#update the new file locations in the database - there are multiple tables that will need changing
updateDB(updatedBooks)
#overwrite old db
print("Overwriting DB")
overwriteDB()

#print out list of all folders of copied files
#ask to delete the original file copies 


#remove sdcard dbCopy

