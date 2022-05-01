import psycopg2

conn  = psycopg2.connect(
     host = 'localhost',
     database = 'postgres',
     user = 'postgres',
     password = 'Haker15987'
)
current = conn.cursor()
get_type = input("Enter the type of query,please:")
if get_type == "number":
    name = input("username:")
    get = '''
        SELECT number FROM phonebook WHERE username = %s;
    '''
    current.execute(get,(name,))
    output = current.fetchone()
    print(output[0])
elif get_type == "username":
    number = input("Number:")
    get = '''
        SELECT username FROM phonebook WHERE number = %s;
    '''
    current.execute(get,(number,))
    output = current.fetchone()
    print(output[0])