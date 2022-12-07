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

def logging_outcome():
    filename = choice(lc.filenames)
    valid = (
        (
            'import logging',
            'logging.basicConfig()',
            'logger = logging.getLogger()',
            f'''logger.{choice(["warning('WARNING message')","error('ERROR message')","critical('CRITICAL message')" ])}''',
        ),
        'Print a logging message in the format LEVEL:root:message'
    )
    invalid = (
        (
            ((f"import {choice(['log','Logging','logger','Logger', 'LogRecord'])}"),'$ModuleNotFoundError'),
            (('import',),'$SyntaxError'),
            ((f"from logging import {choice(['log','makelogger','Logging','logging'])}",),'$ImportError'),
        ),(
            ((f"logging = basicConfig()","logger.basicConfig()"),'$NameError'),
            ((f"logging.{choice(['Config','Conf','Parseconfig','Configparse','configparser','log'])}()"),'$AttributeError'),
        ),(
            ((f'logger= logg.getLogger()',f'logger= log.getLogger()','logging.getLogger()'),'$NameError'),
            ((f"logger = logging.Logger()", f'logger = logging.getLog()', 'logger = logging.makeLogger()'),'$AttributeError'),
        ),(
            ((f'''logger.{choice(["info('INFO message')","debug('DEBUG message')"])}''',),'$No output'),
            ((f'''logger.{choice(["nolevel('NOLEVEL message')","problem('PROBLEM message')","WARNING('WARNING message')","ERROR('ERROR message')","CRITICAL('CRITICAL message')"])}''',),'$AttributeError'),
            ((f'''logger.{choice(["warning()","error()","critical()"])}''',),'$TypeError'),
        ),
    )
    items, code = ql.make_outcome_items_code(valid, invalid)
    question = [{'text':'What will be the outcome of the following code?'}]
    question.append({'code':code})
    return question, items 

def logging_find_the_line():
    filename = choice(lc.filenames)

    correct = (
        'import logging',
        'logging.basicConfig()',
        'logger = logging.getLogger()',
        f'''logger.{choice(["warning('WARNING message')","error('ERROR message')","warning('WARNING message')","info('INFO message')","debug('DEBUG message')"])}'''
    )
    incorrect = (
        (f"import {choice(['log','Logging','logger','Logger', 'LogRecord'])}",'import',"from logging import {choice(['log','makelogger','Logging','logging'])}"),
        (f"logging = basicConfig()","logger.basicConfig()",f"logging.{choice(['Config','Conf','Parseconfig','Configparse','configparser','log'])}()"),
        (f'logger= logg.getLogger()',f'logger= log.getLogger()','logging.getLogger()',f"logger = logging.Logger()", f'logger = logging.getLog()', 'logger = logging.makeLogger()'),
        (f'''logger.{choice(["nolevel('NOLEVEL message')","problem('PROBLEM message')"])}''',f'''logger.{choice(["warning()","error()","critical()"])}'''),
    )
    items, code = ql.make_error_line_items_code(correct, incorrect)
    question = [{'text':'Which line will cause this code to fail?'}]
    question.append({'code':code})
    return question, items 


def logging_set_level_outcome():
    filename = choice(lc.filenames)
    level = randint(0, 5)

    log_level_dict = {
        0:'NOTSET',
        1:'DEBUG',
        2:'INFO',
        3:'WARNING',
        4:'ERROR',
        5:'CRITICAL',
    }

    legit_levels = [log_level_dict[i] for i in range(level, 6)]
    non_legit_levels = [log_level_dict[i] for i in range(0,level+1)]

    valid = choice([

    (
        (
            'import logging',
            'logging.basicConfig()',
            'logger = logging.getLogger()',
            f'logger.setLevel(logging.{log_level_dict[level]})',
            f'''logger.{choice([f"{item.lower()}('{item} message')" for item in legit_levels])}''',
        ),
        'Print a logging message in the format LEVEL:root:message'
    ),
    (
        (
            'import logging',
            f"logging.basicConfig(level=logging.{log_level_dict[level]}, filename={choice(lc.filenames)}.log', filemode='a')"
            'logger = logging.getLogger()',
            f'logger.setLevel(logging.{log_level_dict[level]})',
            f'''logger.{choice([f"{item.lower()}('{item} message')" for item in legit_levels])}''',
        ),
        'Add a logging message in the format LEVEL:root:message to a file'
    ),
    ])

    invalid = (
        (
            ((f"import {choice(['log','Logging','logger','Logger', 'LogRecord'])}"),'$ModuleNotFoundError'),
            (('import',),'$SyntaxError'),
            ((f"from logging import {choice(['log','makelogger','Logging','logging'])}",),'$ImportError'),
        ),(
            ((f"logging = basicConfig()","logger.basicConfig()"),'$NameError'),
            ((f"logging.{choice(['Config','Conf','Parseconfig','Configparse','configparser','log'])}()"),'$AttributeError'),
        ),(
            ((f'logger= logg.getLogger()',f'logger= log.getLogger()','logging.getLogger()'),'$NameError'),
            ((f"logger = logging.Logger()", f'logger = logging.getLog()', 'logger = logging.makeLogger()'),'$AttributeError'),
        ),(
            ((f'''logger.{choice([f"{item.lower()}('{item} message')" for item in non_legit_levels])}''',),'$No output'),
            ((f'''logger.{choice(["nolevel('NOLEVEL message')","problem('PROBLEM message')"]+[f"{item}('{item} message')" for item in non_legit_levels])}''',),'$AttributeError'),
            ((f'''logger.{choice(["warning()","error()","critical()"])}''',),'$TypeError'),
        ),
    )
    items, code = ql.make_outcome_items_code(valid, invalid)
    question = [{'text':'What will be the outcome of the following code?'}]
    question.append({'code':code})
    return question, items 

