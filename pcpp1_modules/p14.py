from random import randint

from .p14_logic import *

def ip_address(length = 4):
    return '.'.join([str(randint(0, 255)) for i in range(length)])

questions = {

    'Some words about REST APIs': {
        'question_with_0':'What does PLACEHOLDER mean?',
        'question_with_1':'',
        'type':'make_items_question_from_pairs',
        'course_code':'1.1.1.2',
        'pairs':(
            ('representational', 'data or states are retained inside the system and presented to the users'),
            ('state', "the values of an object's set of properties"),
            ('transfer', "transmission of a state's representation to and from the server"),
        ),
        'fillers': (
            ('transmission', 'sending data via web sockets'),
            ('text', 'the type of data used in REST'),
            ('server', 'the location where REST states are stored'),
        )
    },

    'REST APIs': {
        'question':'Which of the following statements is PLACEHOLDER?',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'correct',
        'negative':'incorrect',
        'course_code':'1.1.1.2',
        'correct':(
            'REST data is always text',
            'REST is focused on data which reflects states',
            'A change in state is often called a transition',
            "A transition can be caused by a change in any of an object's states",
            "A REST object never leaves its own server",
            'Representation reflects the way in which states are retained and presented to users',
            "Humans can access REST data",
            "Computers can access REST data",
            "REST data is accessible to many users at the same time",
        ),
        'incorrect': (
            'REST data is always stored in hashed numbers',
            'REST data is always stored in arrays',
            'A change in state is often called a transmission',
            "A transition can be caused by a change in any of an object's states",
            "A REST object only leaves the server during transition",
            "Only humans can access REST data",
            "Only computers can access REST data",
            'REST data is accessible to one user at a time'
        ),
    },


    
    'BSD sockets': {
        'question':'Which of the following statements is PLACEHOLDER?',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'correct',
        'negative':'incorrect',
        'course_code':'1.1.1.3',
        'correct':(
            'a socket is a kind of end-point',
            'an end point is where data is available and where it may be sent to',
            'Python can connect to sockets',
            'all modern OSs implement BSD sockets in a more or less accurate way',
            'BSD sockets were originally implemented in C',
            'writing to a socket results in sending the data through a network',
            'reading from a socket enables you to receive the data coming from the network',
        ),
        'incorrect': (
            'a transition is a kind of end-point',
            'sockets can only be used to transmit data',
            'sockets can only be used to recieve data',
            'BSD sockets were originally implemented in Python',
            'only C can connect to sockets',
            'only Python can connect to sockets',
            'reading from a socket results in sending the data through a network',
            'writing to a socket enables you to receive the data coming from the network',
            
        ),
    },

    'Berkeley Software Distribution sockets': {
        'question_with_0':'What is PLACEHOLDER?',
        'question_with_1':'1.1.1.3',
        'type':'make_items_question_from_pairs',
        'course_code':'',
        'pairs':(
            (('an end point', 'a socket'), 'a point where the data is available to get it from and where the data may be sent to'),
            ('transfer', "transmission of a state's representation to and from the server"),
            ('BSD sockets', 'a universal set of functions suitable for implementation in nearly all operating systems and available in all modern programming languages'),
            (('Berkeley Software Distribution','BSD'), 'the name of a Unix-class operating system, where the sockets were deployed for the very first time'),
            ('WinSock', 'the microsoft implementation of BDS sockets'),
        ),
        'fillers': (
            ('object', 'a collection of attributes and methods'),
            ('text', 'the type of data used in REST'),
            ('server', 'the location where REST states are stored'),
            ('Linux Mint', 'a modern implementation of Unix'),
        ),
    },

    'sockets domains addresses ports': {
        'question_with_0':'What is PLACEHOLDER?',
        'question_with_1':'',
        'type':'make_items_question_from_pairs',
        'course_code':'1.1.1.4',
        'pairs':(
            ('the Unix domain', 'the part of BSD sockets used to communicate programs working within one operating system'),
            (('the Internet domain', 'INET'), "part of BSD socket API used to communicate programs working within different computer systems, connected together using a TCP/IP network"),
            ('an IP4 address', ('the address of the computer where a socket is located','32-bit long value used to identify computers connected to any TCP/IP network', ip_address())),
            ('a port number', 'the identifier of the virtual socket interface'),
            ('socket address', ('the address of the computer where a socket is located and the port number', f'{ip_address()} 80')),
            ('socket/service number', 'a 16-bit long integer number identifying a socket within a particular system', f'{randint(1, 65536)}'), 
            ('protocol', ('a standardized set of rules allowing processes to communicate with each other','specification of the rules of behaviour for all participants')),

        ),
        'fillers': (
            ('transmission', 'sending data via web sockets'),
            ('text', 'the type of data used in REST'),
            ('server', 'the location where REST states are stored'),
        )
    },

    'Domains, addresses, ports, protocols': {
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'correct',
        'negative':'incorrect',
        'course_code':'1.1.1.4',
        'question':'Which of the following statements is PLACEHOLDER?',
        'correct':(
            'Unix domain is used for programs working within one operating system to communicate',
            'INET is used for programs working in different computer systems to communicate',
            'INET makes use of TCP/IP networks',
            'INET can be used for programs working within one operating system to communicate',
            'Unix domain is not used for programs working in different computer systems to communicate',
            f"{ip_address()} is an IP address",
            'there are 65,536 possible socket/service numbers', 
            'many standard network services usually use the same, constant socket numbers',
            'IPv4 addresses are 32 bits long',
            f'{ip_address()} 80 is a socket address', 
        ),
        'incorrect': (
            'INET can not be used for programs working within one operating system to communicate',
            'Unix domain is used for programs working in different computer systems to communicate',
            'Unix domain makes use of TCP/IP networks',
            f"{ip_address()} is not an IP address",
            f"{'.'.join([str(randint(0, 255)) for i in range(randint(2,3))])} is an IP address",
            f"{'.'.join([str(randint(0, 255)) for i in range(5)])} is an IP address",
            'there are 65,536 possible IP addresses', 
            f'IPv4 addresses are {randint(24,31)} bits long',
            f'IPv4 addresses are {randint(33,42)} bits long',
            f'{ip_address()} is a socket address', 
        ),
    },
    
    'Protocol stacks': {
        'type':'make_items_question_from_pairs',
        'course_code':'',
        'question_with_0':'What is PLACEHOLDER?',
        'question_with_1':'1.1.1.5',
        'pairs':(
            ('a protocol stack', 'a multilayer set of cooperating protocols providing a unified repertoire of services'),
            (('IP', 'internetwork protocol'), ("one of the lowest parts of TCP/IP protocol stack", 'able to send a packet of data between two network nodes', 'a very unreliable protocol')),
            ('the TCP/IP stack', 'designed to cooperate with networks based on the IP protocol'),
            ('a packet of data', 'a datagram'),
            (('TCP', 'transmission control protocol'), ('first-choice protocol for applications where data safety is more important','a reliable transmission protocol', 'the highest part of the TCP/IP stack', 'the protocol which uses handshakes to construct reliable communication channels', 'responsible for transmitting and recieving single characters')),
            (('UDP', 'user datagram protocol'), ('adequate for applications where response time is crucial', 'higher in the stack than IP', 'lower in the stack than TCP', 'less reliable than TCP', 'faster than TCP')),
        ),
        'fillers': (
            ('TIP', 'transition compliance protocol'),
            ('text', 'the type of data used in REST'),
            ('server', 'the location where REST states are stored'),
        )
    },
    'OS Protocol stack': {
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'correct',
        'negative':'incorrect',
        'course_code':'1.1.1.5',
        'question':'Which of the following statements is PLACEHOLDER?',
        'correct':(
            'the upper TCP/IP layers compensate for the unreliability of the lower layers',
            'IP is a very unreliable protocol',
            "IP doesn't guarantee that datagrams reach their destination",
            'Datagrams sent over IP may not arrive intact',
            'Datagrams sent over IP may not arrive in the order they are sent',
            'TCP uses datagrams and handshakes to construct reliable communication',
            'TCP is able to transmit and recieve single characters',
            'TCP guarantees that a stream of data reaches the target or that failure is reported',
            'TCP guarantees that a datagram reaches the target intact',
            'UDP is faster than TCP',
            'UDP has fewer overheads than TCP',
            'TCP uses handshakes'
        ),
        'incorrect': (
            "IP is one of the highest parts of the TCP/IP stack",
            'the lower TCP/IP layers compensate for the unreliability of the upper layers',
            'TCP is a very unreliable protocol',
            "TCP doesn't guarantee that datagrams reach their destination",
            'Datagrams sent over TCP may not arrive intact',
            'Datagrams sent over TCP may not arrive in the order they are sent',
            'UDP uses datagrams and handshakes to construct reliable communication',
            'IP uses datagrams and handshakes to construct reliable communication',
            'IP is able to transmit and recieve single characters',
            'IP guarantees that a stream of data reaches the target or that failure is reported',
            'UDP guarantees that a stream of data reaches the target or that failure is reported',
            'UDP guarantees that a data reaches the target intact',
            'IP guarantees that a data reaches the target intact',
            'TCP is faster than UDP',
            'TCP has fewer overheads than UDP',
            'IP uses handshakes',
            'UDP uses handshakes'
            
        ),
    },

    'Clients and servers - two sides of network communication': {
        'type':'make_items_question_from_pairs',
        'course_code':'',
        'question_with_0':'What is PLACEHOLDER?',
        'question_with_1':'1.1.1.6',
        'pairs':(
            ('connection-oriented communication', ('usually built on TCP', 'a communication process where both parties have different roles and routines',"a communication process where both parties aren't symmertrical",  'a communication process where both parties are aware that the other party is connected','communication which demands some preliminary steps to establish the connection and other steps to finish it')),
            ('connectionless communication', ('usually built on UDP', 'communication which can be established ad-hoc', 'communication where both parties have equal rights', 'communication where neither parties are aware of the other side\'s state')),
            ('a client', "the side that initiates a connection"),
            ('a server', 'the side that answers the client'),
        ),

        'fillers': (
            ('TIP', 'transition compliance protocol'),
            ('text', 'the type of data used in REST'),
            ('internet', 'the location where REST states are stored'),
        )
    },

    'Connection-oriented and connectionless network communication': {
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'correct',
        'negative':'incorrect',
        'course_code':'1.1.1.6',
        
        'question':'Which of the following statements is PLACEHOLDER?',
        'correct':(
            'Connection-oriented communications are usually built on top of TCP', 
            'Connectionless communications are usually built on top of UDP', 
            'Clients initiate a connection', 
            'Servers answer a request to connect', 
            'In connection-oriented communication, both arties have different roles and routines',
            "In connection-oriented communication, both parties aren't symmertrical",  
            'In connection-oriented communication, both parties are aware that the other party is connected',
            'Connection-oriented communication requires preliminary steps to establish the connection and other steps to finish it'
            'Connectionless communication can be established ad-hoc',
            'In connectionless communication, both parties have equal rights',
            'In connectionless communication, neither parties are aware of the other side\'s state'
        ),
        'incorrect':(
            'Connectionless communications are usually built on top of TCP', 
            'Connection-oriented communications are usually built on top of UDP', 
            'Servers initiate a connection', 
            'Clients answer a request to connect', 
            'In connectionless communication, both arties have different roles and routines',
            "In connectionless communication, both parties aren't symmertrical",  
            'In connectionless communication, both parties are aware that the other party is connected',
            'Connectionless communication requires preliminary steps to establish the connection and other steps to finish it'
            'connection-oriented communication can be established ad-hoc',
            'In connection-oriented communication, both parties have equal rights',
            'In connection-oriented communication, neither parties are aware of the other side\'s state'
        ),
    },

    'How to use sockets in Python': {
        'type':'make_items_question_from_pairs',
        'course_code':'1.2.1.1',
        'question_with_0':['Match the following code and commentary:','PLACEHOLDER'],
        'question_with_1':'',
        'pairs':(
            ('$import socket', 'access the python module to establish and work with sockets'),
            (('$sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)', '$sock = socket.socket()', '$sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)'), 'create a socket object'),
            (('$family = socket.AF_INET', '$socket.AF_INET'), "configure a socket to use TCP/IP domain"),
            (('$type = socket.SOCK_STREAM', '$socket.SOCK_STREAM'), ('specify a high-level socket able to act as a character device', 'transfer data byte by byte, not as fixed sized blocks')),
            (('$type = socket.SOCK_DGRAM', '$socket.SOCK_DGRAM'), 'specify a socket for use with UDP if used when creating a socket'),    
        ),
        'fillers': (
            ('$import time', 'message server'),
            ('$import sockets', 'recieve initial data protocol'),
            ('$import sockset', 'import message from server'),
        )
    },

    'Python sockets code': {
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'correct',
        'negative':'incorrect',
        'course_code':'1.2.1',
        
        'question':'Which of the following snippets is PLACEHOLDER?',
        'correct':(
            '$import socket', 
            '$sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)', 
            '$sock = socket.socket()', 
            '$sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)',
            '$family = socket.AF_INET', 
            '$socket.AF_INET',
            '$type = socket.SOCK_STREAM', 
            '$socket.SOCK_STREAM',
            '$type = socket.SOCK_DGRAM', 
            '$socket.SOCK_DGRAM',
        ),
        'incorrect':(
            '$import sock', '$from socket import sock',
            '$sock = socket.socket(socket.INET, socket.SOCK_STREAM)', 
            '$sock = socket.socket(socket.AF_INET, socket.STREAM)', 
            '$sock = socket(socket)', 
            '$sock = socket.socket(family=socket.SOCK_DGRAM, type=socket.AF_INET)',
            '$type = socket.AF_INET', 
            '$socket.AF_INTERNET',
            '$family = socket.SOCK_STREAM', 
            '$socket.SOCKSTREAM',
            '$family = socket.SOCK_DGRAM', 
            '$family = socket.SOCK_DDRAM',
            '$socket.SOCK_DATAGRAM',
        ),
    },


    'Creating sockets and connecting to sockets with python':{
        'type':'make_items_question_from_pairs',
        'course_code':'1.2.1.3',
        
        'question_with_0':['Match the following code and commentary:','PLACEHOLDER'],
        'question_with_1':'',
        'pairs':(
            (('''$import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)''',
            '''$import socket
sock = socket.socket()'''), 'create a socket object'),
            ((f'''$import socket
sever_addr = '{ip_address()}'
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server_addr, 80))'''), 'try to connect to a server'),
            (('$import sockets', '$sock = socket.socket()', 
            '''$import sockets
sock = socket(socket.AF_INET, socket.SOCK_STREAM)''',
            '''$import sockets
socket.socket(socket.AF_INET, socket.SOCK_STREAM)''',
            f'''$import sockets
sever_addr = '{ip_address()}'
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect((server_addr, 80))''', 
            f'''$import sockets
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect((server_addr, 80))'''),'raise an exception'),
            (f'''$import sockets
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostname(), 80))
sock.listen({randint(2,9)})''', 'create a server socket')),

        'fillers': (
            (f'''$from socks import sockets
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect((server_addr, 80)),''', 'cause an infinite loop'),
)
    },
    'Using HTTP GET':{
    'type':'make_items_question_from_pairs',
    'course_code':'1.2.1',      
    'question_with_0':['Match the following code and commentary:','PLACEHOLDER'],
    'question_with_1':'',
    'pairs':(
        ('$GET / HTTP/1.1\r\n', 'method used'), 
        ('$Host: www.site.com\r\n', 'resource'),
        ('$Connection: close\r\n', 'force close'),
        ('$\r\n', 'terminate line'),
        ((
            '$GET / HTTP/1.1','$Host: www.site.com','$Connection: close',
            '$GET / HTML/1.1 \r\n','$HTTP: www.site.com\r\n','$Connect: True\r\n',
          ), 'invalid code')
    ),
    
    'fillers' :(),
    },

    'Using HTTP GET with Python':using_http_get_with_python,

    'Python socket module':{
    'type':'make_items_question_from_pairs',
    'course_code':'1.2.1',      
    'question_with_0':['Match the following:','PLACEHOLDER'],
    'question_with_1':'',
    'pairs':(
        ('$socket', 'be used to create a new socket'), 
        ('$connect', 'attempt to reach a port address'),
        ('$send', ('send a request to a server', 'natively accepts bytes')),
        ('$recv', ('wait for a server response', 'place server response in a bytes like object')),
        ('$AF_INET', 'specify IPv4 address family'),
        ('$SOCK_STREAM', 'specify TCP socket type'),
        ('$SOCK_DGRAM', 'specify UDP socket  type'),
        ('$AF_INET6', 'specify IPv6 address family'),
        ('$AF_UNIX', 'specify UNIX address family'),
        ('$SHUT_RD', ' response will no longer be required after shutdown'),
        (('$sockit', '$conn', '$snd', '$recieve', '$AF_INTERNET', '$AF_LINUX', '$SOCKET_STREAM', '$SOCKET_STRM', '$SOCKET_DGRAM', '$AF_IV6'), 'cause failure'),  
    ),  
    'fillers' :(),
    },


    'Python socket exceptions':{
    'type':'make_items_question_from_pairs',
    'course_code':'1.2.1',      
    'question_with_0':['Match the following exceptions with their causes:','PLACEHOLDER'],
    'question_with_1':'',
    'pairs':(
        ('$socket.gaierror', 'be raised for address-related errors by getaddrinfo() and getnameinfo()'), 
        ('$socket.timeout', 'be raised when the server has not responded'),
        ('$socket.error', 'not be seen because it is deprecated'), 
        ('$socket.herror', 'be raised for address-related errors by getaddrinfo() and getnameinfo()'),
    ),
    'fillers' :(),
    },

    'JSON introduction':{
    'type':'make_items_question_from_pairs',
    'course_code':'1.3.1',      
    'question_with_0':'What does PLACEHOLDER mean?',
    'question_with_1':'',
    'pairs':(
        ('JSON', 'Java Script Object Notation'),
        ('UTF-8', '8-Bit Universal Character Set Transformation Format'), 
        ('serialization', 'process in which a python object is converted into textual or any other portable formal'), 
        ('deserialization', 'process in which a portable format is converted into a python object'), 
    ),
    'fillers' :(),
    },
    'JSON data':{
    'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
    'positive':'correct',
    'negative':'incorrect',
    'course_code':'1.3.1',      
    'question':'Which of the following statements are PLACEHOLDER?',
    'correct':(
        'JSON stands for Java Script Object Notation', 
        'JSON can be used outside of JavaScript code',
        'JSON uses UTF-8 coded text',
        'JSON uses a simple syntax',
        'JSON uses key value pairs to encode objects',
        'JSON can encode integers',
        'JSON can encode floats',
        'JSON can encode strings',
        'JSON can not encode multi-line strings',
        'JSON can only encode single line strings',
        'JSON can encode Boolean Values as \'true\' and \'false\'',
        'JSON\'s version of \'None\' is \'null\'',
        'JSON can encode unicode values',
        'JSON can encode scientific notation',
        'JSON can encode arrays',
        'JSON objects can contain different types of data',
        'JSON objects can be nested',
    ),
    'incorrect' :(
        'JSON stands for Java Script Oriented Notation', 
        'JSON stands for Java Signed Object Notation', 
        'JSON can not be used outside of JavaScript code',
        'JSON uses Unicode coded text',
        'JSON uses a complex syntax',
        'JSON can encode integers as strings',
        'JSON can only encode strings',
        'JSON can encode multi-line strings',
        'JSON can encode \'None\'',
        'JSON can encode Boolean Values as \'True\' and \'False\'',
        'JSON can not encode scientific notation',
        'JSON can not encode arrays',
        'JSON objects must contain similar types of data',
        'JSON objects can not be nested',
        ),
    },
    'JSON dumps':json_dumps,
    'JSON value support':{
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'correct',
        'negative':'incorrect',
        'course_code':'1.3.1',      
        'question':'Which of the following values are supported by json?',
        'correct':(
            f'{randint(1, 100)}', 
            f'int({randint(1, 100)})',
        ),
        'incorrect' :(
            f'bin({randint(1, 100)})', 
            f'oct({randint(1, 100)})',
            f'hex({randint(1, 100)})',        
        ),
    },

    'sockets_with_python':{
        'type':['code_block_outcome','code_block_error_lines'],
        'valid':(
            (
                (('import socket',),'# import a module from the python library'),
                (('server_addr = input("What server do you want to connect to? ")',),'# get users desired server address'),
                ((f"sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)",),'# create socket object'),
                (("sock.connect((server_addr, 80))",),'# connect socket to specified address using HTTP'),
                (('sock.send(b"GET / 4HTTP/1.1\r\nHost: " +"',),'# make HTTP request'),
                (('\t\t\tbytes(server_addr, "utf8") +',),'# specify encoding'),
                (('\t\t\tb"\r\nConnection: close\r\n\r\n")',),'# terminate http message'),
                ((f'reply = sock.recv({choice(["1000","2000","256", "512", "1024",randint(100, 3000)])})',),'# get returned chunk of data'),
                ((f'sock.shutdown(socket.SHUT_{choice(["RDWR","RD","WR"])}',),'# inform server that communication has ended'),
                (('sock.close()',),'# explicitly close connection'),
                (('print(repr(reply))',),'# output reply'),
            ),
        ),
        'invalid':(
            (
                ((f"import {choice(['Socket','sock','connection','socketConnect'])}",),'ModuleNotFoundError'),
                (('import',),'SyntaxError'),
                ((f"from socket import {choice(['Socket','sock','connection','socketConnect'])}",),'ImportError'),
            ),(
                ((f'{choice(["server_ad", "addr", "server_addr"])} = question("What server do you want to connect to? ")','config == configparser.ConfigParser()','configparser.ConfigParser()'),'NameError'),
            ),(
                (("",),'# print an empty list'),
                ((f"config.read('filename.ini'",f"config.read('filename.ini)",f"config.read(filename.ini')"),'SyntaxError'),
                ((f"config.read(filename.ini)", f'read("filename.ini")'),'NameError'),
                ((f"config.{choice(['get','readfile','parse','readall'])}('filename.ini')",),'AttributeError'),
            ),(
                (("config.sections","config.sections()",),'No output'),
                (("print(sections())",'sections()', 'Config.sections', "print('Config.sections()')"),'NameError'),
                (("print(config.sections)",),'# print an object id and memory address'),
            ),
        )
    },
    # requests methods
    # code outcomes
    # return request object meanings #https://pypi.org/project/requests/
    # status code meanings
    # keep alive
    # on a valid url, requests always returns an object
    # no connection raises exception
    # crud acronym
    # python sock
    # valid port or service number
    # valid numbers...
    # valid json string
    # json equivalences
    # dtd
    # json at 427
    # json module
    # 
    
    #new code question type with same data:
    #four alternatives, and say which will get the answer we ask for
    #radmonly select a number of lines to go down the code
    #each correct line of code also has as an arg what will happen if only goes that far
    #make question code, and ask what will happen. 
    
    

}
    
    



