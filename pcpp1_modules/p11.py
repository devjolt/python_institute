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
        ),
        'fillers': (),
    },
    """
    'Useful functions': {
        'question_with_0':'What does PLACEHOLDER do?',
        'question_with_1':'',
        'type':['make_items_question_from_pairs'],
        'pairs':(
            ('dir()', 'returns a list of an object\'s attributes and methods'),
            ('help()', 'returns documentation explaining an object\'s attributes and methods'),
            
        ),
        'fillers': (),
    },
    """
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

    
}
"""
    'Polymorphism, ': {
        'question_with_0':('What definition best fits the following:','PLACEHOLDER'),
        'question_with_1':('What is best defined by the following:','PLACEHOLDER'),
        'type':['make_items_question_from_pairs'],
        'pairs':(
            ('polymorphism', ('the provision of a single interface to objects of different types', 'the ability to create abstract methods from specific types in order to treat those types in a uniform way')),
            ('duck typing ', ("determining whether an object can be used for a particular purpose by examining the presence of attributes")),
        ),
        'fillers': (),
    },
    """