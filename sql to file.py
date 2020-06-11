import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=AVJ\AVJSQL;'
                      'Database=new;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute("select * from Table_1 inner join Table_2 on Table_1.ID =Table_2.ID;")
#cursor.commit()

cont = ""
for i in cursor:
    cont = cont+str(i)
conn.close()

files = open('myfile.txt','a+')
files.write(cont)

files.close()


