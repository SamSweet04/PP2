import psycopg2

conn = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='Haker15987'
)

cursor = conn.cursor()

username = input("name:")
list = []
for i in username.split(','):
    list.append(i)
sql = '''
     DELETE FROM phonebook WHERE username = %s;
     '''
for i in list:
    cursor.execute(sql, (i,))
conn.commit()
cursor.close()
conn.close()