import psycopg2

conn = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    user = 'postgres',
    password = 'Haker15987'
)

cur = conn.cursor()

'''
create or replace function searcher()
    returns table
            (
                username varchar(12),
                number varchar(12)
            )
as
$$
begin
    return query
        select phonebook.username,phonebook.number
        from phonebook where phonebook.username like 'A%';

end
$$ language plpgsql;
'''

cur.execute("select searcher(); ")
result = cur.fetchall()
print(result)

cur.close()
conn.commit()
conn.close()
