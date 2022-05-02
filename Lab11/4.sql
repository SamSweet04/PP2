select * from phonebook;

do
$$
    declare
        student record;
    begin
        for student in select * from phonebook as s limit 3
            loop
                raise notice 'username=%, number=%', student.username, student.number;
            end loop;
    end
$$;

do
$$
    declare
        student record;
    begin
        for student in select * from phonebook as s offset 3
            loop
                raise notice 'username=%, number=%', student.username, student.number;
            end loop;
    end
$$;
