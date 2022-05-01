import psycopg2,csv

config  = psycopg2.connect(
     host = 'localhost',
     database = 'postgres',
     user = 'postgres',
     password = 'Haker15987'
)
current = config.cursor()
input_type = input("Please choose type:(from terminal or from file)\n")
arr = []

if input_type == "from terminal":
    name = input("Add username:\n")
    number = input("Add number:\n")
    sql = ''' INSERT INTO phonebook VALUES (%s, %s) RETURNING * '''
    current.execute(sql,(f'{name}',f'{number}'))
elif input_type == "from file":
    with open("a.csv","r") as file:
        data = csv.reader(file,delimiter =',')
        for line in data:
            arr.append(line)
    sql = ''' INSERT INTO phonebook VALUES (%s, %s) RETURNING * '''
    for row in arr:
        current.execute(sql, row)
current.close()
config.commit()
config.close()
# SELECT username,number FROM phonebook ORDER BY username;