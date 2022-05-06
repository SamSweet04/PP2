import psycopg2


conn = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    user = 'postgres',
    password = 'Haker15987'
)

cur = conn.cursor()

offset = 4

s = "select * from phonebook order by username"
s += " offset " + str(offset)


cur.execute(s)
res = cur.fetchall()
print(res)


cur.close()
conn.commit()
conn.close()
