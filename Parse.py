import mysql.connector
import csv
con=mysql.connector.connect(user='root',password='Digital5%5',host='localhost', database='ali')
m=con.cursor()
q='SELECT * FROM parse'
m.execute(q)
with open('output.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([ i[0] for i in m.description ]) 
        writer.writerows(m.fetchall())
