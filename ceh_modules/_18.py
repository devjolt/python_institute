from random import choice
from ceh.utilities import utilities as utl

from ._18_logic import *
"""
question_logic={
                'correct_incorrect':utl.make_items_question_from_correct_incorrect,
                'multi_from_correct':utl.multi_option_from_correct_incorrect,
                'old_pairs':utl.make_items_question_from_pairs,
                'posneg_pairs':utl.posneg_pairs,
                'new_pairs':utl.new_pairs,
                'multi_option_pairs':utl.multi_option_pairs,
                'order_from_pairs':utl.order_from_pairs
            }


'definition of attack': {
'question_with_0':'which of the following POSNEG PLACEHOLDER?',
'positive_negative':('are','could not be described as'),
'type':['posneg_pairs', 'multi_option_pairs'],
'course_code':'1',
'pairs':(
    ('elements of an attack', ['motive','goal','method','vulnerability']),
    ('something other than the elements of an attack', ['risk','threat','identification','disruption','backdoor']),
),
'fillers': ([])  
},

'formula of attack': {
'question':'Which of the following PLACEHOLDERcorrectly describes the formula of an attack?',
'type':'correct_incorrect',
'positive':'',
'negative':'in',
'course_code':'',
'correct':(
    'attacks = motive + method + vulnerability',
    'attacks = goal + method + vulnerability',
    'attacks=goal+method+vulnerability',
),
'incorrect': (
    f"attacks = goal + method + {choice(words)}",
    f"attacks = goal + {choice(words)} + vulnerability",
    f"attacks = {choice(words)} + method + vulnerability",
),
},

resource = {
        'question_with_0':'Which isPOSNEG an example of PLACEHOLDER?',
        'positive_negative':('',' not'),
        'type':['multi_pairs'],
        'course_code':'',
        'pairs':[
            ('correct',['A','B','C','D']),
            ('incorrect',['1', '2', '3','4']),
            ('ambiguous',['0', '9', '8','7']),
            
        ],
        'fillers': (
            ('backwards',['z', 'y', 'x','w']),
        )
    }

"""


