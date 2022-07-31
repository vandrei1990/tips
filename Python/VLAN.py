import sqlite3
import os 
import sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))

conn = sqlite3.connect('dummy.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS VLANS (
    id INTEGER NOT NULL UNIQUE,
    name TEXT NOT NULL,
    description TEXT
);''')
c.execute('DELETE FROM VLANS')  # flush the table

## Generating some values to have in the VLAN table
dummy_values=[(i,'VLAN'+ str(i), 'Description of VLAN'+str(i)) for i in range(1,100)]
c.executemany("INSERT INTO VLANS VALUES (?,?,?)",dummy_values)
#####

c.execute("select ID from VLANS") 
InitialVLANsnapshot=list(i[0] for i in c.fetchall())
print("My initial VLAN IDs list is ",InitialVLANsnapshot) # getting all VLAN ids, if any other vlan is inserted, we should insert it to router

c.execute("select count(*) from VLANS") 
print(c.fetchall())

exec_mode='router>'
config_mode='router(config)#'
vlan_config_mode='router(config-vlan)#'


def Cisco(operation,vlanid,description=None,vlanName=None):
    f= open("cisco_router","w+")
    f.write('{} show vlan \n{}\n'.format(exec_mode,dummy_values))
    if operation == 'create':
        f.write('{} vlan database \n{}'.format(exec_mode,vlan_config_mode))
        f.write('{} vlan {} \n'.format(vlan_config_mode,vlanid))
        f.write('{} name {} \n'.format(vlan_config_mode,vlanName))
        c.execute('INSERT INTO VLANS VALUES (?,?,?)',(vlanid,vlanName,description))
    elif operation =='delete':
        f.write('{} no vlan {} \n'.format(vlan_config_mode,vlanid))
        c.execute('DELETE FROM VLANS WHERE ID = ?',vlanid)
    elif operation =='update':
        f.write('{}configure {} \n'.format(vlan_config_mode,vlanid))  
        f.write('{}vlan {} \n'.format(vlan_config_mode,vlanid))   
        f.write('{}name {} \n'.format(vlan_config_mode,vlanName))  
        c.execute('UPDATE VLANS SET name = ?, description= ',vlanName,description)
    else:
         print("Operation not supported")   
		 
    c.execute('SELECT * from VLANS')	
    f.write('\n{}show vlan \n{}'.format(exec_mode,c.fetchall()))
    f.close()


   
j_exec_mode='root@host>'
j_config_mode='root@host#'

def Juniper(operation,vlanid,description=None,vlanName=None):
    f= open("juniper_router","w+")
    f.write('{} show vlans \n{}\n'.format(j_exec_mode,dummy_values))
    if operation == 'create':
        f.write('{}configure \n{}'.format(exec_mode,j_config_mode))
        f.write('{}set vlans vlanName vlan-id vlanid {} \n'.format(j_config_mode,vlanid))        
        f.write('{}commit \n'.format(j_config_mode)) 
    elif operation =='delete':
        f.write('{}configure \n{}'.format(j_exec_mode,j_config_mode))
        f.write('{}delete vlans{}'.format(j_config_mode,vlanName))
        f.write('{}commit \n'.format(j_config_mode)) 
    elif operation =='update':
        f.write('{}edit interfaces ifName unit 0 family ethernet-switching vlan {} \n'.format(j_config_mode,vlanid))    
        f.write('{}commit \n'.format(j_config_mode)) 
    else:
         print("Operation not supported")   
    c.execute('SELECT * from VLANS')	
    f.write('\n{}show vlan \n{}'.format(exec_mode,c.fetchall()))
    f.close()


operation = ['create','update','delete']
if sys.argv[1] not in operation:
 print("The operation is not known")
elif sys.argv[1] ==operation[0] and len(sys.argv) > 3 and isinstance(int(sys.argv[2]), int):
    Cisco(sys.argv[1],int(sys.argv[2]) ,str(sys.argv[3]),str(sys.argv[4:]))
	
elif sys.argv[1] ==operation[1] and len(sys.argv) == 2 and isinstance(int(sys.argv[2]), int):
    pass


elif sys.argv[1] ==operation[2]:
    pass

conn.commit()
conn.close()



''''
Cisco
create
router#config t
router(config)#interface vlan 10
router(config)#ip address 10.10.10.1 255.255.255.0
router(config)#no shut

# router# vlan database
# router(vlan)# vlan 10
# router(vlan)# name test10
# router(vlan)#apply
# router(vlan)#exit

delete
router(config)#no vlan
update
SW1(config)#vlan 11
SW1(config-vlan)#name Accounting
SW1(config-vlan)#exit

'''

'''
Juniper
create:
root@test# set vlans visitor-vlan vlan-id 300
commit

delete:

root@test# delete vlans vlan010
commit

root@test#delete interfaces ge/0/0 unit 0 family ethernet-switching vlan members 10
root@test#delete interfaces vlan unit 10
commit

update:
edit interfaces ifName unit 0 family ethernet-switching vlan
commit


=
'''


