import mysql.connector
import csv
con=mysql.connector.connect(user='root',password='******',host='localhost', database='ali')
m=con.cursor()
q='SELECT * FROM parse'
m.execute(q)
with open('Parse.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([ i[0] for i in m.description ]) 
        writer.writerows(m.fetchall())