questions = {

    'IoT Architecture':{
        'question_with_0':'Which describes the PLACEHOLDER?',
        'question_with_1':'What best describes the following: PLACEHOLDER?',
        'type':['new_pairs'],
        'course_code':'',
        'pairs':[
            ('edge technology layer',['hardware components of an IoT device','deployed in the field','plays an important part in data collection',f"plays an important part in connecting devices {choice(['within the network','with the server'])}"]),
            ('access gateway layer',['helps to bridge the gap between two endpoints', 'initial data handling takes place here', f"carries out {choice(['message routing', 'message identification', 'subscribing'])}"]),
            ('internet layer',['main component in carrying out communication between two endpoints', f"carries out {choice(['device to device','device to cloud','device to gateway', 'back end'])} data sharing"]),
            ('middleware layer', ['operates in a two way mode', f"responsible for {choice(['data management', 'device management', 'data analysis', 'data aggregation', 'data filtering', 'device information discovery','access control'])}"]),
            ('application layer',['the top of the IoT stack', 'responsible for delivery of services to users']),
        ],
        'fillers': (
            ()
        )
    },
    'IoT Components': {
        'question_with_0':'Which of the following isPOSNEG PLACEHOLDER?',
        'positive_negative':('',' not'),
        'type':['posneg_pairs', 'multi_option_pairs'],
        'course_code':'1',
        'pairs':(
            ('a component of IoT technology which plays an essential role in the function of an IoT device', ['sensing technology','IoT gateway','cloud server','data storage', 'remote control using a mobile app', 'remote control']),
            ('the name of a layer in IoT Architecture', ['edge technology','access gateway','internet','middleware','application']),
        ),
        'fillers': ([])  
    },
    'Short-Range Wireless Communcation': {
        'question_with_0':'Which describes PLACEHOLDER?',
        'question_with_1':'What best describes the following: PLACEHOLDER?',
        'type':['new_pairs'],
        'course_code':'1',
        'pairs':(
            (['Bluetooth low energy', 'BLE'], ['wireless personal area network','wireless personal area network']),
            (['Light-Fidelity', 'Li-Fi'], ['visible light communication system', 'uses houshold light bulbs for data transfer', 'operates at 224 Gbps']),
            (['Near field communication', 'NFC'], ['uses magnetic field induction', 'short range communication']),
            (['QR codes'],'two dimensional machine readable tag which encodes information'),
            (['Bar codes'],'one dimensional machine readable tag which encodes information'),
            (['Radio-frequency identification', 'RFID'],'stores data in tags read using electromagnetic fields'),
            ('thread', ['IPv6 based networking protocol for IoT devices', 'enables communication on local wireless home networks']),
            ('Wi-Fi',['widely used in wireless (LAN)','the most common standard is 802.11n', 'maximum speed of 600 Mbps','range of approximately 50 m']),
            ('Wi-Fi direct', ['used for peer-to-peer communication without the need for a wireless access point','start communication only after deciding which device will act as an access point']),
            ('Z-wave', ['low-power, short-range communication designed primarily for home automation']),
            ('Zig-Bee',['based on the IEEE 203.15.4 standard','used in devices that transfer data infrequently at a low rate in a restricted area and within a range of 10-100m']),
            (['Adaptive network topology','Ant'], ['a multicast wireless sensor network technology','used mainly for short-range communication between devices related to sports and fitness sensors']),
        ),
        'fillers': ([])  
    },
    'Medium-Range Wireless Communcation': {
        'question_with_0':'Which describes PLACEHOLDER?',
        'question_with_1':'What best describes the following: PLACEHOLDER?',
        'type':['new_pairs'],
        'course_code':'1',
        'pairs':(
            ('HaLow', ['another variant of the Wi-Fi standard','provides an extended range, making it useful for communications in rural areas','offers low data rates, thus reducing the power and cost of transmission']),
            ('LTE-advanced', 'a standard for mobile communication that provides enhancement to LTE, focusing on providing higher capacity in terms of data rate, extended range, efficiency, and performance'),
            (['6LoWPAN','IPv6 over Low Power Wireless Personal Area Networks'],'an Internet protocol used for communication between smaller and low-power devices with limited processing capacity'),
            (['QUIC', 'Quick UDP Internet Connection'],[f"multiplexed connections between IoT devices over{choice(['the User Datagram Protocol','UDP'])}","provides security equivalent to SSL/TLS"]),
        ),
        'fillers': ([])  
    },
    'Long-Range Wireless Communcation': {
        'question_with_0':'Which describes PLACEHOLDER?',
        'question_with_1':'What best describes the following: PLACEHOLDER?',
        'type':['new_pairs'],
        'course_code':'1',
        'pairs':(
            (['LoRaWAN','Long Range Wide Area Network'], ['used to support applications such as mobile, industrial machine-to-machine, and secure two-way communications for IoT devices, smart cities, and healthcare applications']),
            ('Sigfox', 'used in devices that have short battery life and need to transfer a limited amount of data'),
            ('NEUL','used in a tiny part of the TV white space spectrum to deliver high-quality, high-power, high-coverage, and low-cost networks'),
            (['Very Small Aperture Terminal', 'VSAT'],['a communication protocol that is used for data transfer using small dish antennas for both broadband and narrowband data']),
            ('Cellular', [' a type of communication protocol that is used for communication over a longer distance','It is used to send high-quality data but with the drawbacks of being expensive and having high power consumption']),
            (['MQTT', 'Message Queuing Telemetry Transport'], ['an ISO standard lightweight protocol used to transmit messages for long-range wireless communication','helps in establishing connections to remote locations, for example via satellite links']),
            (['Narrowband IoT', 'NB-IoT'],['a variant of LoRaWAN and Sigfox that uses more enhanced physical layer technology and the spectrum used for machine-to-machine communication'])
        ),
        'fillers': ([])  
    },
    'Wired Communcation': {
        'question_with_0':'Which describes PLACEHOLDER?',
        'question_with_1':'What best describes the following: PLACEHOLDER?',
        'type':['new_pairs'],
        'course_code':'1',
        'pairs':(
            ('Ethernet', ['the most commonly used type of network protocol today','a type of LAN (Local Area Network) that consists of a wired connection between computers in a small building, office, or campus']),
            (['Multimedia over Coax Alliance', 'MoCA'],'a type of network protocol that provides high-definition videos and related content to homes over existing coaxial cables'),
            (['Power-Line Communication', 'PLC'],['a type of protocol that uses electrical wires to transmit power and data from one endpoint to another','required for applications in different areas such as home automation, industrial devices, and broadband over power lines (BPL)'])
        ),
        'fillers': ([])  
    },
            
    'IoT methods of communication': {
        'question_with_0':'Which of the following isPOSNEG an example of PLACEHOLDER?',
        'positive_negative':('',' not'),
        'type':['posneg_pairs', 'multi_option_pairs'],
        'course_code':'1',
        'pairs':(
            ('wired Communcation', ['Ethernet','Multimedia ocer Coax Alliance','MoCA','Power-Line Communication', 'PLC']),
            ('long-range wireless communcation', ['Narrowband IoT', 'NB-IoT','MQTT', 'Message Queuing Telemetry Transport','Cellular','Very Small Aperture Terminal', 'VSAT','NEUL','Sigfox','LoRaWAN','Long Range Wide Area Network']),
            ('Medium-Range Wireless Communcation', ['HaLow','LTE-advanced', '6LoWPAN','IPv6 over Low Power Wireless Personal Area Networks','QUIC', 'Quick UDP Internet Connection']),
            ('Short-Range Wireless Communcation',['Bluetooth low energy', 'BLE','Light-Fidelity', 'Li-Fi','Near field communication', 'NFC','QR codes','Bar codes','Radio-frequency identification', 'RFID','thread','Wi-Fi','Wi-Fi direct','Z-wave','Zig-Bee','Adaptive network topology','Ant']),
        ),
        'fillers': ([]) 
    },
    'IoT Operating Systems': {
        'question_with_0':'Which describes PLACEHOLDER?',
        'question_with_1':'What best describes the following: PLACEHOLDER?',
        'type':['new_pairs'],
        'course_code':'1',
        'pairs':(
            ('Windows 10 IoT', 'a family of operating systems developed by Microsoft for embedded systems'),
            ('Amazon Free RTOS', 'a free open-source OS used in IoT microcontrollers that makes low-power, battery-operated edge devices easy to deploy, secure, connect, and manage'),
            ('Contiki','used in low-power wireless devices such as street lighting and sound monitoring systems'),
            ('Fuchsia','open-source OS developed by Google for various platforms, such as embedded systems, smartphones, tablets'),
            ('RIOT', 'fewer resource requirements and uses energy efficiently. It has the ability to run on embedded systems, actuator boards and sensors'),
            ('Ubuntu Core', 'Also known as Snappy, this is used in robots, drones, edge gateways, etc'),
            ('ARM mbed OS',' mostly used for low-powered devices such as wearable devices'),
            ('Zephyr', 'used in low powered and resource-constrained devices'),
            ('Nucleus RTOS','Primarily used in aerospace, medical, and industrial applications'),
            ('NuttX RTOS','an open-source OS primarily developed to support 8-bit and 32-bit microcontrollers of embedded systems'),
            ('Integrity RTOS','Primarily used in the aerospace or defense, industrial, automotive, and medical sectors'),
            ('Brillo', 'Android-based embedded OS used in low-end devices such as thermostats'),
            ('Apache Mynewt', 'supports devices that work on the BLE protocol')
        ),
        'fillers': ([])  
    },
    'IoT Application Protocols': {
        'question_with_0':'Which describes PLACEHOLDER?',
        'question_with_1':'What best describes the following: PLACEHOLDER?',
        'type':['new_pairs'],
        'course_code':'1',
        'pairs':(
            (['CoAP', 'Constrained Application Protocol'], ['a family of operating systems developed by Microsoft for embedded systems', 'a web transfer protocol used to transfer messages between constrained nodes and IoT networks','mainly used for machine-to-machine (M2M) applications such as building automation and smart energy']),
            ('Edge',['helps the IoT environment to move computational processing to the edge of the network','allows smart devices and gateways to perform tasks and services from the cloud end','improves content caching, delivery, storage, and management of the IoT']),
            (['LWM2M','Lightweight Machine-to-Machine'],['used for application-level communication between IoT devices','used for IoT device management']),
            ('Physical Web',['used to enable faster and seamless interaction with nearby IoT devices','reveals the list of URLs being broadcast by nearby devices with BLE beacons']),
            (['XMPP','eXtensible Messaging and Presence Protocol'],['open technology for real-time communication used for IoT devices','used for developing interoperable devices, applications, and services for the IoT environment']),
            (['Mihini','M3DA'],['software used for communication between an M2M server and applications running on an embedded gateway','allows IoT applications to exchange data and commands with an M2M server']),         
        ),
        'fillers': ([])  
    },            
    
    'IoT Application Protocols': {
        'question_with_0':'Which describes PLACEHOLDER?',
        'question_with_1':'What best describes the following: PLACEHOLDER?',
        'type':['new_pairs'],
        'course_code':'1',
        'pairs':(
            ('Device-to-Device Communication Model',['inter-connected devices interact with each other through the Internet, but they predominantly use protocols such as ZigBee, Z-Wave or Bluetooth','commonly used in smart home devices such as thermostats, light bulbs, door locks, CCTV cameras, and fridges, which transfer small data packets to each other at a low data rate','popular in communication between wearable devices','an ECG/EKG device attached to the body of a patient will be paired to their smartphone and will send them notifications during an emergency']),
            ('Device-to-Cloud Communication Model',['uses communication protocols such as Wi-Fi or Ethernet','sometimes uses Cellular','a CCTV camera that can be accessed on a smartphone from a remote location','a CCTV camera cannot directly communicate with the client']),
            ('Device-to-Gateway Communication Model',['the IoT device communicates with an intermediate device called a gateway which in turn communicates with the cloud service','could use a smartphone or a hub as a gateway which acts an intermediate point, and provides security features and data or protocol translation','generally uses ZigBee and Z-Wave','could be an app that interacts with the IoT device and with the cloud','this device might be a smart TV that connects to the cloud through a mobile phone app']),
            ('Back-End Data-Sharing Communication Model',['extends the device-to-cloud communication type such that the data from the IoT devices can be accessed by authorized third parties','devices upload their data onto the cloud, which is later accessed or analyzed by third parties','an analyzer of the yearly or monthly energy consumption of a company']),
        ),
        'fillers': ([])  
    },            
}

