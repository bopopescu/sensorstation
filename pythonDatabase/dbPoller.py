import subprocess
import pymysql
import threading
import datetime

	#Connection configurations
DB_HOST = '127.0.0.1'
DB_USER = 'root'
DB_PASSWORD = 'windows12'
DB_NAME = 'sensorsql'
DB_POLLTIMEOUT = 30

	#Getting data from sensors via C code by creating a pipe
def getSensorData():
	processOutput = subprocess.check_output('./dht11read')
	data = processOutput.split(',')
	return data

class dbPoller:
	
	dbConn=""
	dbCursor=""
	
	def __init__(self):
		print("-> Aquiring connection to the database ["+DB_USER+"@"+DB_NAME+"] ...")
		self.dbConn = pymysql.connect(host=DB_HOST,user=DB_USER,password=DB_PASSWORD,db=DB_NAME)
		print("->... OK!")
		print("-> Aquiring the cursor...")
		self.dbCursor = self.dbConn.cursor()
		print("->... OK!")
	
	def run(self):
		polling_stop = threading.Event()
		self.pollData(polling_stop)
		print("-> Program running!")

	def __exit__(self):
		self.dbConn.close()

	def pollData(self, polling_stop):
		sensorData = getSensorData()
		timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		sqlqueryTemp = "insert into sensordata_temperature(temperature,time) values ('"+sensorData[0]+"','"+timestamp+"')"
		sqlqueryHumi = "insert into sensordata_humidity(humidity,time) values ('"+sensorData[1]+"','"+timestamp+"')"
		try:
			self.dbCursor.execute(sqlqueryTemp)
			self.dbCursor.execute(sqlqueryHumi)
			self.dbConn.commit()
		except:
			print("-> SQL error eccured, catch dbConn errors :)")
			self.dbConn.rollback()
		if not polling_stop.is_set():
			threading.Timer(DB_POLLTIMEOUT,self.pollData,[polling_stop]).start()
	

def main():
	print("*** Starting the data polling system ***")
	dbPollerInstance = dbPoller()
	dbPollerInstance.run()

if __name__ == "__main__":
	main()

