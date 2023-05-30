

# LAB 1 - PYTHON EXPERIMENTEN

## 1.1 Installatie van tools/packages op Ubuntu DEVASC-LABVM:
### Task implementation
 #### Python 3.8 en PIP installatie
  
   *In de terminal, typ de volgende commando's:*
   
    Sudo apt-get update
    Sudo apt-get upgrade
    Sudo apt install python3-pip
  
  #### Jupyter Notebook installatie
  
   * Typ de volgende commando's in de terminal:*
   
    pip install notebook
    pip install jupyter


  #### Visual Studio Code
 ***Dit is al vooraf geïnstalleerd op de virtual machine. Ga naar de extensions, zoek naar "Python" en klik op "Install" om  toe te voegen.***

#### Python IDLE installatie
  
   *Typ in de terminal:*
       
    sudo apt-get install idle3
 

 ### Task troubleshooting
 #### Jupyter Notebook troubleshooting
 *Als er problemen optreden bij het uitvoeren van programma's na installatie, probeer dan de volgende commando's:*
 
     pip install -U Jinja2
     pip install markupsafe==2.0.1

### Task verification
  #### Python verificatie en PIP
  ##### Versie controle
  
    python3 --version
   [python version check](https://github.com/12002507/Devasc_Skills_LV/blob/master/Lab%201%20-%20Python%20Experiments/python%20version%20check.png)
  ##### Versiecontrole pip:
    pip --version
  [pip version check](https://github.com/12002507/Devasc_Skills_LV/blob/master/Lab%201%20-%20Python%20Experiments/pip%20version%20check.png)

  #### Jupyter verificatie
  *Voer het commando "jupyter notebook" uit in de terminal.*
 [jupyter version](https://github.com/12002507/Devasc_Skills_LV/blob/master/Lab%201%20-%20Python%20Experiments/juniper%20verificatie.png)

  #### IDLE verificatie
  *Typ "idle" in de terminal.*

  #### Visual Studio Code
  *Open Visual Studio Code*

  ## 1.2 Uitvoeren van geopy en timedate Python-scripts op DEVASC-LABVM met behulp van de tools (1.1):
  
    -timedate.py
    -geopy-geocoders_location.py
    -location.py
  

 ### Task preparation and implementation
  *Voer de volgende commando's uit in de terminal*
  
    pip install datetime
    pip install geopy
    pip install folium

 ### Task troubleshooting
 

  ### Task verification
  #### timedate.py
  *Voer het volgende commando uit in de terminal:*
  
    python3 ./labs/devnet-src/python/import-datetime.py

  #### Visual Studio Code
  *Plak de code in Visual Studio Code en druk op de afspeelknop om uit te voeren.*

  #### Jupyter Notebook
  *Voer het commando "jupyter notebook" uit in de terminal, ga naar het juiste pad op de website, kopieer de code en voer deze uit.*

  ## 1.3 Installatie van tools/packages op Windows OS (verdiepingsopdracht)
  ### Python 3.8 en PIP installatie
  
    Download Python 3.8 van de officiële website 
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py

 ### Visual Studio Code
  * Download Visual Studio Code van de officiële website en volg de installatie-instructies.*

  ### Jupyter Notebook
  *Open de opdrachtprompt en voer de volgende commando's uit:*
  
    python -m pip install --upgrade pip
    python -m pip install jupyter

  ### Python IDLE
  *Python IDLE wordt standaard geïnstalleerd met Python.*

  ### Task troubleshooting
  #### Jupyter Notebook
  *Als je een foutmelding krijgt zoals "python setup.py egg_info did not run successfully", probeer dan de volgende commando's:*
  
    pip uninstall jupyter
    pip install jupyter

  ### Task verification
  #### Visual Studio Code
  *Zoek naar Visual Studio Code in het startmenu en voer het uit.*

  #### Python en IDLE
  *Open de opdrachtprompt en typ "python" om Python te starten. Typ "python -m idlelib.idle" om IDLE te starten.*

  #### PIP
  *Open de opdrachtprompt en typ "pip help" om PIP te verifiëren.*

  #### Jupyter Notebook
  *Voer het commando "jupyter notebook" uit in de opdrachtprompt om Jupyter Notebook te starten.*
 

  ## 1.4 Installatie van tools/packages op Ubuntu 22.04.01 LTS (verdiepingsopdracht)
  ### Task preparation and implementation
  #### Python en PIP installatie
  *Voer de volgende commando's uit in de terminal:*
  
    sudo apt-get update
    sudo apt-get upgrade
    sudo apt install python3-pip

  #### Jupyter Notebook installatie
  *Voer de volgende commando's uit in de terminal:*
    
    pip install notebook
    pip install jupyter

  ### Visual Studio Code
  *werkt niet in de server cli versie van Ubuntu.*

  ### Python IDLE installatie
  *werkt niet in de server cli versie van ubuntu.*

  ### Task troubleshooting
  #### Jupyter Notebook troubleshooting
  *Als Jupyter Notebook niet werkt met het "jupyter notebook" commando, probeer het volgende commando:*
  
     sudo -H pip install jupyter</code>

 #### Python IDLE
  *Als je een "No display name and no display environment variable" foutmelding krijgt, kun je Python IDLE niet gebruiken op een serverversie van Ubuntu.*

  ### Task verification
  #### Python verificatie en PIP
  *Om de versie van Python te controleren, typ in de terminal:*
  
    python3 --version
  *Om de versie van PIP te controleren, typ:*
 
    pip --version

  #### Jupyter Notebook verificatie
  *Typ het volgende commando in de terminal:*

    python3 -m jupyter notebook

  #### Python IDLE verificatie
  * Typ "idle" in de terminal.*

  #### Visual Studio Code
  * Visual Studio Code kan niet worden geïnstalleerd op de serverversie van Ubuntu.*

## Python Programming Review 
### Task preparation and implementation:

  #### Python3 installeren: 
  
    sudo apt install python3-pip


### Task troubleshooting:

* Zorg ervoor dat pip eerst is geïnstalleerd op de virtual machine.*


### Task verification:

 #### Python-versie controleren:
  
    python3 -V
   #### Script uitvoeren: 
    python3 script.py


## Explore Python Development Tools 
### Task preparation and implementation:

   #### Virtuele omgeving aanmaken:
 
    cd labs/devnet-src/python/</
    python3 -m venv naam
    
   ####Pakket installeren:
   
    pip3 install naam
   #### Virtuele omgeving activeren: 
   
    source devfun/bin/activate


### Task troubleshooting:

  *Geen specifieke problemen gemeld.*


### Task verification:

   #### Controleren op geïnstalleerde pakketten in de virtuele omgeving: 
    pip3 freeze
   ####  Controleren op geïnstalleerde pakketten in het hele systeem: 
     python3 -m pip freeze
     
# LAB 2 – EXPLORE REST APIs WITH API SIMULATOR AND POSTMAN 
## Explore API Documentation Using the API Simulator 
### Task preparation and implementation:
    website library.demo.local bezoeken
   ##### Get/books
     Lijst boeken op met de get API
     cli : curl -X GET "http://library.demo.local/api/v1/books" -H
          "accept: application/json"
     Gui : Klik op try it out en vervolgens execute
     
  ##### Token via Post /loginViaBasic API
    Inloggen via deze api, vervolgens krijg je een token.
    bv. "token": "cisco|KZZzteQbC5iV3HKEzB7hCJ6qHQXen4rLGh72YJKeVfs"
  ##### Boek toevoegen via Post /book API  
    Cli:curl -X POST "http://library.demo.local/api/v1/books" -H "accept: application/json" -H "X-API-KEY: cisco|Ujk15vEJPGys6ZxkKpDCCnMaKH5L5miN5h1Sh1Qq2B8" -H "Content-Type: application/json" -d "{ \"id\": 3,   \"title\": \"31 Days Before Your CCNA Exam\", \"author\": \"Allan Johnson\"}"
    Gui: Op de API klikken, try it out en vervolgens de variabelen veranderen
  ##### Boeken lijsten via Get/books API
    Gui: Op API drukken, try it out en execute.
  ##### Specifieke boeken lijsten via Get/books{Id} API
    Cli: curl -X GET "http://library.demo.local/api/v1/books/4" -H "accept: application/json"
    Gui: Op de API klikken, try it out, vul het id van het boek en en execute
  ##### Specifieke boeken verwijderen via DELETE/books{Id} API  
     Cli: curl -X DELETE "http://library.demo.local/api/v1/books/5" -H "accept: application/json" -H "X-API-KEY: cisco|Ujk15vEJPGys6ZxkKpDCCnMaKH5L5miN5h1Sh1Qq2B8"
     Gui: Op de API klikken, try it out, vul het id van het boek en en execute
     
### Task troubleshooting:
    401 Server response : Spaties weghalen bij api variabelen wanneer je de naam veranderd van een boek
### Task verification
##### Voorbeeld get/books
[getbooks]()
## Use Postman to Make API Calls to the API Simulator 
### Task preparation and implementation:
 ##### Boeken lijsten via Get/books API
    Maak een nieuwe request, vink GET aan, vul de URL in en druk op send
 ##### Token via Post /loginViaBasic API
    Selecteer POST , vul de URL in, Authorize met de credentials en druk op send
 ##### Boek toevoegen via Post /book API     
    1.Selecteer POST , vul de URL in, Authorize met type API key,vol X-API-KEY in en plak de token.
    2.Bij authroization klik je op body, raw en vervolgens tekst in JSON
    3.Vul het object in
    {
    "id": 4,
    "title": "IPv6 Fundamentals",
    "author": "Rick Graziani",
    "isbn": "978 158144778"
    }
    4.Druk op send
 
### Task troubleshooting:
    Postman verkeerde in een goede werking
### Task verification
    Ga naar de eerste GET tab, druk op send en vervolgens op body

## Use Python to Add 100 Books to the API Simulator
### Task preparation and implementation:
  ##### Het script bestaat uit 3 grote delen
    1. Faker module: deze verzint random namen
    2.Loop voor de faker module die ervoor zorgt dat deze 100x gebruikt wordt
    3.De requesten om de boeken te maken
   [100bookscript]()
### Task troubleshooting:
    Het script werkte naar behoren
### Task verification
[Lab 2 script](https://github.com/12002507/Devasc_Skills_LV/blob/master/Lab%201%20-%20Python%20Experiments/juniper%20verificatie.png)
# LAB 3 – PYTHON REVIEW – DEVELOPMENT TOOLS AND CLASSES 

## Explore Python Classes 
### Task preparation and implementation:
*Een functie is een blok code dat is gedefinieerd met een naam.*

    Bv def functionName:
    ...blocks of code...
   #### Call the function
    functionName()
    </pre>
    <p>Een methode kan niet rechtstreeks worden aangeroepen, maar is afhankelijk van een object.</p>
    <pre><code>
    Define the class
    class className
#### Define a method
    def method1Name
    ...blocks of code
    # Define another methode

#### Define yet another method
    def method3Name
    ...blocks of code
#### Instantiate the class
    myClass = className()
#### Call the instantiation and associated methods
    myClass.method1Name()
    myClass.method2Name()
    myClass.method3Name()

#### Functie definiëren (mycity met argument city voorbeeld).

    myCity("Austin")
    myCity("Tokyo")
    myCity("Salzburg")
    devasc@labvm:~/labs/devnet-src/python$ python3 myCity.py
    I live in Austin.
    I live in Tokyo.
    I live in Salzburg.
#### Class definiëren moet met de _init_() methode.

    1. def __init__(self, name, country):
    self.name = name
    self.country = country
    2. def myLocation(self):
    print("Hi, my name is " + self.name + " and I live in " +
    self.country + ".")
    3. loc2 = Location("Ying", "China")
    loc3 = Location("Amare", "Kenya")
    loc2.myLocation()
    loc3.myLocation()
    your_loc = Location("Your_Name", "Your_Country")
    your_loc.myLocation()

#### Task troubleshooting:
#### Task verification

    Hi, my name is Tomas and I live in Portugal.
    Hi, my name is Ying and I live in China.
    Hi, my name is Amare and I live in Kenya.
    Hi, my name is Your_Name and I live in Your_Country.
    devasc@labvm:~/labs/devnet-src/python$

 ## LAB 4 - NETWORK INFRASTRUCTURE AND TROUBLESHOOTING

  #### Task preparation and implementation
  
     -Line console en vty instellen
     -Vlans instellen
     -ip’s op poorten zetten
     -ssh versie 2 aanzetten
     -duplex en speed op poorten instellen
     - domain ingesteld
   [Netwerk tekening](https://github.com/12002507/Devasc_Skills_LV/blob/master/Lab%204%20-%20Network%20infrastructure%20and%20troubleshooting/cisco.drawio.png)
   [Ip plan](https://github.com/12002507/Devasc_Skills_LV/blob/master/Lab%204%20-%20Network%20infrastructure%20and%20troubleshooting/Ip%20plan.png)
 
  #### Proactively determine what is needed to ensure the continuity of the system and network infrastructure:
  
     -DHCP moet werken voor de users
     -Vlan moet ingesteld worden ter verdeling van het netwerk
     -HSRP voor redundantie en schaalbaarheid
  
  #### Apply best practices to configuration and network security:
  
     -wachtwoorden gezet op line console 0, line vty
     -wachtwoord encryptie
     -maximale log-out timer
     -wachtwoord minimale grootte
     -ongebruikte poorten dichtgezet
     -ssh version 2 rsa key 1024
  

  #### Make sure you can backup and restore device configuration from a backup environment:
  
   

    -Zorgen dat tftp langs de subinterface 10 gaat.
    -basis configuratie doen
    -default gateway toevoegen en poorten openzetten.
 

  #### Router:
  
    router
    en
    conf t
    interface GigabitEthernet0/1
    ip address 10.199.66.108 255.255.255.224
    duplex auto
    speed auto
    no shutdown
    ip route 0.0.0.0 0.0.0.0 10.199.66.100
    copy tftp running-config
    10.188.64.134
    lab-ra08-c-r03-confg
    interface GigabitEthernet0/0.10
    encapsulation dot1Q 10
    no shutdown
 

  #### Switch:
  
    switch
    en
    conf t
    vlan 10
    exit
    interface vlan 10
    ip address 172.16.8.7 255.255.255.240
    no shutdown
    exit
    ip default-gateway 172.16.8.1
    interface g0/1
    switchport mode trunk
    switchport trunk allowed vlan 10
    switchport trunk native vlan 99
    no shutdown
    exit
  

  ### Task Troubleshooting
  #### Document your findings and important commands.
  
    - TFTP veranderen van poort
    -ip tftp source-interface GigabitEthernet 0/0.10
    -SSH version 2 gebruiken
    -Basis configuratie heropzetten router
    -Vergeet default gateway niet in te stellen op de router bij TFTP van de config naar het apparaat.
  

  ### Task verification:
  
    -Connective test
    -SSH naar verschillende apparaten
    -TFTP wipe test op tijd
   [config router](https://github.com/12002507/Devasc_Skills_LV/blob/master/Lab%204%20-%20Network%20infrastructure%20and%20troubleshooting/lab-RA08-R03)
   [config switch](https://github.com/12002507/Devasc_Skills_LV/blob/master/Lab%204%20-%20Network%20infrastructure%20and%20troubleshooting/lab-RA08-SW01)
 
 # LAB 5: Software Development and Design Content
 ### Part 1 Software Version Control with Git  
 ### Task preparation and implementation:
#### Git repository configureren

    - git config --global user.name "leandro.vankrunkelsven"
    - git config --global user.email leandro.vankrunkelsven@student.pxl.be
    - Git config –list (bovenste controleren)
    -mkdir git-folder (directory kiezen)
    -git init(directory initialiseren)
    -bestand naar keuze toevoegen
    -git add bestand.txt(bestand klaarmaken)
    -git commit -m “tekst op github die verteld over het bestand”

#### Bestand wijzigen op GIT

       -bestand wijzigen
       -git add bestand.txt
       -git commit -m “Toevoegingen gedaan, bugfixes”
       -git log (verschillende versies bekijken)
       -git diff  3453 34534(verschillen tussen de 2 bekijken)

#### Bestand en verschillende branches
    -git branch branchnaam
    -git branch (bekijken van branch)
    -git checkout branchnaam (Naar de branch gaan)
    -git add bestandsnaam.txt()in de branch steken)

#### Bestanden branches bij elkaar toevoegen
    -Git merge branchnaam
    -branch verwijderen
    -git branch
    -git branch -d feature
    -git branch

#### Merge conflicten
    -sed -i 's/Cisco/NetAcad/' DEVASC.txt (Woord cisco naar netacad veranderen in een bestand)
    -git commit -a -m "bug fixes" (stage en committen tegelijk)
    -git merge branchnaam (bij elkaar mergen)
    -git log (commits bekijken en conflicten vinden)

#### Integratie github
    -new repostory
    -naam repository
    -link kopieren
    -op vm een directory aanmaken voor de repository 
    -bestanden kopieren
    -git init (initialiseren)
    -git remote set-url origin https://github.com/12002507/devasc-study-team.git (origin erop zetten van rep)
    -git commit doen op de file


#### Task troubleshooting:
*Link gegeven in Devnet cursus voor remote werkte niet bij mij
juiste link: git remote set-url origin https://github.com/12002507/devasc-study-team.git*
#### Task verification:
#### File push to github
    -token creeren  https://github.com/settings/tokens
    -git push origin branchnaam

## Part 2: Create a Python Unit Test 3.5.7 
################################################################
#
## Part 3: Parse Different Data Types with Python Cisco
### Task preparation and implementation:
#### XML in python parsing
    import xml.etree.ElementTree as ET
    import re
    xml = ET.parse("myfile.xml")
    root = xml.getroot()
    ns = re.match('{.*}', root.tag).group(0)
    editconf = root.find("{}edit-config".format(ns))
    defop = editconf.find("{}default-operation".format(ns))
    testop = editconf.find("{}test-option".format(ns))
    print("The default-operation contains: {}".format(defop.text))
    print("The test-option contains: {}".format(testop.text))
#### JSON in python parsing
    import json
    import yaml
    with open('myfile.json','r') as json_file:
     ourjson = json.load(json_file)
     print(ourjson)
     print("The access token is: {}".format(ourjson['access_token']))
     print("The token expires in {} seconds.".format(ourjson['expires_in']))
    print("\n\n---")
    print(yaml.dump(ourjson))
#### YAML in python parsing
    import json
    import yaml
    with open('myfile.yaml','r') as yaml_file:
     ouryaml = yaml.safe_load(yaml_file)
     print(ouryaml)
    print("The access token is {}".format(ouryaml['access_token']))
    print("The token expires in {} seconds.".format(ouryaml['expires_in']))
    print("\n\n")
    print(json.dumps(ouryaml, indent=4))
### Task troubleshooting: /

#### Task verification: 
Uitvoeren
[lab5script](https://github.com/12002507/Devasc_Skills_LV/blob/master/Lab%205%20-%20Software%20development%20and%20design%20content/lab5scripten.py)
## LAB 6 – Python Network automation with netmiko
### Task preparation and implementation:

##### python voorbeeld script, ieder script heeft deze belangrijke elementen
        
    from netmiko import ConnectHandler              *netmiko module importeren
   	from getpass import getpass

   	cisco1 = { 
	   "device_type": "cisco_ios",              *Variabelen waar informatie staat over connecties met de apparaten zoals login gegevens
    "host": "172.16.8.4",
    "username": "admin",
    "password": "Administrator123.",
    }
    
     command = "show ip int brief",                 *Het commando dat wordt doorgestuurd

     with ConnectHandler(**cisco1) as net_connect:
     output = net_connect.send_command(command)     *output versturen

    	print()                                     *informatie Printen op het scherm
    	print(output)
     
     print()
     ####
### Part 1: Connecting to a single iOS device
#### Sending single show command

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
     ####
#### sending multiple show commands

    from netmiko import ConnectHandler
    from getpass import getpass

    cisco1 = { 
    "device_type": "cisco_ios",
    "host": "172.16.8.4",
    "username": "admin",
    "password": "Administrator123.",
    }

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
   
   #### Send multiple configuration commands to a single device
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

### Part 2: Connecting to a multiple iOS devices
#### Send show commands to multiple devices
    from netmiko import ConnectHandler

     devices = [
    {
        "device_type": "cisco_ios",
        "host": "172.16.8.4",
        "username": "cisco",
        "password": "class",
        "secret": "cisco"
    },
    {
        "device_type": "cisco_ios",
        "host": "172.16.8.7",
        "username": "cisco",
        "password": "class",
        "secret": "cisco"
    }
    ]
    commands = ["banner motd 'Authorized acces only!'"]
    for device in devices:
    connection = ConnectHandler(**device)
    connection.enable()

    output = connection.send_config_set(commands)
    print(f"Commands uitgevoerd op: {device['host']}")
    print(output)


    connection.disconnect()
  #### Send configuration commands to multiple devices
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
    'interface gi0/0', 'descri WAN', 'exit'
    ]

    for device in devices:
    # Connect to the device
    connection = ConnectHandler(**device)

    # Send the configuration commands
    output = connection.send_config_set(config_commands)

    # Disconnect from the device
    connection.disconnect()
  #### Run show commands and save the output
    from netmiko import ConnectHandler

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

    show_commands = ['show version', 'show interfaces', 'show running-config']

    for device in devices:
    # Connect to the device
    net_connect = ConnectHandler(**device)

    output = ''
    for command in show_commands:
        output += '\nOutput from {} running command {}: \n'.format(device['host'], command)
        output += net_connect.send_command(command)
        output += '\n'

    # Disconnect from the device
    net_connect.disconnect()

    filename = 'output_{}.txt'.format(device['host'])
    with open(filename, 'w') as file:
        file.write(output)
        print('Output saved to file {}.'.format(filename))
#### Backup the device configurations

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

    for device in devices:
    connection = ConnectHandler(**device)

    output = connection.send_command('show running-config')

    filename = f"{device['host']}_config.txt"
    with open(filename, 'w') as file:
        file.write(output)

    connection.disconnect()
	
#### Configure a subset of Interfaces

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

    interfaces = ['GigabitEthernet0/0', 'GigabitEthernet0/1']

    config_commands = [
    'interface ' + intf for intf in interfaces,
    'ip address 172.168.8.4 255.255.255.0',
    'no shutdown'
    ]

    for device in devices:
    # Connect to the device
    connection = ConnectHandler(**device)

    # Send the configuration commands for the subset of interfaces
    output = connection.send_config_set(config_commands)

    # Print the output to the console
    print(output)

    # Disconnect from the device
    connection.disconnect()
    
 #### send device configuration using external file
 
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

    config_file = '172.16.8.0.txt'

    for device in devices:
    # Connect to the device
    connection = ConnectHandler(**device)

    # Send the configuration commands from the file
    output = connection.send_config_from_file(config_file)

    # Print the output to the console
    print(output)

    # Disconnect from the device
    connection.disconnect()
    
   #### Connect using a Python Dictionary
        
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
    
#### Execute a script with a Function or classes

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
#### Execute a script with a statements (if, ifelse, else)

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
### Task verification:
    -Apparaten getest via visual studio code
  [Netmiko scripts](https://github.com/12002507/Devasc_Skills_LV/blob/master/Lab%206%20-%20Python%20network%20automation%20with%20netmiko/Netmiko%20lab%206%20scripten.py)
### Task troubleshooting:
    -Zorgen dat de username en password volledig correct is geschreven
    -Let op dat niet ieder commando gaat op switch op router bijvoorbeeld vlan's aanmaken.

#LAB 7 – YANG, NETCONFIG and RESTCONFIG 
## Part 1: Install the CSR1000v VM
### Task preparation and implementation:
    -Vm downloaden
    -Vm opstarten
    -Vm terug afluisten en vervolgens iso in disk drive 1 steken
    -show ip int brief
   [CSR1000 installatie](https://github.com/12002507/Devasc_Skills_LV/blob/master/Lab%207%20-%20NETCONFIG%20and%20YANG/vmware%20installatie.png)
   [csr1000 succesvol gui na installatie](https://github.com/12002507/Devasc_Skills_LV/blob/master/Lab%207%20-%20NETCONFIG%20and%20YANG/cisco%20gui.png)
   
### Task verification:
    -Vm pingen van devasc in terminal
    -Op ip van de switch de webgui openen

### Task troubleshooting:
    -cisco VM werkt niet goed in virtual box, vmware gebruiken
    -Grub Loading stage 2 : cisco booten via vga optie, andere werkt niet
## Part 2: Explore YANG Models
### Task preparation and implementation:
     Cd devnet-src/
     Mkdir pyang
    wget https://raw.githubusercontent.com/YangModels/yang/main/vendor/cisco/xe/1693/ietf-interfaces.yang
[wget](https://github.com/12002507/Devasc_Skills_LV/blob/master/Lab%207%20-%20NETCONFIG%20and%20YANG/wget.png)
### Task verification:
    Pyang -v : versie controle
### Task troubleshooting:
    Link github werkte niet, werkende link : https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1693/ietf-interfaces.yang
## Part 3: Use NETCONF to Access an IOS XE Device
### Task preparation and implementation:
    ssh connectie: ssh cisco@192.168.206.128
    Netconf via ssh:  ssh cisco@192.168.206.128 -p 830 -s Netconf
    script uitvoeren: python3 ncclient-netconf.py
Script nccclient:
       
    from ncclient import manager
    import xml.dom.minidom

    #connectie naar de VM
    m = manager.connect(
    host="192.168.206.128",
     port=830,
     username="cisco",
     password="cisco123!",
       hostkey_verify=False
       )


    print("#Supported Capabilities (YANG models):")
    for capability in m.server_capabilities:
     print(capability)
     .............


[script](https://github.com/12002507/Devasc_Skills_LV/blob/master/Lab%207%20-%20NETCONFIG%20and%20YANG/sciptncc7.py)

### Task verification:
    Ping -c 5 192.168.206.128
    show platform software yang-management process
    show Netconf-yang sessions
    pip3 list --format=columns | more
[running](https://github.com/12002507/Devasc_Skills_LV/blob/master/Lab%207%20-%20NETCONFIG%20and%20YANG/running%20processes.png)
### Task troubleshooting:
    ]]>]]> : deze niet toevoegen bij commando’s, komen van de router

## Part 4: Use RESTCONF to Access an IOS XE Device
### Task preparation and implementation:
   Restcof aanzetten:
   
    configure terminal
    restconf
   https aanzetten: 
   
    ip http secure-server
    ip http authentication local


Task troubleshooting:

Task verification:

    ssh cisco@192.168.56.101
    ping -c 5 192.168.56.101
    show platform software yang-management process
   [script](https://github.com/12002507/Devasc_Skills_LV/blob/master/Lab%207%20-%20NETCONFIG%20and%20YANG/postmanscript.py)


