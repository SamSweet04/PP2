create or replace function get_user(_username varchar)
    returns record
as
$$
declare
    phone record;
begin
    select * into phone from phonebook where phonebook.username = $1;
    return phone;
end;
$$ language plpgsql;
----------------------------------------------------------------------

create or replace procedure add_user(username varchar,number varchar)
as
$$
begin
    insert into phonebook(username, number) values ($1, $2);
end;
$$
    LANGUAGE plpgsql;


call add_user('Amina', '8707666643');
select get_user('Amina');

---------------------------------------------------------------------

DROP PROCEDURE update_user(username varchar, number varchar);
create or replace procedure update_user(username varchar, number varchar)
as
$$
begin
    update phonebook
    set number = $2
    where phonebook.username = $1;
end;
$$
    LANGUAGE plpgsql;

call update_user('Amina', '87076667809');
select get_user('Amina')

---------------------------------------------------------------
