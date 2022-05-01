import psycopg2
conn  = psycopg2.connect(
     host = 'localhost',
     database = 'postgres',
     user = 'postgres',
     password = 'Haker15987'
)
cursor = conn.cursor()
cursor.execute('''
     CREATE TABLE phonebook(
          username VARCHAR(21),
          number VARCHAR(12)
     );
     '''
)

cursor.close()

conn.commit()
conn.close()