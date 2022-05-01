import psycopg2,re
conn  = psycopg2.connect(
     host = 'localhost',
     database = 'postgres',
     user = 'postgres',
     password = 'Haker15987'
)
current = conn.cursor()
update_type = input("What you want to update?(username or number):")
if update_type == "username":
    name = input("username in phonebook:")
    new_name = input("Enter new name,please:")
    try:
        upd = '''
        UPDATE phonebook SET username = %s WHERE username = %s;
        '''
        current.execute(upd,(new_name,name))
    except:
        print("Contact with this name does not exist!")
elif update_type == "number":
    name = input("username in phonebook:")
    new_number = input("Enter new number,please:")
    pattern_1 = r"\+{1}\d+$"
    pattern_2 = r"\d+$"
    ok = True
    if re.match(pattern_1,new_number) or re.match(pattern_2,new_number):
        pass
    else:
        print("Impossible phone number!")
        ok = False
    try:
        if ok:
            upd='''
            UPDATE phonebook SET number = %s WHERE username = %s
            '''
            current.execute(upd,(new_number,name))
    except:
        print("Contact with this number does not exist!")
current.close()
conn.commit()
conn.close()