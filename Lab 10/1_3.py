import psycopg2

conn = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='Haker15987'
)

cursor = conn.cursor()

username = input()
phone = input()


sql = '''
     UPDATE phonebook
     SET username=%s WHERE phone=%s;
     '''

cursor.execute(sql, (username, phone))
conn.commit()

cursor.close()
conn.close()