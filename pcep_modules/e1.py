from random import randint, choice

from .e1_logic import *

"""
PCEP 1.1 Understand fundamental terms and definitions
interpreting and the interpreter, compilation and the compiler, lexis, syntax and semantics
PCEP 1.2 Understand Python’s logic and structure
keywords, instructions, indenting, comments
PCEP 1.3 Introduce literals and variables into code and use different numeral systems
Boolean, integers, floating-point numbers, scientific notation, strings, binary, octal, decimal, and hexadecimal numeral system, variables, naming conventions, implementing PEP-8 recommendations
PCEP 1.4 Choose operators and data types adequate to the problem
numeric operators: ** * / % // + –, string operators: * +, assignments and shortcut operators, operators: unary and binary, priorities and binding, bitwise operators: ~ & ^ | << >>, Boolean operators: not and or, Boolean expressions, relational operators ( == != > >= < <= ), the accuracy of floating-point numbers, type casting
PCEP 1.5 Perform Input/Output console operations
print(), input() functions, sep= and end= keyword parameters, int() and float() functions
"""

questions = {
        
    'a1qa_interpreting_the_interpreter': {
        'question':'Which of the following statements about the python interpreter is PLACEHOLDER:',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'correct',
        'negative':'incorrect',
        'course_code':'1.1',
        'link':'',
        'incorrect':(
            'the interpreter translates source code into machine code only once and then never again',
            'the interpreter usually reads code from top to bottom and right to left',
            'the interpreter will inform you what caused an error but not which line it originated on',
            'the interpreter will inform you which line it originated on but not what caused an error ',
            'the interpreter will always detect errors at at the location of their exact cause',
            'the interpreter will execute all lines at the same time',
            'the interpreter checks if all lines are correct alphabetically, lexically and syntactically but not semantically',
            'the interpreter checks if all lines are correct alphabetically, lexically and semantically but not syntactically',
            'the interpreter checks if all lines are correct alphabetically, semantically and syntactically but not lexically',
            'the interpreter checks if all lines are correct semantically,syntactically and lexically but not  alphabetically',
            'the interpreter performs the \'read check execute\' cycle once',
            'the interpreter performs the \'read check execute\' cycle exactly once for every line in the source file',
            'a significant part of the source code may be exectuted successflly before the interpreter finds an error',
            'an interpreter doesn\'t execute any code until it has all been interpreted',
            'if there is an error in the code, the interpreter will not execute any of it',
            'the python interpreter is a compiler',
            'interpreted source code is ready to be distributed',
            ),
        'correct': (
            'the interpreter translates source code into machine code every time the code is run',
            'the interpreter usually reads code from top to bottom and left to right',
            'the interpreter will inform you where the error is and what caused it',
            'the interpreter may detect errors at some distance from their real causes',
            'the interpreter will execute line by line seperately',
            'the interpreter checks if all lines are correct alphabetically, lexically, syntactically and semantically',
            'the interpreter will inform you where the error is and what caused it',
            'The interpreter may detect errors at some distance form their real causes',
            'an interpreter will execute line by line seperately',
            'the interpreter performs the \'read check execute\' cycle repeated many times',
            'the interpreter performs the \'read check execute\' cycle more times than lines in source file',
            'a significant part of the source code may be exectuted successflly before the interpreter finds an error',
            'the python interpreter is not a compiler',
            'interpreted source code cannot just be distributed as the end user also needs an interpreter to execute it',
        ),
    },
    'a1qb_compilation_and_the_compilera1qb_compilation_and_the_compiler': {
        'question':'Which of the following statements about the python compilers and compilation are PLACEHOLDER:',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'correct',
        'negative':'incorrect',
        'course_code':'1.1',
        'link':'',
        'incorrect':(
            'the compiler executes source code whilst it is being translated into machine code',
            'the python interpreter is a compiler',
            'compiled source code is translated each time it is run',
            'modifications to source code automatically modify executed machine code',
            'compiled machine code is saved in the same file as its original source code',
            'a program which creates an executable file from source code is called an interpreter', 
            'if a compiler finds an error whilst compiling, it continues to the end of the file allowing partial executiong',
        ),
        'correct': (
            'the compiler translates source code into machine code before it is run',
            'the python interpreter is not a compiler',
            'compiled source code is translated once and can then be run multiple times',
            'source code must be compiled again each time source code is modufied',
            'compiling source code creates a new executable file',
            'a program which translates source code in machine code is called a compiler or translator', 
            'if a compiler finds an error whilst compiling, it ends translation straight away and gives an error message',
            'python is not a compiled language'     
        ),
    },


    'a1qc_machine_higher_level_natural_languages': {
        'question':'Which of the following statements about machine language, natural language and higher level coding languages are PLACEHOLDER:',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'correct',
        'negative':'incorrect',
        'course_code':'',
        'link':'',
        'incorrect':(
            'ILS stands for Intuitive Language Source',
            'machine languages are developed by computers',
            'natural languages are spoken between machines',
            'the rudimentary language understood by computers is known as source code',
            'the rudimentary language understood by computers is known as natural language',
            'a complete set of known commands in machine language is known as source code',
            'a complete set of known commands in machine language is known as natural language',
            'machine language is the same as native language',
            'machine language is the same as source code',
            'a natural language allows humans to use a language they can comprehend and that computers can understand',
            'higher level languages are more different to natural languages than machine language',
            'machine language allows humans to express commands to computers that are much more complex than those offered by source code',
            'machine language is called source code',
            'source code is another name for machine code exectuted by computers',
            'a file containing the source code is called the ILS',
            ),
        'correct': (
            'machine languages are developed by humans',
            'natural languages are spoken between humans',
            'the rudimentary language understood by computers is known as machine language',
            'a complete set of known commands in machine language is known as an instruction list',
            'machine language is different to native language',
            'a higher level coding language allows humans to use a language they can comprehend and that computers can understand',
            'higher level languages are more similar to natural languages than machine language',
            'they allow humans to express commands to computers that are much more complex than those offered by ILS',
            'a program written in a high-level language is called source code',
            'source code is different to machine code exectuted by computers',
            'a file containing the source code is called the source file',
            'ILS stands for Instruction List Set',
        ),
    },

    'a1qd_language_elements': {
        'question':'Which of the following statements about the elements of a language are PLACEHOLDER:',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'true',
        'negative':'false',
        'course_code':'1.1',
        'link':'',
        'incorrect':(
            'an alphabet is a set of words',
            'the instruction list is the alphabet of a machine language',
            'a syntax is a set of words which a language offers its users',
            'a lexis is a set of rules used to determine if a certain string of words form a valid sentence',
            'an instruction list is a set of rules determining if a certain phrase makes sense',
            'alphabetically a program needs to be written in lower case',
            'each programming language has its own alphabet',
            'the dictionary of a programming language is larger than an natural language',
            'each language has the same syntax',
            'as long as a program has correct lexis, it does not need to make semantic sense',
        ),
        'correct': (
            'an alphabet is a set of symbols used to build words',
            'the instruction list is the alphabet of a machine language',
            'a lexis is a set of words which a language offers its users',
            'a syntax is a set of rules  used to determine if a certain string of words form a valid sentence',
            'semantics are a set of rules determining if a certain phrase makes sense',
            'alphabetically a program needs to be written in a recognisable script',
            'lexically, a programming language has its own vocabulary',
            'programiming dictionary is smaller than an natural language',
            'each language has rules syntactically',
            'a program has to make semantic sense',
        ),
    },

    'a1qe_python': {
        'question':'Which of the following statements about the Python programming language are PLACEHOLDER:',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'true',
        'negative':'false',
        'course_code':'',
        'link':'',
        'incorrect':(
            'Python is a not a widely-used programming language',
            'Python is a not an object oriented programming language',
            'Python is a not an interpreted programming language',
            'Python is a not a high level programming language',
            'python does not have dynamic semantics',
            'python is used only for web development',
            'python is used only for data science',
            'python is used only in machine learning',
            'python is used only for teaching programming',
            'the name of the Python programming language comes from the snake', 
            'the Python programming language is named after the snake', 
            'Python is a compiled language',
            'Python is a machine language',
            'Python files have the extension .txt'
    ),
        'correct': (
            'Python is a widely-used, interpreted, object-oriented, and high-level programming language',
            'python has dynamic semantics',
            'python is used for general-purpose programming.',
            'the name of the Python programming language comes from an old BBC television comedy sketch series called Monty Python\'s Flying Circus', 
            'Python is an interpreted language',
            'Python is an object-oriented language',
            'Python is a high-level programming language',
            'Python files have the extension .py'    
        ),
    },

    'a1qf_python_keywords': {
        'question':'Which of the following is PLACEHOLDER a python keyword:',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'',
        'negative':'not',
        'course_code':'1.2',
        'link':'https://www.programiz.com/python-programming/keyword-list',
        'correct':(
            'False', 'await', 'else', 'import', 'pass','None', 'break', 'except', 'in', 'raise','True',
            'class', 'finally', 'is', 'return','and', 'continue', 'for', 'lambda', 'try','as', 'def',
            'from', 'nonlocal', 'while','assert', 'del', 'global', 'not', 'with','async', 'elif', 'if', 'or', 'yield'
        ),
        'incorrect': (
            'Incorrect', 'hold tight', 'but', 'findme', 'Nothing','Negative', 'stop', 'Maybe', 'Put', 'lift','Correct',
            'thing', 'eventually', 'could', 'dothis','plus', 'keepgoing', 'silly', 'beta', 'attempt','whilst', 'func',
            'apart', 'there', 'during','assume', 'delete', 'worldwide', 'never', 'ifandonlyif', 'assuming', 'alternatively', 'use'
        ),
    },



    'a1qg_indentation_and_spacing': {
        'question':'Which of the following statements about the Python programming language are PLACEHOLDER?',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'true',
        'negative':'false',
        'course_code':'1.2',
        'correct':(
            'if a line ends with a colon (:), the following line must be intented',
            'all lines in a block must have the same indentation',
            'if indentation level is not correct, the interpreter will highlight the indentation error and stop',
            'usually, tab is used for indentation',
            'indentation is mandatory in python'
        ),
        'incorrect': (
            'if a line ends with a semi colon (;), the following line must be intented',
            'if a line ends with a colon (:), the following line must be at the same level of indentation',
            'all lines in a block must have the same indentation as the previous block',
            'if indentation level is not correct, the interpreter will highlight the indentation error and continue to execute',
            'indentation has to be done by pressing space the right number of times',
        ),
    },

}
