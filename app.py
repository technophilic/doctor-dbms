import pyodbc
import json
from flask import request
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)
server = 'hellodoc.database.windows.net'
database = 'DOCTOR'
username = 'vikrame1999'
password = 'Viky123!'
driver= 'SQL Server'
@app.route("/")
@cross_origin(supports_credentials=True)
def login():
	
	cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
	cursor = cnxn.cursor()
	cursor.execute("select * from Hospital;")
	#row = cursor.fetchone()
	#response=''
	#while row:
	#	response=response+str(row)
	#	row = cursor.fetchone()
	results= []
	for row in cursor.fetchall():
		results.append(dict(zip('abcdefgh',row)))
	
	return jsonify(results)
@app.route('/lan',methods=['POST'])
def test():
	cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
	cursor = cnxn.cursor()
	cursor.execute("insert into Hospital values('hh00009','vhospital@gmail.com','8013491344','24Hrs','V Hospital');")
	cursor.commit(force=True);
	return ("HI")
	
@app.route('/m',methods=['GET'])
def get():
	cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
	cursor = cnxn.cursor()
	cursor.execute("select max(p_id) from patient;")
	x=cursor.fetchone()
	print(x)
	y=x[0]
	y=str(int(y[2:])+1)
	while(len(y)!=5):
		y='0'+y
	y='pp'+y	
	print(y)
	return(x)
"""@app.route('/search',methods=['POST','GET'])
def search():
	results=[]
	if request.method=='POST':
		data=request.get_json()
		res=str(data['content'])
		print(res)
		cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
		cursor = cnxn.cursor()
		cursor.execute("select * from Hospital where H_ID= ?",res)
		#print(cursor.fetchall())
		x=cursor.fetchall()
		cursor.execute("select column_name from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='Hospital';")
		y=[]
		for row in cursor.fetchall():
			y.append(row)
		print(y)	
		print(x)
		dat=[]
		for row in x:
			dat.append(row)
		fin_dat=[]		
		for row in x:
			fin_dat.append(dict(zip('abcdefgh',row)))
		print(fin_dat)
					
	else:
		return jsonify(fin_dat)		
	return jsonify(fin_dat)"""
	
@app.route('/search',methods=['POST','GET'])
def search():
	results=[]
	if request.method=='POST':
		data=request.get_json()
		res=str(data['contentone'])
		res2=str(data['contenttwo'])
		print(res,res2)
		cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
		cursor = cnxn.cursor()
		cursor.execute("select * from doctor where location= ? and d_specs= ?",(res,res2))
		#print(cursor.fetchall())
		x=cursor.fetchall()
		#cursor.execute("select column_name from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='Hospital';")
		#y=[]
		#for row in cursor.fetchall():
		#	y.append(row)
		#print(y)	
		print(x)
		dat=[]
		for row in x:
			dat.append(row)
		fin_dat=[]	
		for row in x:
			fin_dat.append(dict(zip('abcdefghijk',row)))
		print(fin_dat)
					
	else:
		return jsonify(fin_dat)		
	return jsonify(fin_dat)	
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8000, debug=True)
