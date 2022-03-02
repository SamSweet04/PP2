import json

f = open("file.json")
d = json.load(f)

print('Interface Status','='* 90,sep='\n')
print('DN' , ' '*60 , 'Description' , ' '*6, 'Speed' , ' '*4 , 'MTU') 
print('-'*61 , ' ' , "-" *15 , " "*2 , "-"*6 , " "*3 , "-"*6)
y=0
for i in d['imdata']:
    y+=1
    out1=i["l1PhysIf"]["attributes"]["dn"]
    out11=i["l1PhysIf"]["attributes"]["fecMode"]
    out111=i["l1PhysIf"]["attributes"]["mtu"]

    print(out1,' '*39, out11,' ' * 2,out111)
    if y == 3:
        break

