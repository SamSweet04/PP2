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

select *
from searcher();


create or replace function search_num()
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
        from phonebook where phonebook.number like '8707%';

end
$$ language plpgsql;

select *
from search_num();
