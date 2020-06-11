import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=AVJ\AVJSQL;'
                      'Database=new;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

cont=""
file = open("myfile.txt",'r')
cont=file.read()
cont.split('\n')
print(cont)

conn.close()
file.close()
