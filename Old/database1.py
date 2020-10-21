import os
import cx_Oracle

os.environ['PATH'] = 'C:\\APP\OracleHome1\instantclient_10_3'

con = cx_Oracle.connect("hr","hr","localhost/prod2")
cur = con.cursor
query1 = "select * from Department"
query2 = "select * from Employee"
cur.execute("select * from Students")
cur.execute(query1)

for cols in cur:
    print(cols[0],"   ",cols[1],"   ",cols[5])

con.commit()
cur.close()
con.close()