"""
OWASP Top 10 IoT Threats Source: https://www.owasp.org
The Top 10 IoT threats, according to the Open Web Application Security Project (OWASP), are listed below:  Weak, Guessable, or Hardcoded Passwords Using weak, guessable, or hardcoded passwords allows publicly available or unchangeable credentials to be determined via brute forcing. This also includes backdoors in the firmware or client software that lead to unauthorized access to the deployed devices.
 Insecure Network Services
Insecure network services are prone to various attacks like buffer overflow attacks, which cause a denial-of-service scenario, thus leaving the device inaccessible to the user. An attacker uses various automated tools such as port scanners and fuzzers to detect the open ports and exploit them to gain unauthorized access to services.
These insecure network services that are open to the Internet may compromise the confidentiality, authenticity, integrity, or availability of information and also allow remote access to critical information.
Insecure Ecosystem Interfaces
Insecure ecosystem interfaces such as web, backend API, mobile, and cloud interfaces outside the device lead to compromised security of the device and its components. Common vulnerabilities in such interfaces include lack of authentication/authorization, lack of encryption or weak encryption, and lack of input/output filtering.
 Lack of Secure Update Mechanisms
Lack of secure update mechanisms, such as a lack of firmware validation on the device, lack of secure delivery, lack of anti-rollback mechanisms, or lack of notifications of security changes, may be exploited to perform various attacks.
 Use of Insecure or Outdated Components
Use of outdated or older versions of software components or libraries, such as insecure customization of OS platforms or use of third-party hardware or software components from a compromised supply chain, may allow the devices themselves to be compromised.
 Insufficient Privacy Protection
Insufficient privacy protection allows the user’s personal information stored on the devices or ecosystem to be compromised.
 Insecure Data Transfer and Storage
Lack of encryption and access control of data that is in transit or at rest may result in leakage of sensitive information to malicious users.

Lack of Device Management
Lack of appropriate security support through device management on devices deployed in production, including asset management, update management, secure decommissioning, system monitoring, and response capabilities, may open the door to various attacks.
 Insecure Default Settings Insecure or insufficient device settings restrict the operators from modifying configurations to make the device more secure.
 Lack of Physical Hardening
Lack of physical hardening measures allows potential attackers to acquire sensitive information that helps them in performing a remote attack or obtaining local control of the device.
"""