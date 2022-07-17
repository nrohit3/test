#read data from table
import mysql.connector as con

connect=con.connect(host='localhost',port=3306,user='root',passwd='Feb2018a')
cur=connect.cursor(buffered=True)
q1='select * from r1pred.good_raw_data'
cur.execute(q1)
print(cur.fetchall())

#Above is basic db query
