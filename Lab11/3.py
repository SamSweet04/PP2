
import psycopg2, re

conn = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    user = 'postgres',
    password = 'Haker15987'
)
cur = conn.cursor()
contacts = [
    ('Meirambek', '87759654547'),
    ('Delnaz', '87774754547'),
    ('Aselya', '87788885651'),
    ('Dayana', '87762275377'),
]
incorrect_values = []
pattern = r'^8777[0-9]{7}$|^8747[0-9]{7}$|^8778[0-9]{7}$|^8700[0-9]{7}$|^8707[0-9]{7}$|^8708[0-9]{7}$|^8705[0-9]{7}$|^8775[0-9]{7}$' 
for i in contacts:
    if re.search(pattern, i[1])==None:
        contacts.remove(i)
        incorrect_values.append(i)

cur.executemany('CALL inserting(%s, %s)', contacts)
print(f'List of incorrect values is: {incorrect_values}')
cur.close()
conn.commit()
conn.close()
