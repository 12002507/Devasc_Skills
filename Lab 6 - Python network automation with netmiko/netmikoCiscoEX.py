


#### Send show commands to multiple devices
from netmiko import ConnectHandler
import threading
devices = [
    {
        'device_type': 'cisco_xe',
        'ip': '192.168.206.128',
        'username': 'cisco',
        'password': 'cisco123!.',
    }
   
    ]
def send_show_command(device):
    connection = ConnectHandler(**device)
    output = connection.send_command('show version')  
    print(f"Output from {device['ip']}:\n{output}")
    connection.disconnect()
threads = []
for device in devices:
    thread = threading.Thread(target=send_show_command, args=(device,))
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()

#### Send configuration commands to multiple devices
from netmiko import ConnectHandler
import threading
devices = [
    {
        'device_type': 'cisco_xe',
        'ip': '192.168.206.128',
        'username': 'cisco',
        'password': 'cisco123!.',
    }
   
    ]
def send_config_commands(device, commands):
    connection = ConnectHandler(**device)
    output = connection.send_config_set(commands)
    print(f"Output from {device['ip']}:\n{output}")
    connection.disconnect()
threads = []
config_commands = [
    'interface GigabitEthernet1',
    'ip address 192.168.10.1 255.255.255.0',
    'no shutdown',
    # Add more configuration commands as needed
]
for device in devices:
    thread = threading.Thread(target=send_config_commands, args=(device, config_commands))
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()


#### Run show commands and save the output
from netmiko import ConnectHandler
import threading
devices = [
    {
        'device_type': 'cisco_xe',
        'ip': '192.168.206.128',
        'username': 'cisco',
        'password': 'cisco123!.',
    }
   
    ]
def run_show_command(device, command):
    connection = ConnectHandler(**device)
    output = connection.send_command(command)
    filename = f"{device['ip']}_output.txt"
    with open(filename, 'w') as f:
        f.write(output)
    print(f"Output from {device['ip']} saved to {filename}")
    connection.disconnect()
threads = []
show_command = 'show version'
for device in devices:
    thread = threading.Thread(target=run_show_command, args=(device, show_command))
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()

#### Backup the device configurations
from netmiko import ConnectHandler
import threading

devices = [
    {
        'device_type': 'cisco_xe',
        'ip': '192.168.206.128',
        'username': 'cisco',
        'password': 'cisco123!.',
    }
   
    ]
def backup_device_config(device):
    connection = ConnectHandler(**device)
    output = connection.send_command('show running-config')
    filename = f"{device['ip']}_config.txt"
    with open(filename, 'w') as f:
        f.write(output)
    print(f"Configuration backup from {device['ip']} saved to {filename}")
    connection.disconnect()
threads = []

for device in devices:
    thread = threading.Thread(target=backup_device_config, args=(device,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

#Configure a subset of Interfaces
from netmiko import ConnectHandler
import threading

devices = [
    {
        'device_type': 'cisco_xe',
        'ip': '192.168.206.128',
        'username': 'cisco',
        'password': 'cisco123!.',
    }
   
    ]
def configure_interfaces(device, interfaces):
    connection = ConnectHandler(**device)
    interface_commands = []
    for interface in interfaces:
        interface_commands.append(f"interface {interface}")
        interface_commands.append("description Configured via Netmiko")  # Example configuration command
        # Add more configuration commands for each interface as needed
    output = connection.send_config_set(interface_commands)
    print(f"Configuration applied to interfaces on {device['ip']}")
    connection.disconnect()
threads = []

interfaces_to_configure = ['GigabitEthernet1', 'GigabitEthernet2']

for device in devices:
    thread = threading.Thread(target=configure_interfaces, args=(device, interfaces_to_configure))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

#### Send device configuration using an external file
from netmiko import ConnectHandler
import threading
devices = [
    {
        'device_type': 'cisco_xe',
        'ip': '192.168.206.128',
        'username': 'cisco',
        'password': 'cisco123!.',
    }
   
    ]
def send_config_from_file(device, config_file):
    with open(config_file, 'r') as file:
        config_commands = file.read().splitlines()
    connection = ConnectHandler(**device)
    output = connection.send_config_set(config_commands)
    print(f"Configuration applied to {device['ip']}")
    connection.disconnect()

threads = []

config_file = 'config.txt'

for device in devices:
    thread = threading.Thread(target=send_config_from_file, args=(device, config_file))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

#### Connect using a Python Dictionary
from netmiko import ConnectHandler
import threading
devices = [
    {
        'device_type': 'cisco_xe',
        'ip': '192.168.206.128',
        'username': 'cisco',
        'password': 'cisco123!.',
    }
   
    ]
def connect_to_device(device):
    connection = ConnectHandler(**device)
    # Perform actions on the device, such as running commands or sending configurations
    connection.disconnect()

threads = []

for device in devices:
    thread = threading.Thread(target=connect_to_device, args=(device,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()









