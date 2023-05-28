#sending single show commands
from netmiko import ConnectHandler
from getpass import getpass

cisco1 = { 
    "device_type": "cisco_ios",
    "host": "172.16.8.4",
    "username": "admin",
    "password": "Administrator123.",
}

command = "show ip int brief", 

with ConnectHandler(**cisco1) as net_connect:
    output = net_connect.send_command(command)

print()
print(output)
print()
# Sending multiple show commands
from netmiko import ConnectHandler
from getpass import getpass

cisco1 = { 
    "device_type": "cisco_ios",
    "host": "172.16.8.4",
    "username": "admin",
    "password": "Administrator123.",
}

# Show command that we execute.
command = "show ip int brief"

with ConnectHandler(cisco1) as net_connect:
    output = net_connect.send_command(command)

command2 = "show ip arp"

with ConnectHandler(cisco1) as net_connect:
    output2 = net_connect.send_command(command2)

print()
print(output)
print(output2)
print()

#Send multiple configuration commands to a single device
from netmiko import ConnectHandler
import getpass

passwd = getpass.getpass('Please enter the password: ')

cisco_01 = {
    "device_type": "cisco_ios",
    "host": "172.16.8.4",
    "username": "admin",
    "password": "Administrator123."
    "secret": "Admin123."
}

connection = ConnectHandler(**cisco_01)
connection.enable()

config_commands = ['interface gi0/0', 'descri WAN', 'exit', 'access-list 1 permit any']
connection.send_config_set(config_commands)

print('Closing Connection')
connection.disconnect()





#Part 2: Connect to multiple IOS devices
#  Send show commands to multiple devices
from netmiko import ConnectHandler

devices = [
    {
         "device_type": "cisco_ios",
    "host": "172.16.8.4",
    "username": "admin",
    "password": "Administrator123."
    },
    {
        'device_type': 'cisco_ios',
        'host': '172.16.8.5',
        'username': 'admin',
        "password": "Administrator123."
    }
]

commands = ['show version', 'show interfaces', 'show running-config']

for device in devices:
    net_connect = ConnectHandler(**device)

    for command in commands:
        output = net_connect.send_command(command)
        print('Output from {}: {}'.format(device['host'], output))

    net_connect.disconnect()






#Send configuration commands to multiple devices( script werkt niet)
from netmiko import ConnectHandler

# Define the devices you want to connect to
devices = [
     {
         "device_type": "cisco_ios",
    "host": "172.16.8.4",
    "username": "admin",
    "password": "Administrator123."
    },
    {
        'device_type': 'cisco_ios',
        'host': '172.16.8.5',
        'username': 'admin',
        "password": "Administrator123."
    }
]

# Define the configuration commands you want to send to the devices
config_commands = [
    'vlan 30',
    'name test',
    'no shutdown'
]

# Loop through each device and send the configuration commands
for device in devices:
    # Connect to the device
    connection = ConnectHandler(**device)

    # Send the configuration commands
    output = connection.send_config_set(config_commands)

    # Disconnect from the device
    connection.disconnect()

   













#Run show commands and save the output(script werkt niet)
from netmiko import ConnectHandler

# Define the devices you want to connect to
devices =[
   [
    {
         "device_type": "cisco_ios",
    "host": "172.16.8.4",
    "username": "admin",
    "password": "Administrator123."
    
    },
    {
        'device_type': 'cisco_ios',
        'host': '172.16.8.5',
        'username': 'admin',
        "password": "Administrator123."
        
    }
]
]

# Define the show commands you want to run on the devices
show_commands = ['show version', 'show interfaces', 'show running-config']

# Loop through each device and run the show commands
for device in devices:
    # Connect to the device
    net_connect = ConnectHandler(**device)

    # Run the show commands
    output = ''
    for command in show_commands:
        output += '\nOutput from {} running command {}: \n'.format(device['host'], command)
        output += net_connect.send_command(command)
        output += '\n'

    # Disconnect from the device
    net_connect.disconnect()

    # Write the output to a file
    filename = 'output_{}.txt'.format(device['host'])
    with open(filename, 'w') as file:
        file.write(output)
        print('Output saved to file {}.'.format(filename))








