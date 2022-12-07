from random import randint, shuffle, choice

from python_institute.utilities import utilities as utl


def using_http_get_with_python():
    question = [{'text':'Which line will cause this request to fail?'}]

    options = ['SHUT_RDWR', 'SHUT_WR', 'SHUT_RDWR']

    correct = (
        ('import socket',),
        ("server_addr = 'www.server.com'",),
        ('sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)',),
        ('sock.connect((server_addr, 80))',),
        ('sock.send(b"GET / HTTP/1.1\\r\\nHost: " +',),
        ('      bytes(server_addr, "utf8") +',),
        ('      b"\\r\\nConnection: close\\r\\n\\r\\n")',),
        (f'reply = sock.recv({randint(100, 10000)})',),
        (f'sock.shutdown(socket.{choice(options)})',),
        ('sock.close()',),
    )

    incorrect = (
        (
        'import sock', 
        'from socket import socket',
        'from socket',
        'import server'
        ),(
        "server_addr = www.server.com",
        "server_addr = 'www.server.com"
        "server_addr = www.server.com'"
        ),(
        'sock = socket.socket(AF_INET, SOCK_STREAM)', 
        'sock = socket(socket.AF_INET, socket.SOCK_STREAM)', 
        'sock = socket.socket(socket.AF_INET, socket.SOCKET_STREAM)', 
        'sock = socket.socket(socket.AF_INTERNET, socket.SOCK_STREAM)',
        'sock = socket.socket(sock.AF_INET, sock.SOCK_STREAM)',
        'socket = socket.sock(socket.AF_INET, socket.SOCK_STREAM)'
        ),(
        'socket.connect((server_addr, 80))',
        'sock.conn((server_addr, 80))',
        'sock.connect((80, server_addr))',
        'sock.socket((server_addr, 80))',
        'sock.connect((server_addr, 80)'
        ),(
        'sock.send("GET / HTTP/1.1\\r\\nHost: " +',
        'sock.send(b"GET / HTML/1.1\\r\\nHost: " +',
        'sock.send(r"GET / HTTP/1.1\\r\\nHost: " +',
        'socket.send(b"GET / HTTP/1.1\\r\\nHost: " +',
        ),(
        '       str(server_addr, "utf8") +',
        '       bytes("utf8", server_addr) +',
        '       bytes(server, "utf8") +',
        '       bytes(server_addr, "uht8") +',
        '       bytes(server_addr, "utf8")) +',
        '       bytes(server_addr, "utf8" +'
        ),(
        '       b"\\r\\nConnection: close\\r\\n\\r\\n"))''',
        '       "\\r\\nConnection: close\\r\\n\\r\\n")''',
        '       r"\\r\\nConnection: close\\r\\n\\r\\n")''',
        '       b"\\r\\nConnection: end\\r\\n\\r\\n")''',
        '       b"\\r\\nConnection: close")''',
        '       b"\\r\\nclose\\r\\n\\r\\n")''',
        '       b"\Connection: close\\r\\n\\r\\n")''',
        ),(
        'reply = socket.recv(10000)',
        'reply = socket.recieve(10000)',
        'reply = sock.recieve(None)',
        'reply = socket.recv(10000)',
        ),(
        'socket.shutdown(socket.SHUT_RDWR)',
        'sock.shtdwn(socket.SHUT_RDWR)',
        f'socket.shutdown(sock.{choice(options)})',
        ),(
        'socket.close()',
        'sock.shut()',
        'sock.end()',
        )
    )
    items, code = utl.make_error_line_items_code(correct, incorrect)
    #for line in code:
    question.append({'code':code})
    return question, items

def json_dumps():
    name = choice(utl.names)
    age = str(randint(10,99))
    
    options = (
        (f'''import json
class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def encode_who(w):
    if isinstance(w, Who):
        return w.__dict__ 
    else:
        raise TypeError(w.__class__.__name__ + ' is not JSON serializable')

some_man = Who(f'{name}', {age})
print(json.dumps(some_man, default=encode_who))''', f'{{"name": "{name}", "age": {age}}}'),

(f'''import jason

class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def encode_who(w):
    if isinstance(w, Who):
        return w.__dict__ 
    else:
        raise TypeError(w.__class__.__name__ + ' is not JSON serializable')

some_man = Who(f'{name}', {age})
print(json.dumps(some_man, default=encode_who))''','ModuleNotFoundError'),

(f'''import json

class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def encode_who(w):
    if isinstance(w, Who):
        return w 
    else:
        raise TypeError(w.__class__.__name__ + ' is not JSON serializable')

some_man = Who(f'{name}', {age})
print(json.dumps(some_man, default=encode_who))''','ValueError: Circular reference detected'),

(f'''import json

class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def encode_who(w):
    if isinstance(w, Who):
        return w.__dict__
    else:
        raise TypeError(w.__class__.__name__ + ' is not JSON serializable')

some_man = Who(f'{name}', {age})
json.dumps(some_man, default=encode_who)''', 'There will be no output'),

(f'''import json

class Who:
def __init__(self, name, age):
    self.name = name
    self.age = age

def encode_who(w):
    if isinstance(w, Who):
        return w.__dict__ 
    else:
        raise TypeError(w.__class__.__name__ + ' is not JSON serializable')

some_man = Who(f'{name}', {age})
print(json.dumps(some_man, default=encode_who))''', 'syntax error - expected an indented block'), 

(f'''import json

class Who:
def __init__(self, name, age):
    self.name = name
    self.age = age

def encode_who(w):
    if isinstance(w, Who):
        return w.__dict__ 
    else:
        raise TypeError(w.__class__.__name__ + ' is not JSON serializable')

some_man = Who(f'{name}', {age})
print(json.dumps(some_man))''', 'TypeError: Object of type Who is not JSON serializable'), 
    )
    chosen_num = randint(0, len(options)-1)
    code = options[chosen_num][0]
    id = 1
    used = [chosen_num]
    items = [{'item':options[chosen_num][1], 'indicator':'correct', 'id':f'item{id}'}]
    
    while len(used) !=4:
        chosen_num = randint(0, len(options)-1)
        if chosen_num not in used:
            id+=1
            items.append({'item':options[chosen_num][1], 'indicator':'incorrect', 'id':f'item{id}'})
            used.append(chosen_num)

    question = [
        {'text':'What will be the output from the following code?'},
        {'code':code},
        ]
    return  question, items