create or replace procedure delete_user(username varchar)
as
$$
begin
    delete
    from phonebook s
    where s.username = $1;
end;
$$
    LANGUAGE plpgsql;

call delete_user('Amina');
select get_user('Amina');
