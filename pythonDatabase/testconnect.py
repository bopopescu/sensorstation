import subprocess
import pymysql
import threading


	#Connection configurations
DB_HOST = '127.0.0.1'
DB_USER = 'root'
DB_PASSWORD = 'windows12'
DB_NAME = 'sensorsql'



	#Getting data from sensors via C code by creating a pipe
def getSensorData():
	processOutput = subprocess.check_output('./dht11read')
	data = processOutput.split(',')
	return data

def initializeDataPolling(polling_stop,dbConn,dbCursor):
	#wrzucamy do bazy danych
	sqlquery = "insert into Temperature(Temperature,Time) values ('19.5','2017-11-13 12:39:00')"
	dbConn.execute(sqlquery)
	if not polling_stop.is_set():
		threading.Timer(5,initializeDataPolling,[polling_stop]).start()
	

def main():
	dbConn = pymysql.connect(host=DB_HOST,user=DB_USER,password=DB_PASSWORD,db=DB_NAME)
	dbCursor = dbConn.cursor()
	polling_stop = threading.Event()
	initializeDataPolling(polling_stop,dbConn)
	
	#sql = "SELECT * FROM sensorsql.Temperature;"
	#dbConn.execute(sql)
	#dbData = dbCursor.fetchall()
	#print(dbData)
	#dbConn.close()


	
if __name__ == "__main__":
	main()