#Backup the device configurations
 from netmiko import ConnectHandler

# Define device information for each device to be backed up
devices = [
    {
         "device_type": "cisco_ios",
    "host": "172.16.8.4",
    "username": "admin",
    "password": "Administrator123."
    
    },
    {
        'device_type': 'cisco_ios',
        'host': '172.16.8.5',
        'username': 'admin',
        "password": "Administrator123."
        
    }
]

# Iterate over each device and backup the configuration
for device in devices:
    # Connect to the device
    connection = ConnectHandler(**device)

    # Send the show running-config command
    output = connection.send_command('show running-config')

    # Save the output to a file
    filename = f"{device['host']}_config.txt"
    with open(filename, 'w') as file:
        file.write(output)

    # Disconnect from the device
    connection.disconnect()
    







#Configure a subset of Interfaces
from netmiko import ConnectHandler

# Define device information for each device to be configured
devices = [
     {
         "device_type": "cisco_ios",
    "host": "172.16.8.4",
    "username": "admin",
    "password": "Administrator123."
    
    },
    {
        'device_type': 'cisco_ios',
        'host': '172.16.8.5',
        'username': 'admin',
        "password": "Administrator123."
        
    }
]

# Define the subset of interfaces to be configured
interfaces = ['GigabitEthernet0/0', 'GigabitEthernet0/1']

# Define the configuration commands to be sent to the device for the subset of interfaces
config_commands = [
    'interface ' + intf for intf in interfaces,
    'ip address 172.168.8.4 255.255.255.0',
    'no shutdown'
]

# Iterate over each device and configure the subset of interfaces
for device in devices:
    # Connect to the device
    connection = ConnectHandler(**device)

    # Send the configuration commands for the subset of interfaces
    output = connection.send_config_set(config_commands)

    # Print the output to the console
    print(output)

    # Disconnect from the device
    connection.disconnect()

    
    
    
    
    
    
    #send device configuration using external file
from netmiko import ConnectHandler

# Define device information for each device to be configured
devices = [
    {
         "device_type": "cisco_ios",
    "host": "172.16.8.4",
    "username": "admin",
    "password": "Administrator123."
    
    },
    {
        'device_type': 'cisco_ios',
        'host': '172.16.8.5',
        'username': 'admin',
        "password": "Administrator123."
        
    }
]

# Define the name of the file containing the configuration commands
config_file = '172.16.8.0.txt'

# Iterate over each device and configure it using the commands in the file
for device in devices:
    # Connect to the device
    connection = ConnectHandler(**device)

    # Send the configuration commands from the file
    output = connection.send_config_from_file(config_file)

    # Print the output to the console
    print(output)

    # Disconnect from the device
    connection.disconnect()
-	Connect using a Python Dictionary
 from netmiko import ConnectHandler

device = {
  "device_type": "cisco_ios",
"host": "172.16.8.4",
"username": "admin",
"password": "Administrator123."
}

connection = ConnectHandler(**device)

output = connection.send_command('show interfaces')

print(output)

connection.disconnect()
-	Execute a script with a Function or classes
from netmiko import ConnectHandler

def connect_to_device(device):
connection = ConnectHandler(**device)


def send_command(connection, command):
output = connection.send_command(command)

# Return the output
return output

def disconnect_from_device(connection):

connection.disconnect()

device = {
"device_type": "cisco_ios",
"host": "172.16.8.4",
"username": "admin",
"password": "Administrator123."
}

connection = connect_to_device(device)

output = send_command(connection, 'show interfaces')

print(output)

disconnect_from_device(connection)

from netmiko import ConnectHandler

-	Execute a script with a statements (if, ifelse, else)
device = {
'device_type': 'cisco_ios',
    'host': '172.16.8.5',
    'username': 'admin',
    "password": "Administrator123."
 }

connection = ConnectHandler(**device)

interface_name = 'GigabitEthernet0/1'
if interface_name.startswith('GigabitEthernet'):
command = 'show interfaces ' + interface_name
else:
command = 'show interface ' + interface_name

output = connection.send_command(command)

print(output)

connection.disconnect()



