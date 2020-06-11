import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=AVJ\AVJSQL;'
                      'Database=new;'
                      'Trusted_Connection=yes;')


def read(conn):
    print("Read")
    cursor = conn.cursor()
    cursor.execute("select * from Table_1")
    for row in  cursor:
        print(f'row = {row} ')
    print()

def create(conn):
    print("create")
    cursor = conn.cursor()
    cursor.execute(
        'insert into Table_1 values(1001, "AVJ","Director");',
        
    )
    conn.commit()
    read(conn)

def update(conn):
    print("Update")
    cursor = conn.cursor()
    cursor.execute(
        'update Table_1 set b = ? where a = ? and c = ?;',
        (1002, 'Shreya','PA')
    )
    conn.commit()
    read(conn)    

def delete(conn):
    print("Delete")
    cursor = conn.cursor()
    cursor.execute(
        'delete from Table_1 where a  5;',
        (1002, 'Shreya','PA')
    )
    conn.commit()
    read(conn) 

#cursor = conn.cursor()
##cursor.execute("insert into mytest values(3, 'sumeet');")
##cursor.commit()
##
##cursor.execute("select * from mytest;")
##
##for items in cursor:
##    print(items)

read(conn)
create(conn)
update(conn)
delet(conn)

conn.close()


