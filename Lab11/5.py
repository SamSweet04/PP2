import psycopg2


conn = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    user = 'postgres',
    password = 'Haker15987'
)
cur = conn.cursor()


name = input('Enter username you want delete...\n')

'''
create or replace procedure deleting(name varchar)
as
$$
begin
    delete from phonebook where username = $1;
end;
$$
    language plpgsql;

'''
cur.execute('call deleting(%s)',(name,))
cur.close()
conn.commit()
conn.close()
