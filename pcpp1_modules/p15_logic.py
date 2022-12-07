from random import randint, choice

from python_institute.utilities import utilities as utl
from python_institute.utilities import helper_functions as hf
from python_institute.utilities import lists_and_content as lc
from python_institute.utilities import question_logic as ql


def sql_commands():
    names = ['duck', 'stool', 'door','cup', 'tennis', 'pool','monkey','chair','orange','fruit','trampoline','beef','employees','customers','shoes','pants','troopers','rioters','clocks']
    data_types = ['INT','TEXT','DATE','TIME',f'CHAR({randint(1,20)})','REAL','DEC', 'BOOLEAN', f'BINARY({randint(1,16)})']
    entities = ['DATABASE', 'TABLE',]
    selection = randint(0, len(entities)-1)
    entity = entities[selection]
    name = names[randint(0, len(names)-1)]
    answer = f'CREATE {entity} {name}'
    data = '('
    for i in range(randint(1,4)):
        data += f"{names[randint(0, len(names)-1)]} {data_types[randint(0, len(data_types)-1)]}, "
    data = data[:-2] + ')'
    if selection == 0:
        a,b,c = f'CREATE {name} {entity};', f'CREATE {entity} {name} {data};', f'CREATE {entity};'
        answer += ';'
    else:
        answer += data + ';'
        a,b,c = f'CREATE {name} {entity};', f'CREATE {entity} {data} {name};', f'CREATE {entity} {data};'
    raw_items = [a,b,c]
    id = 1
    items = [{'code':answer, 'indicator':'correct', 'id':f'item{id}'}]
    for item in raw_items:
        id+=1
        items.append({'code':item, 'indicator':'incorrect', 'id':f'item{id}'})

    question = [{'text':f'Which of the following statements for creating a {entity} named {name} is valid:'}]
    return  question, items

def sqlite_find_the_line():
    filename = choice(lc.filenames)

    create = '''CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    priority INTEGER NOT NULL
    );'''

    correct = (
        'import sqlite3',
        f"conn = sqlite3.connect('{filename}.db')",
        'c = conn.cursor()',
        'conn.commit()',
        'conn.close()',
    )
    incorrect = (
        ('import sqlite','import sql', 'import', 'from sqlite3 import sql'),
        (
            f"conn = sqlite.connect('{filename}.db')",
            f"conn = sqlite2.connect('{filename}.db')",
            f"connect = sqlite3.conn('{filename}.db')",
            f"conn = sqlite3.open('{filename}.db')",
            f"connect = sqlite3.conn('{filename}.db'",
            f"conn = sqlite3.open('{filename}.db)",
        ),
        (
            'c = cursor()', 'c = curse()', 'c = conncursor()', 'c = conn.curse()',
            'c = conn.connection()','c = conn.curse)','c : conn.curse()',
        ),
        ('conn.comit()'),
        ('c.close()'),
    )
    items, code = ql.make_error_line_items_code(correct, incorrect)
    question = [{'text':'Which line will cause this code to fail?'}]
    question.append({'code':code})
    return question, items 

def sqlite_outcome():
    filename = choice(lc.filenames)
    valid = (
        (
            'import sqlite3',
            f"conn = sqlite3.connect('{filename}.db')",
            'c = conn.cursor()',
            'conn.commit()',
            'conn.close()',
        ),
        'The code will execute without errors, creating a database file'
    )
    invalid = (
        (
            (('import sqlite','import sql',),'$ModuleNotFoundError'),
            (('import',),'$SyntaxError'),
            (('from sqlite3 import sql',),'$ImportError'),
        ),(
            ((f"conn = sqlite.connect('{filename}.db')",f"conn = sqlite2.connect('{filename}.db')"),'$NameError'),
            ((f"connect = sqlite3.conn('{filename}.db')",f"conn = sqlite3.open('{filename}.db')"),'$AttributeError'),
            ((f"conn = sqlite3.connect('{filename}.db'",f"conn = sqlite3.connect('{filename}.db)"),'$SyntaxError'),
            ((f"conn = sqlite3.connect()",),'Run without errors but create no database file'),
            ((f"conn = sqlite3.connect(':memory:')",),'Run without errors creating and closing a temporary database'),
        ),(
            (('c = cursor()', 'c = curse()', 'c = conncursor()'),'$NameError'),
            (('c = conn.curse()', 'c = conn.connection()'),'$AttributeError'),
            (('c = conn.curse',),'Run without errors, but without a cursor object being created'),
            (('c = conn.curse)','c : conn.curse()'),'$SyntaxError'),    
        ),(
            (('conn.comit()',),'$AttributeError'),
        ),(
            (('c.close()',),'$AttributeError'),
        )
    )
    items, code = ql.make_outcome_items_code(valid, invalid)
    question = [{'text':'What will be the outcome of the following code?'}]
    question.append({'code':code})
    return question, items 


def log_level_order():
    """CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET
    """
    num_choices=4
    question_text='What are the Python logging levels from PLACEHOLDER?'
    ascending_order, descending_order= 'highest to lowest', 'lowest to highest'
    correct_list=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'NOTSET']#least to most default
    fillers=['IMPORTANT','NOTICE', 'EXIT', 'UNSET', 'LOG', 'NOT IMPORTANT', 'NOT CRITICAL']
    return utl.generic_correct_order(num_choices, question_text, ascending_order, descending_order, correct_list, fillers)