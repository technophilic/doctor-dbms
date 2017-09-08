import pyodbc
server = 'hellodoc.database.windows.net'
database = 'DOCTOR'
username = 'vikrame1999'
password = 'Viky123!'
driver= 'SQL Server'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("select * from Hospital;")
row = cursor.fetchone()
while row:
    print (str(row))
    row = cursor.fetchone()
