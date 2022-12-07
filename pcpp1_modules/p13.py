from .p13_logic import *

questions = {
    'Gui Programming Concepts': {
        'question_with_0':'Which best refects the concept of PLACEHOLDER?',
        'question_with_1':'What is best described by the following: PLACEHOLDER?',
        'type':['make_items_question_from_pairs'],
        'course_code':'',
        'pairs':(
            ('visual programming', 'reflects the fact that an application\'s appearance is as important as its functionality'),
            (['a widget', 'a control'], "elements designed to recieve input"),
            ('focus', " the default recipient of some of all of the user\'s actions"),
            ('an icon', 'a small image representing an idea'),
            ('a label', 'an explanatory piece of text inside a window'),
            ('active', 'an element which is currently able to recieve user input'),
            ('traditional programmer paradigm', 'programmer must respond to all users actions'),
            (['a widget toolkit', 'a GUI toolkit', 'a UX library'], 'a set of uniform facilities to write code without worrying about portability'),
            ('Tkinter', ['a free, open source GUI Toolkit', 'developed since 1991', 'includes more than thirty universal widgets']),
            ('event driven programming', ['a paradigm in which the flow of the program is determined by events such as user actions','paradigm where entities (objects, services, and so on) communicate indirectly by sending messages to one another']),
        ),
        'fillers': ()
    },
    'Colours': {
        'question_with_0':['Which colour best describes:', '$PLACEHOLDER'],
        'question_with_1':'The colour PLACEHOLDER is best described by:',
        'type':'make_items_question_from_pairs',
        'course_code':'',
        'pairs':(
            ('$#FF0000', 'red'),
            ('$#00FF00', "green"),
            ('$#0000FF', "blue"),
            ('$#000000', 'white'),
            ('$#FFFFFF', 'black'),
            ('$#808080', 'grey'),
            ('$#FFFF00', 'yellow'),
            ('$#00FFFF', 'cyan'),
            ('$#FF00FF', 'magenta'),
            ('$#FFFF80', 'light red'),
            ('$#FF80FF', 'light green'),
            ('$#80FFFF', 'light blue'),
            ('$#008000', 'dark green'),
            ('$#800000', 'dark red'),
            ('$#000080', 'dark blue')
        ),
        'fillers': ()
    },

    'Starting a tkinter window': {
        'question':'Which of the following snippets is PLACEHOLDER ?',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'correct',
        'negative':'incorrect',
        'course_code':'',
        'correct':(
            '$import tkinter',
            '$import tkinter as tk',
            '$from tkinter import Button',
            '$from tkinter import *',
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
    'tkinter_window_coordinates':tkinter_window_coordinates,

    'Tkinter geometry manager options': {
        'question_with_0':'Which isPOSNEG a PLACEHOLDER option?',
        'question_with_1':'Which geometry manager has the option: PLACEHOLDER?',
        'positive_negative':('',' not'),
        'type':['posneg_pairs', 'new_pairs'],
        'course_code':'',
        'pairs':(
            ('pack()', ['expand', 'fill', 'side']),
            ('place()', ['anchor', 'bordermode', 'height', 'width', 'relheight', 'relwidth', 'relx', 'rely', 'x', 'y']),
            ('grid()', ['column', 'columnspan', 'ipadx', 'ipady', 'padx', 'pady', 'row', 'rowspan', 'sicky']),
        ),
        'fillers': (
            (['put()', 'add()', 'locate()'],['stick', 'xlocate', 'ylocate', 'xval', 'yval'])
        )
    },
    'tkinter_button':{
        'type':'code_block_question', 
        'valid':(
            (
                ('import tkinter', 'Import tkinter library'),
            ),
            (
                ('window = tkinter.Tk()', 'Create tkinter window object'),
            ),
            (
                ('window.title("my_window")', 'Add title to window'),
            ),
            (
                ('button = tkinter.Button(window, text="Bleep")', 'Create button object'),
            ),
            (
                (f"button.place(x={randint(1,10)*10}, y={randint(1,10)*10}{choice([', width=30', 'height=30',''])})", 'Position button 10 down and right of the top left corner of the window'),
                (f"button.pack({choice(['fill=tk.X','fill=tk.y',''])})", 'Place button in window'),
            ),
            (
                ('window.mainloop()', choice(['Window appears with a clickable','Window controller starts']))

            )
        ),
        'invalid':(
            (
                ('import tk', 'ModuleNotFoundError'),
                ('import Tk', 'ModuleNotFoundError'),
            ),
            (
                ('window = tkinter.tk()', "AttributeError: module 'tkinter' has no attribute 'tk'"),
                ('window = Tk.tkinter()', "NameError: name 'Tk' is not defined"),
            ),
            (
                ('window.maintitle("my_window")', "AttributeError: '_tkinter.tkapp' object has no attribute 'maintitle'"),
            ),
            (
                ('button = tk.Button(window, text="Bleep")', "NameError: name 'tk' is not defined"),
            ),
            (
                ('place(button, x=10, y=10)', "NameError: name 'place' is not defined"),
                (f"button.place({choice(['xval = 30','yval = 30', 'heigt = 30', 'length = 30',])})", "_tkinter.TclError: unknown option"),
            ),
            (
                ('window.run()', "AttributeError: '_tkinter.tkapp' object has no attribute 'run'"),
                ('window.loop()', "AttributeError: '_tkinter.tkapp' object has no attribute 'loop'")
            )
        ),
    }

}