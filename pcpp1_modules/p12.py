from random import choice, randint, shuffle
from .p12_logic import *


questions = {
    'peps': {
        'question_with_0':'Which best describes PLACEHOLDER?',
        'question_with_1':['Which PEP is best described by the following:', 'PLACEHOLDER'],
        'type':['make_items_question_from_pairs'],
        'course_code':'',
        'pairs':(
            ('PEP 1', ['contains PEP templates','contains PEP formats','contains PEP submission process',f'details the submission process for {choice(["reporting bugs", "updates"])}', f'details the {choice(["review","resolution","maintenance"])} stages after submissions are made','PEP purpose and guidelines', 'provides information about purpose of PEPs', 'provides information about types of PEPs']),
            ('PEP 8', ("style guide for python code","gives python conventions", "presents best practices for Python coding")),
            ('PEP 20', ("Zen of Python","presents a list of principles for Python's design")),
            ('PEP 257', ('docstring conventions', "guidelines for conventions associated with Python docstrings","guidelines for semantics associated with Python docstrings")),
            ('a standards track PEP', ('describes new langauge features', "describes implementations")),
            ('a informational PEP', ('describes python design issues', "provides guidelines to the python community","provide information to the python community")),
            ('a process PEP', ('describes processes which revolve around python', "proposes changes","provides recommendations", "specifies certain procedures")),
        ),
        'fillers': (
            ('PEP 2', ['Function purpose and guidelines', 'provides information about purpose of objects', 'provides information about types of objects']),
            (f'PEP {randint(3,19)}', ("licenses for python code","gives web-development conventions", "presents non-negotiable rules for Python coding")),
            (f'PEP {randint(20,256)}', ("Law of Python","presents a list of mandates for Python's design")),
            ('PEP 0', ('docstring conventions', "guidelines for conventions associated with Python docstrings","guidelines for semantics associated with Python docstrings")),
        )
    },
    'people_involved': {
        'question_with_0':'Which best describes PLACEHOLDER?',
        'question_with_1':['Which participant  is best described by the following:', 'PLACEHOLDER'],
        'type':['make_items_question_from_pairs'],
        'course_code':'',
        'pairs':(
            ("Python's Steering Council", ['composed of five people','final authorities in accepting or rejecting PEPs']),
            ("Python's Core Developers", ("group of volunteers who manage python")),
            ("Python's BFDF", ("Guido van Rossum", "the original creator of Python")),
        ),
        'fillers': (
        )
    },
    'zen_of_python': {
        'question_with_0':'Which best describes PLACEHOLDER?',
        'question_with_1':['Which participant  is best described by the following:', 'PLACEHOLDER'],
        'type':['make_items_question_from_pairs'],
        'course_code':'',
        'pairs':(
            ("Beautiful is better than ugly", ['readability is important','79-character maximum line length', 'variable naming conventions', 'placing statements on seperate lines']),
            ("Explicit is better than implicit", ("importing specific modules is preferable to use of *", f"${choice(['bananas','applies','oranges'])}({randint(1,10)},{randint(1,10)}) #z argument names could be named)")),
            ("Simple is better than complex", ("generally, a minimalist approach wins","use fewer lines of code if that's possible","divide problems into smaller, simpler parts")),
            ("Complex is better than complicated", ("simplicity carries limitations","code should not be difficult to understand even if consisting of many elements","avoid  misunderstanding, lack of clarity and miscomprehension")),
            ("Flat is better than nested", ("three levels deep is enough","more than three deep is a warning sign","flat code is easier to maintain", "should be balanced with writing sparse code")),
            ("Sparse is better than dense", ("don't write too much code on one line","should be balanced with implementing flat code and reducing nesting")),
            ("Readability counts", ("the essence of the python philosophy","code is read more often than it is written")),
            ("Special cases aren't special enough to break the rules", ("ensure backward compatability","time pressure or complexity should not be an excuse", "discipline, consistency andcompliance with standards and conventions")),
            ("Practicality beats purity", ("obeying rules should not prevent you from writing better code","rules can be broken if benefits outweigh negative impact")),
            ("Errors should never pass silently -s unless explicitly silenced", ("Knowing why code fails is important")),
            ("In the face of ambiguity, refuse the temptation to guess", ("testing allows you to save time", "avoid writing ambiguous code","self commenting names","leave comments","have limited trust in your code")),
            ("There should be one - and preferably only one - obvious way to do it", ("agree the best way to achieve a particular goal")),
            (("Now is better than never","Although never is often better than right nows"), ("perfect is the enemy of good","faster is the enemy of slower","acting sooner is better than later","Python allows quick translation of ideas into working code")),
            (("If the implementation is hard to explaain, it's a bad idea","If the implementation is easy to explain, it may be a good idea"), ("everything which can be explained in words can be translated into code","being able to describe what your code does means that non experts can comment on it","acting sooner is better than later")),
            ("Namespaces are one honking great idea - let's do more of those", ("avoid conflicts with already existing object across different scopes","use these to make code clearer and more readable")),


        ),
        'fillers': (
        )
    },'hobgoblin': {
        'question':'Which of the following snippets is PLACEHOLDER ?',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'correct',
        'negative':'incorrect',
        'course_code':'',
        'correct':(
            'a foolish consistency is the hobgoblin of little minds',
            'PEP 8 is still evolving',
            'some conventions in PEP 8 have been identified as obsolete',
            'some conventions in PEP 8 are now discouraged',
            '$from tkinter import Button',
            '$window = tkinter.Tk()',
            '$window.title(\'window title\')',
            '$window.mainloop()',
            
        ),
        'incorrect': (
            '$import tk',
            '$import Tkinter as tk',
            '$import Tkinter',
            '$import tk as tkinter',
            '$window = tkinter.tk()',
            '$window = tk()',
            '$window = tkinter()',
            '$window.title = \'window title\'',
            '$tk.title(\'window title\')',
            '$tkinter.title(\'window title\')',
            '$tk.windowtitle(\'window title\')',
            '$tkinter.windowtitle(\'window title\')', 
            '$window.loop()',
            '$tkinter.mainloop()',
            '$window = mainloop()',
        ),
    },
    
    

}