def logging_set_level_find_the_line():
    filename = choice(lc.filenames)

    level = randint(0, 5)

    log_level_dict = {
        0:'NOTSET',
        1:'DEBUG',
        2:'INFO',
        3:'WARNING',
        4:'ERROR',
        5:'CRITICAL',
    }

    legit_levels = [log_level_dict[i] for i in range(level, 6)]
    non_legit_levels = [log_level_dict[i] for i in range(0,level+1)]

    correct = (
        'import logging',
        'logging.basicConfig()',
        'logger = logging.getLogger()',
        f'''logger.{choice([f"{item.lower()}('{item} message')" for item in legit_levels])}'''
    )
    incorrect = (
        (f"import {choice(['log','Logging','logger','Logger', 'LogRecord'])}",'import',"from logging import {choice(['log','makelogger','Logging','logging'])}"),
        (f"logging = basicConfig()","logger.basicConfig()",f"logging.{choice(['Config','Conf','Parseconfig','Configparse','configparser','log'])}()"),
        (f'logger= logg.getLogger()',f'logger= log.getLogger()','logging.getLogger()',f"logger = logging.Logger()", f'logger = logging.getLog()', 'logger = logging.makeLogger()'),
        (f'''logger.{choice(["nolevel('NOLEVEL message')","problem('PROBLEM message')"]+[f"{item}('{item} message')" for item in non_legit_levels])}''',f'''logger.{choice(["warning()","error()","critical()"])}'''),
    )
    items, code = ql.make_error_line_items_code(correct, incorrect)
    question = [{'text':'Which line will cause this code to fail?'}]
    question.append({'code':code})
    return question, items 

"""
import logging

FORMAT = '%(name)s:%(levelname)s:%(asctime)s:%(message)s'

logger = logging.getLogger(__name__)

handler = logging.FileHandler('prod.log', mode='w')
handler.setLevel(logging.CRITICAL)

formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.critical('Your CRITICAL message')

https://docs.python.org/3/library/logging.html#logrecord-attributes
"""

def configparser_find_the_line():
    filename = choice(lc.filenames)

    correct = (
        'import configparser',
        'config = configparser.ConfigParser()',
        f"config.read('{filename}.ini')",
        "print('Sections:', config.sections())",
    )
    incorrect = (
        (f"import {choice(['config','conf','parseconfig','configparse'])}","from configparser import {choice(['config','conf','parseconfig','parse'])}",),
        (f"config = {choice(['config','conf','parseconfig','configparse'])}.ConfigParser()",'config == configparser.ConfigParser()','configparser.ConfigParser()',f"config = configparser.{choice(['Config','Conf','Parseconfig','Configparse','configparser'])}()"),
        (f"config.read('{filename}.ini'",f"config.read('{filename}.ini)",f"config.read({filename}.ini')",f"config.read({filename}.ini)", f'read("{filename}.ini")',f"config.{choice(['get','readfile','parse','readall'])}('{filename}.ini')"),
        ("print(sections())",'sections()', 'Config.sections', "print('Config.sections()')"),
    )
    items, code = ql.make_error_line_items_code(correct, incorrect)
    question = [{'text':'Which line will cause this code to fail?'}]
    question.append({'code':code})
    return question, items 


def configparser_outcome():
    filename = choice(lc.filenames)
    valid = (
        (
            'import configparser',
            'config = configparser.ConfigParser()',
            f"config.read('{filename}.ini')",
            "print('Sections:', config.sections())",
        ),
        'Print the section titles of an ini file'
    )
    invalid = (
        (
            ((f"import {choice(['config','conf','parseconfig','configparse'])}"),'$ModuleNotFoundError'),
            (('import',),'$SyntaxError'),
            ((f"from configparser import {choice(['config','conf','parseconfig','parse'])}",),'$ImportError'),
        ),(
            ((f"config = {choice(['config','conf','parseconfig','configparse'])}.ConfigParser()",'config == configparser.ConfigParser()','configparser.ConfigParser()'),'$NameError'),
            ((f"config = configparser.{choice(['Config','Conf','Parseconfig','Configparse','configparser'])}()"),'$AttributeError'),
        ),(
            ((""),'Print an empty list'),
            ((f"config.read('{filename}.ini'",f"config.read('{filename}.ini)",f"config.read({filename}.ini')"),'$SyntaxError'),
            ((f"config.read({filename}.ini)", f'read("{filename}.ini")'),'$NameError'),
            ((f"config.{choice(['get','readfile','parse','readall'])}('{filename}.ini')"),'$AttributeError'),
        ),(
            (("config.sections","config.sections()",),'$No output'),
            (("print(sections())",'sections()', 'Config.sections', "print('Config.sections()')"),'$NameError'),
            (("print(config.sections)",),'Print an object id and memory address'),
        ),
    )
    items, code = ql.make_outcome_items_code(valid, invalid)
    question = [{'text':'What will be the outcome of the following code?'}]
    question.append({'code':code})
    return question, items 