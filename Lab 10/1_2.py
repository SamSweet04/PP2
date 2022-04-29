import psycopg2
conn  = psycopg2.connect(
     host = 'localhost',
     database = 'postgres',
     user = 'postgres',
     password = 'Haker15987'
)
cursor = conn.cursor()

username = 'Alina'
phone = '8662544'


sql = '''
     INSERT INTO phonebook
     VALUES(%s, %s);
     '''

cursor.execute(sql, (username, phone))
cursor.close()

conn.commit()
conn.close()