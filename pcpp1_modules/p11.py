from .p11_logic import *

questions = {
    'Classes, instances, attributes and methods': {
        'question_with_0':('What definition best fits the following:','PLACEHOLDER'),
        'question_with_1':('What is best defined by the following:','PLACEHOLDER'),
        'type':['make_items_question_from_pairs'],
        'pairs':(
            ('a class', 'an idea, blueprint, or recipe for an instance'),
            ('an instance', ("an instantiation of the class; very often used interchangeably with the term 'object'")),
            ('an object', "Python's representation of data and methods; could be aggregates of instances"),
            ('an attribute', ("a class trait",  "a variable or method")),
            ('a method', ("a function built into a class that is executed on behalf of the class or object","a callable attribute")),
            ('a type', "the class that was used to instantiate an object"),
            ('a class variable',('defined within class construction', 'available before an instance is created','accessed via CLASS.VARIABLE_NAME and OBJECT.VARIABLE_NAME', 'not listed in OBJECT.__dict__')),
            ('an instance variable',('exists only when it is explicitly created and added to an object','added during objects initialization', 'will not interfere with a similar variable in another object', 'accessed via OBJECT.VARIABLE_NAME', 'listed in OBJECT.__dict__')),        
            ('an instance method',('performs operations on instances','perform operations on attributes of an instance', 'will not interfere with a similar variable in another object')),
        ),
        'fillers': (),
    },

    'useful_tools': {
        'question_with_0':('What description best fits the following:','PLACEHOLDER'),
        'question_with_1':('What is best described by the following:','PLACEHOLDER'),
        'type':['make_items_question_from_pairs'],
        'pairs':(
            ('help()', 'displays an object\'s documentation'),
            ('dir()', f"a built in function which returns a list of the {choice(['attributes', 'variables and methods'])} of an object"),
            ('__dict__', "contains an object's variables and their values"),
            ('type()', ("returns the class used instantiate an object", "returns an instance's class")),
            ('self',('the first parameter of an instance method','allows you to refer to an existing instance')),
            ('isinstance()',('returns True if the specified object is of the specified type',)),
            
        ),
        'fillers': (
            (('info()', 'dict(), self()', '__help__', '__dir__', 'ininstance()'), ('returns true if the specified object is a class', 'returns true if the specified object is an instance', 'returns an object\'s documentation', 'displays the type of an object', 'displays an object\'s variables and their values'))
        ),
    },
    'OOP Foundations': {
        'question_with_0': ('What definition best fits the following:', 'PLACEHOLDER'),
        'question_with_1': ('What is best defined by the following:', 'PLACEHOLDER'),
        'pairs': (
            ('Class', ('blueprint for objects', 'encapsulates data and behavior', 'can be instantiated')),
            ('Inheritance', ('enables code reuse', 'establishes "is-a" relationships', 'promotes modularity')),
            ('Polymorphism', ('ability to take on multiple forms', 'includes method overloading', 'enhances flexibility')),
            ('Encapsulation', ('hides implementation details', 'bundles data and methods', 'promotes data security')),
            ('Abstraction', ('focuses on essential features', 'reduces complexity', 'provides a simplified view')),
        ),
        'fillers': (
            ('Algorithm', ('step-by-step procedure', 'DNA sequence', 'static class method')),
        ),
    },
    "instance_class_variables_differences": {
        'question':'Which of the following describes PLACEHOLDER variable?',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'an instance',
        'negative':'a class',
        'course_code':'',
        'correct':(
            'does not change if a variable in a different instance with the same namespace changes',
            'contains information related to an instance',
            'cannot be accessed through the class namespace',
            'does not exist before an instance is created',
            'can be accessed through the object keyword',
            'can be accessed through the self keyword',
        ),
        'incorrect': (
            'can refer to meta information shared amongst instances',
            'can be referred to prior to the creation of an instance',
            'cannot be accessed through the object keyword',
            'cannot be accessed through the self keyword',
        ),
    },
    'inheritance and polymorphism': {
        'question_with_0':('What description best fits the following:','PLACEHOLDER'),
        'question_with_1':('What is best described by the following:','PLACEHOLDER'),
        'type':['make_items_question_from_pairs'],
        'pairs':(
            ('inheritance',('an "is a" relation','a way of building a new class by using a previously defined repetoire of traits', f"expresses the fundamental relationships between {choice(['superclasses and subclasses', 'parent classes and descendants'])}")),
            ('polymorphism', f"a built in function which returns a list of the {choice(['attributes', 'variables and methods'])} of an object"),
            ('single inheritance', "where a class inherits from another class"),
            ('multiple inheritance', ("where a class inherits from other classes", "risks violating the single responsiblity principle")),
            ('method resolution order',('how python acts when a class inherits from other classes',"how python searches for inherited attributes")),
            ('diamond problem',"ambiguity in defining attribute inheritance"),
            ('class heirarchy','family tree for a group of classes'),
            ('composition',('an alternative to multiple inheritance', 'a "has a" relation')),
            ('duck typing','a way to determine whether an object can be used for a particular purpose'),

        ),
        'fillers': (
            (('decomposition, ruby problem', 'minority inheritance', 'monomorphism', 'instance', 'method', 'info()'), ('returns true if the specified object is a class', 'importing an object', 'returns an object\'s documentation', 'displaying the type of an object', 'creating an instance'))
        ),
    },

    "args_and_kwargs": {
        'question':'Which of the following are PLACEHOLDER?',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'correct',
        'negative':'incorrect',
        'course_code':'',
        'correct':(
            'using the name args is just a convention',
            'using the name kwargs is just a convention',
            'if present, kwargs must be the last argument listed',
            'if both are present, args must follow kwargs',
            'if other arguments are present, args must come after them',
            'args refers to a tuple of positional arguments',
            'args are not explicitly expected',
            'kwargs are not explicitly expected',
            'kwargs refers to key value arguments',
            '* can be used with any available namespace to store args',
            '** can be used with any available namespace to store kwargs',
        ),
        'incorrect': (
            'using the name args is essential',
            'using the name kwargs is essential',
            'kwargs can be listed at any point within the arguments',
            'if both are present, kwargs must follow args',
            'if other arguments are present, args must come before them',
            'args refers to a key value arguments',
            'args are explicitly expected',
            'kwargs are explicitly expected',
            'kwargs refers to a tuple of arguments',
            '* can only be used with the namespace args',
            '** can only be used with the namespace kwargs',
        ),
    },
    'args_and_kwargs_pairs': {
        'question_with_0':('Which function declaration is best described as PLACEHOLDER?'),
        'question_with_1':('What description best fits the following function declaration:','PLACEHOLDER'),
        'type':['make_items_question_from_pairs'],
        'pairs':(
            ('a good implementation', f'$def func({choice(["*args", "*args, **kwargs", "a, *args, **kwargs", "a, *args", "a, **kwargs"])}):'),
            ('an unconventional but good implementation ', f'$def func({choice(["*b", "*b, **c", "a, *b, **c", "a, *b", "a, **c"])}):'),
            ('an unconventional implementation which is not incorrect but risks confusion', f'$def func({choice(["*kwargs", "*kwargs, **args", "a, *kwargs, **args", "a, *kwargs", "a, **args"])}):'),
            ('an erroneous implementation leading to TypeError', f'$def func({choice(["*args, c", "*args, b","a, *args, b"])}):'),
            ('an erroneous implementation causing a syntax error', f'$def func({choice(["**kwargs, c", "**kwargs, b","**kwargs, *args, b"])}):'),
        ),
        'fillers': (),
    },
    'Comparison_unary_binary_and_agmented_operators_and_functions': {
        'question_with_0':'Which of the following isPOSNEG PLACEHOLDER?',
        'question_with_1':'Which most accurately describes the following: PLACEHOLDER',
        'positive_negative':('','not'),
        'type':['posneg_pairs', 'new_pairs'],
        'pairs':(
            ('a comparison method', ('__eq__', '__ne__', '__lt__', '__gt__', '__le__', '__ge__')),
            ('a unary operator or function', ('__pos__', '__neg__', '__abs__', '__round__')),
            ('a common, binary operator or function',('__add__', '__sub__', '__mul__', '__floordiv__', '__div__', '__mod__', '__pow__')),
            ('an augumented operator or function', ('__iadd__', '__isub__', '__imul__', '__ifloordiv__', '__idiv__', '__imod__', '__ipow__'))
        ),
        'fillers': (),
    },

    'Type_conversion_introspection_object_retrospection_attribute_and_container_access': {
        'question_with_0':'Which of the following isPOSNEG used for PLACEHOLDER?',
        'question_with_1':'Which most accurately describes the following: PLACEHOLDER',
        'positive_negative':('','not'),
        'type':['posneg_pairs', 'new_pairs'],
        'pairs':(
            ('type conversion', ('__int__', '__float__', '__oct__', '__hex__')),
            ('object introspection', ('__str__', '__repr__', '__format__', '__hash__', '__dir__', '__nonzero__')),
            ('object retrospection',('__instancecheck__', '__subclasscheck__')),
            ('object attribute access', ('__getattr__', '__getattribute__', '__setattr__', '__delattr__')),
            ('allowing access to containers', ('__len__', '__getitem__', '__setitem__', '__delitem__', '__iter__', '__contains__')),
            
        
        ),  
        'fillers': (),
    },
    'object_types': object_types,
    'class_info':class_info,

    'methods': {
        'question_with_0':('What definition best fits the following:','PLACEHOLDER'),
        'question_with_1':('What is best defined by the following:','PLACEHOLDER'),
        'type':['make_items_question_from_pairs'],
        'pairs':(
            ('abstract method', ('a blank method', "part of a contract between class designer and programmer", "makes the owner's class an abstract class")),
            (('dunder method','magic method'), ("start and end with double underscores", "invoked indirectly through another action", "can be overloaded")),
            ('class method', ("uses @classmethod decorator", "works on class attributes", "conventionally uses cls argument", "can be used as an alternative constuctor")),
            ('static method', ("uses @staticmethod decorator", "semantically related to a class", "does not work directly on class attributes", "does not work directly on instance attributes")),
            ('instance method', ("conventionally uses the self argument","can not be called until instantiation", "called using instance namespace")),
        ),
        'fillers': (
            (("function method","decorator method"),("uses @instancemethod decorator","is called automatically on instantiation", "works on builtin python attributes"))
        ),
    },
    "abstract_classes": {
        'question':'Which of the following are PLACEHOLDER?',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'correct',
        'negative':'incorrect',
        'course_code':'',
        'correct':(
            'if any abstract methods are present in a class, the class is abstract',
            'an abstract method has a declaration but no implementation',
            '@abc.abstractmethod is used to denote an abstract method',
            'an abstract class inherits from abc.ABC',
            'abstract methods need to be overridden in child classes',
            'abstract methods are a contract between class designer and a programmer',
            'abstract classes cannot be instantiated',
            'child classes of abstract classes can be instantiated',
        ),
        'incorrect': (
            'if all methods present in a class are abstract, the class is abstract',
            'an abstract method if a fully defined method',
            '@ABC.abstractmethod is used to denote an abstract method',
            '@abstractmethod is used to denote an abstract method',
            'an abstract class inherits from ABC.abc',
            'an abstract class inherits from abc.abc',
            'an abstract class inherits from abc',
            'an abstract class inherits from ABC',
            'abstract methods may be overridden in child classes',
            'abstract classes can be instantiated',
            'abstract classes can be instantiated if they inherit from abc',
            'child classes of abstract classes cannot be instantiated',
        ),
    },
    
    
    'Encapsulation': {
        'question_with_0':('What definition best fits the following:','PLACEHOLDER'),
        'question_with_1':('What is best defined by the following:','PLACEHOLDER'),
        'type':['make_items_question_from_pairs'],
        'pairs':(
            ('getter', ('a method which designates the name of the attribute to be used by external code', "decorated with @property")),
            ("setter", ("allows external code to change an attribute", "sets conditions under which external code can change an attribute", "decorated with @name.setter")),
            ('deleter', ("allows external code to delete an attribute", "decorated with @name.deleter")),
        ),
        'fillers': (
            (("accesser","instantiater"),("decorated with @getter", "decorated with @deleter", "decorated with @setter","is called automatically on instantiation", "works on builtin python attributes"))
        ),
    },
    'Exceptions': {
        'question_with_0':('What definition best fits the following:','PLACEHOLDER'),
        'question_with_1':('What is best defined by the following:','PLACEHOLDER'),
        'type':['make_items_question_from_pairs'],
        'pairs':(
            ('exception', ('a special kind of data', 'a special kind of object')),
            ("raising an exception", ("stopping a program and creating a special object")),
            ('handling', ("responding to a event which would otherwise cause a program to terminate")),
            ('terminating', ("ending a program as a result of an situation the program is not prepared for")),
            ('chaining', ('making infomation about an exception which causes another available')),
            ('implicit chaining', ('incidentally triggering an exception whilst handling another', 'information original exception accessed through __context__')),
            ('explicit chaining', ('translating one type of exception to another', 'information about original exception accessed through __cause__')),    
        ),
        'fillers': (
            ()
        ),
    },
    """
    'syntax': {
        'question_with_0':('What definition best fits the following:','PLACEHOLDER'),
        'question_with_1':('What is best defined by the following:','PLACEHOLDER'),
        'type':['make_items_question_from_pairs'],
        'pairs':(
            ('import traceback')
            ('try:', ('a special kind of data', 'a special kind of object')),
            ("except Exception as e:", ("stopping a program and creating a special object")),
            ('args', ("responding to a event which would otherwise cause a program to terminate")),
            ('name', ("ending a program as a result of an situation the program is not prepared for")),
            ('__context__', ("a clause within which an event can be handled")),
            ('__cause__', ("a clause within which an event can be handled")),
            ('__traceback__', ("a clause within which an event can be handled")),
            ('__traceback__', ("a clause within which an event can be handled")),
            ('raise Exception from f')
            

            
    
        ),
        'fillers': (
            ()
        ),
    },
    """
    'copying_compound_objects': {
        'question_with_0':('What definition best fits the following:','PLACEHOLDER'),
        'question_with_1':('What is best defined by the following:','PLACEHOLDER'),
        'type':['make_items_question_from_pairs'],
        'pairs':(
            ('simple copy', ("$thing2 = thing1", "copying the reference of an object", "not creating any new objects", "copied and copy have same id")),
            ("shallow copy", ("$thing2 = thing1[:]","$thing2 = copy.copy(thing1)", "creating a new object and copying references to all objects it contains")),
            ('deep copy', ("$thing2 = copy.deepcopy(thing1)", "No references are copied", "all objects in the new namespace are independent")),
        ),
        'fillers': (
            (("quick copy","master copy"),("largest objects are copied first", "$thing2 = copy.copyall(thing1)","$thing2 = copy.shallowcopy(thing1)","$thing2 = copy.refcopy(thing1)","all objects are cached in RAM"))
        ),
    },
    "pickle": {
        'question':'Which of the following arePLACEHOLDER serialisable canPLACEHOLDER be pickled?',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'',
        'negative':' not',
        'course_code':'',
        'correct':(
            '$None','$True','$False',
            'integers',
            'floats',
            'booleans',
            'bytes','bytearrays',
            'tuples','lists','sets',
            'references to functions and classes',
            'dictionaries',
        ),
        'incorrect': (
            'file handlers',
            'sockets',
            'module objects',
            'functions',
            'classes'
        ),
    },



    
'Shallow and Deep Operations': {
    'description': 'Explore the concepts of shallow and deep operations in Python:',
    'question_with_0': ('What is best defined by the following topic:', 'PLACEHOLDER'),
    'question_with_1': ('What definition best fits the following topic:', 'PLACEHOLDER'),
    'type':['make_items_question_from_pairs'],
    'pairs': (
        ('Shallow Copy', ('creates a new object', 'references original objects', 'changes in one affect the other')),
        ('Deep Copy', ('creates an independent object', 'creates copies of nested objects', 'independent of the original')),
        ('Shallow Operation', ('applies to the top-level elements', 'shares references', 'modifies original objects')),
        ('Deep Operation', ('applies recursively to nested elements', 'creates independent copies at all levels', 'isolated from the original')),
        ('Mutable Objects', ('can be modified in place', 'lists and dictionaries', 'affected by shallow operations')),
    ),
    'fillers': (
        ('Immutable Objects', ('cannot be modified in place', 'tuples and strings', 'unaffected by shallow operations')),
    ),
},
'Abstract Classes, Method Overriding, Static and Class Methods, Special Methods': {

    'question_with_0': ('What is best defined by the following topic:', 'PLACEHOLDER'),
    'question_with_1': ('What definition best fits the following topic:', 'PLACEHOLDER'),
    'pairs': (
        ('Abstract Classes', ('cannot be instantiated', 'may have abstract methods', 'provides a blueprint for subclasses')),
        ('Method Overriding', ('redefines a method in a subclass', 'maintains the same method name', 'overrides the behavior of the superclass')),
        ('Static Methods', ('belongs to the class', 'does not have access to class attributes', 'cannot modify instance state')),
        ('Class Methods', ('belongs to the class', 'has access to class attributes', 'can modify class state')),
        ('Special Methods', ('surrounded by double underscores', 'used for operator overloading', 'provides a way to customize object behavior')),
    ),
    'fillers': (
        ('Instance Methods', ('belong to the instance', 'can modify class attributes', 'used for operator overloading')),
    ),
},


'Inheritance, Polymorphism, Subclasses, and Encapsulation': {
    'question_with_0': ('What is best defined by the following topic:', 'PLACEHOLDER'),
    'question_with_1': ('What definition best fits the following topic:', 'PLACEHOLDER'),
    'type':['make_items_question_from_pairs'],
    'pairs': (
        ('Inheritance', ('enables code reuse', 'establishes "is-a" relationships', 'promotes modularity')),
        ('Polymorphism', ('ability to take on multiple forms', 'includes method overloading', 'enhances flexibility')),
        ('Subclasses', ('inherit from a superclass', 'can override methods', 'specialized versions of a class')),
        ('Encapsulation', ('hides implementation details', 'bundles data and methods', 'promotes data security')),
    ),
    'fillers': (
        ('Abstraction', ('focuses on essential features', 'reduces complexity', 'provides a simplified view')),
    ),
},

'Advanced Exception Handling Techniques': {
    'question_with_0': ('What is best defined by the following topic:', 'PLACEHOLDER'),
    'question_with_1': ('What definition best fits the following topic:', 'PLACEHOLDER'),
    'type':['make_items_question_from_pairs'],
    'pairs': (
        ('Custom Exceptions', ('user-defined exception classes', 'allows specific error handling', 'inherits from the base Exception class')),
        ('Context Managers', ('manages resources using "with" statement', 'implements __enter__ and __exit__ methods', 'ensures proper resource cleanup')),
        ('Exception Chaining', ('captures multiple exceptions', 'preserves the context of the original exception', 'provides a traceback for each exception')),
        ('Handling Multiple Exceptions', ('multiple except blocks', 'order matters in exception handling', 'catches and handles different exception types')),
    ),
    'fillers': (
        ('Basic Exception Handling', ('uses try, except, and finally', 'handles a single exception type', 'may lack specificity')),
    ),
},

'Advanced Exception Handling Techniques 2': {
        'question_with_0': ('What is best defined by the following topic:', 'PLACEHOLDER'),
        'question_with_1': ('What definition best fits the following topic:', 'PLACEHOLDER'),
        'type':['make_items_question_from_pairs'],
        'pairs': (
            ('Custom Exceptions', (
                'user-defined exception classes',
                'specific error handling',
                'inherits from base Exception',
                'class CustomError(Exception): pass',
            )),
            ('Context Managers', (
                '"with" statement for resource management',
                '__enter__ and __exit__ methods',
                'ensures proper cleanup',
                'with open("example.txt", "r") as file:',
            )),
            ('Exception Chaining', (
                'captures multiple exceptions',
                'preserves context of original exception',
                'provides traceback for each',
                'try: except Exception as e: raise CustomError("An error occurred") from e',
            )),
            ('Handling Multiple Exceptions', (
                'multiple except blocks',
                'order matters in handling',
                'catches different exception types',
                'try: except FileNotFoundError: except ValueError:',
            )),
        ),
        'fillers': (
            ('Basic Exception Handling', (
                'uses try, except, and finally',
                'handles single exception type',
                'may lack specificity',
                'try: except Exception as e: print("An error occurred:", e)',
            )),
        ),
    },

    'Pickle and Shelve Modules': {
        'question_with_0': ('What common functionality do the following modules provide:', 'PLACEHOLDER'),
        'question_with_1': ('Which description best fits the following modules:', 'PLACEHOLDER'),
        'type':['make_items_question_from_pairs'],
        'pairs': (
            ('Pickle Module', (
                'serialization and deserialization of Python objects',
                'converts objects into byte streams',
                'saves and loads complex data structures',
                'import pickle',
            )),
            ('Shelve Module', (
                'persistent dictionary-like storage',
                'stores and retrieves Python objects',
                'uses pickle for serialization',
                'import shelve',
            )),
        ),
        'fillers': (
            ('JSON Module', (
                'handles JavaScript Object Notation',
                'used for data interchange',
                'human-readable and writable format',
                'import json',
            )),
            ('SQLite Module', (
                'handles relational databases',
                'provides SQL-based storage',
                'requires a separate database file',
                'import sqlite3',
            )),
        ),
    },

    
    'Metaclasses in Python': {
        'question_with_0': ('What is the primary purpose of the following concept:', 'PLACEHOLDER'),
        'question_with_1': ('Which definition best describes the following concept:', 'PLACEHOLDER'),
        'type':['make_items_question_from_pairs'],
        'pairs': (
            ('Metaclasses', (
                'define the behavior of classes',
                'create classes dynamically',
                'are the class of a class',
                'often used for code introspection',
            )),
            ('Decorators', (
                'modify or extend functions or methods',
                'applied using the "@" syntax',
                'commonly used for aspect-oriented programming',
                'import functools',
            )),
            ('Abstract Classes', (
                'cannot be instantiated',
                'may have abstract methods',
                'provides a blueprint for subclasses',
                'from abc import ABC, abstractmethod',
            )),
            ('Class Methods', (
                'belongs to the class',
                'has access to class attributes',
                'can modify class state',
                'def class_method(cls): pass',
            )),
        ),
        'fillers': (
            ('Inheritance', (
                'establishes "is-a" relationships',
                'promotes code reuse',
                'creates a hierarchy of classes',
                'class Derived(Base): pass',
            )),
            ('Modules', (
                'encapsulate code and data',
                'provide a namespace for identifiers',
                'can be imported using import statement',
                'import module_name',
            )),
        ),
    },



    'Object Persistence': {
        'question_with_0': ('What is the primary purpose of the following concept:', 'PLACEHOLDER'),
        'question_with_1': ('Which definition best describes the following concept:', 'PLACEHOLDER'),
        'type':['make_items_question_from_pairs'],
        'pairs': (
            ('Object Persistence', (
                'the ability to store and retrieve objects',
                'maintains the state of objects between sessions',
                'enables long-term storage and retrieval',
                'commonly used in databases and file systems',
            )),
            ('Serialization', (
                'converts objects into a byte stream',
                'facilitates storage and transmission',
                'allows objects to be reconstructed',
                'import pickle',
            )),
            ('Caching', (
                'temporary storage for faster access',
                'reduces the need for redundant computations',
                'improves performance by storing frequently used data',
                'used in memory or external storage',
            )),
            ('ORM (Object-Relational Mapping)', (
                'maps objects to database tables',
                'facilitates database interactions using objects',
                'provides a higher-level abstraction for database operations',
                'examples include SQLAlchemy and Django ORM',
            )),
        ),
        'fillers': (
            ('Polymorphism', (
                'ability to take on multiple forms',
                'used for method overloading',
                'enhances flexibility in object-oriented programming',
                'class Shape: def draw(self): pass',
            )),
            ('Multithreading', (
                'concurrent execution of multiple threads',
                'improves parallelism in programs',
                'deals with concurrent tasks or processes',
                'import threading',
            )),
        ),
    },
}



