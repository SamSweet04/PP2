import psycopg2

n_name = input('Enter name you want insert...\n')
n_number = input('Enter phone you want insert...\n')

conn = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    user = 'postgres',
    password = 'Haker15987'
)
cur = conn.cursor()

'''
create or replace procedure inserting(n_name varchar, n_number varchar)
AS $$  
BEGIN 
    IF EXISTS (select * from phonebook where username = n_name) THEN 
        UPDATE phonebook SET number = n_number where username = n_name;
    ELSE
        INSERT INTO phonebook Values (n_name, n_number);
END IF;
END; 
$$ 
LANGUAGE plpgsql 
'''
cur.execute('CALL inserting(%s, %s)', (n_name, n_number))
cur.close()
conn.commit()
conn.close()
