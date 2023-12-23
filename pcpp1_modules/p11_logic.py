from random import randint, choice, shuffle

# question ideas:
# class vs instance variables code outcomes

# magic method code outcome
def object_types():
    code_options = {
        "Car":{
            "instance_name": "wheels",
            "str_var_name": "make",
            "str_var": choice(['Audi', 'Mercedes', 'Ford', 'Honda', 'Opel', 'Citroen', 'Maserati']),
            "int_var_name": "top_speed",
            "int_var": randint(10, 500)
            },
        "Dog":{
            "instance_name": "pooch",
            "str_var_name": "breed",
            "str_var": choice(['Poodle', 'Shitzu', 'Bulldog', 'Yorkshire Terrier', 'Spaniel', 'Retriever']),
            "int_var_name": "weight",
            "int_var": randint(10, 100)
            },
        "Person":{
            "instance_name": "homosapien",
            "str_var_name": "name",
            "str_var": choice(['Leslie', 'Ron', 'Terry', 'Rob', 'Sam', 'Rudager', 'Rasputin', 'Vlad', 'Bob', 'Chelsea', 'Jerry', 'Pat']),
            "int_var_name": "age",
            "int_var": randint(1, 99)
            },
    }

    subject = choice(list(code_options.keys()))
    subject_dict = code_options[subject]

    pairs = (
        ("<class 'type'>",f'print({subject}.__class__)'),
        (f"<class '__main__.{subject}'>",f'print({subject_dict["instance_name"]}.__class__)'),
        ("<class 'str'>",f'print({subject_dict["instance_name"]}.{subject_dict["str_var_name"]}.__class__)'),
        ("<class 'int'>",f'print({subject_dict["instance_name"]}.{subject_dict["int_var_name"]}.__class__)'),
        ("<class 'method'>",f'print({subject_dict["instance_name"]}.move.__class__)'),
    )

    pairs_l = [
        ["<class 'type'>",f'print({subject}.__class__)'],
        [f"<class '__main__.{subject}'>",f'print({subject_dict["instance_name"]}.__class__)'],
        ["<class 'str'>",f'print({subject_dict["instance_name"]}.{subject_dict["str_var_name"]}.__class__)'],
        ["<class 'int'>",f'print({subject_dict["instance_name"]}.{subject_dict["int_var_name"]}.__class__)'],
        ["<class 'method'>",f'print({subject_dict["instance_name"]}.move.__class__)'],
    ]

    code = f"""class {subject}:
    def __init__(self, {subject_dict["str_var_name"]}, {subject_dict["int_var_name"]}):
        self.{subject_dict["str_var_name"]} = {subject_dict["str_var_name"]}
        self.{subject_dict["int_var_name"]} = {subject_dict["int_var_name"]}

    def move(self):
        return print('going')

{subject_dict['instance_name']} = {subject}({subject_dict["str_var_name"]} = '{subject_dict["str_var"]}', {subject_dict["int_var_name"]}={subject_dict["int_var"]})\n"""

    pair = choice(pairs)
    if randint(0,1)==0: 
        question = f"Which line of code would you need to add to the code below to output:\n{pair[0]}"
        items = [{'code':pair[1], 'indicator':'correct', 'id':'item1'}]
        used, id = [pair[1]], 2
        while len(items)!=4:
            attempt = choice(pairs)
            if attempt[1] not in used:
                items.append({'code':attempt[1], 'indicator':'incorrect', 'id':f'item{id}'})
                used.append(attempt[1])
                id+=1

    else:
        question = "What would the output be from the following snippet?"
        code+= pair[1]
        items = [{'code':pair[0], 'indicator':'correct', 'id':'item1'}]
        used, id = [pair[0]], 2
        while len(items)!=4:
            attempt = choice(pairs)
            if attempt[0] not in used:
                items.append({'code':attempt[0], 'indicator':'incorrect', 'id':f'item{id}'})
                used.append(attempt[0])
                id+=1
    shuffle(items)
    return [{'text':question}, {'code':code}], items

def class_info():
    """
    # first three classes may have print info or not print info
    # final class inherits from two of previous classes


    # if first inheriting class is first, 
    result always
TypeError: Cannot create a consistent method resolution
order (MRO) for bases A, C

    else:
        if no inheriting classes have info, 
AttributeError: 'D' object has no attribute 'info'

else: 
    if first in list has info print that
    if second in list has info print that. 
    """
    numbers = []
    for x in range(4):
        number = randint(97, 122)
        while number in numbers:
            number = randint(97, 122)
        numbers.append(number)

    letters = []
    for x in range(4):
        letters.append(chr(numbers[x-1]-32))
    
    class_dict = {
        1:letters[0],
        2:letters[1],
        3:letters[2],
        4:letters[3],
    }
    info_dict = {
        letters[0]:'pass' if randint(0,1)==0 else f"def info(self):\n\tprint('Class {letters[0]}')",
        letters[1]:'pass' if randint(0,1)==0 else f"def info(self):\n\tprint('Class {letters[1]}')",
        letters[2]:'pass' if randint(0,1)==0 else f"def info(self):\n\tprint('Class {letters[2]}')",
    }

    inhertantce_letters = letters[:3]
    shuffle(inhertantce_letters)
    
    inheritance_dict = {
        1:inhertantce_letters[0],
        2:inhertantce_letters[1]
    }

    code = f"""
class {class_dict[1]}:
    {info_dict[class_dict[1]]}

class {class_dict[2]}({class_dict[1]}):
    {info_dict[class_dict[2]]}

class {class_dict[3]}({class_dict[1]}):
    {info_dict[class_dict[3]]}

class {class_dict[4]}({inheritance_dict[1]},{inheritance_dict[2]}):
    pass

{class_dict[4]}().info()"""

    if inheritance_dict[1] == class_dict[1]:
        correct = f"TypeError: Cannot create a consistent method resolution order (MRO) for bases {inheritance_dict[1]}, {inheritance_dict[2]}"
    elif (info_dict[inheritance_dict[1]] == 'pass') & (info_dict[inheritance_dict[2]] == 'pass'):
        correct = f"AttributeError: '{letters[3]}' object has no attribute 'info'"
    elif info_dict[inheritance_dict[1]] != 'pass':
        correct = f"class {inheritance_dict[1]}"
    elif info_dict[inheritance_dict[2]] != 'pass':
        correct = f"class {inheritance_dict[2]}"

    items = [{'code':correct, 'indicator':'correct', 'id':'item1'}]
    used = [correct]
    id = 2

    while len(items)!=4:
        option=randint(0,4)
        if option == 0:
            attempt = f"TypeError: Cannot create a consistent method resolution order (MRO) for bases {choice(list(class_dict.values()))}, {choice(list(class_dict.values()))}"
        elif option == 1:
            attempt = f"AttributeError: '{choice(letters)}' object has no attribute 'info'"
        else:
            attempt = f"class {choice(letters)}"
        
        if attempt not in used:
            items.append({'code':attempt, 'indicator':'incorrect', 'id':f'item{id}'})
            used.append(attempt)
            id+=1

    return [{'text':'What is the output from the following code?'},{'code':code}], items

def instance_vs_class_variables():
    """
    Question types:
    1. What line of code could be added to:
    2. What impact would the addition of the following line of code have?
    """
    code = """class A:
    var = "some_value"
 
a = A()
"""
    pairs = (
        ("change the value of the class variable","A.var = 'another_value'"), 
        ("create an instance variable","a.var = 'another_value'"),
        ("display the value of the class variable","print(A.var)"),
        ("create a new instance","b = A()"),
        ("create a new class variable","A.z = 'another_value'"),
        ("diplay an empty dictionary","print(a.__dict__)"),
        ("would show all attributes of the class","print(A.__dict__)"),
    )

    pair = choice(pairs)
    if randint(0,1)==0: # Which snippet would
        question = f"Which snippet would {pair[0]} in the following code:"
        if randint(0,3)==0: # correct answer is none of the above
            used = ["# None of the above", pair[1]]
        else:
            used = [pair[1]]
        incorrect = [item[1] for item in pairs if item not in used]
        
        items = [{'code':used[0], 'indicator':'correct', 'id':'item1'}]
        while len(items)!=4:
            item = choice(incorrect)
            if item in used:
                continue
            used.append(item)
            items.append({'code':item, 'indicator':'incorrect', 'id':f'item{len(items)+1}'})
    else:
        question = f"What would be the outcome of the following code?"
        code+=pair[1]
        if randint(0,3)==0: # correct answer is none of the above
            used = ["# None of the above", pair[0]]
        else:
            used = [pair[0]]
        incorrect = [item[0] for item in pairs if item not in used]
        
        items = [{'item':used[0], 'indicator':'correct', 'id':'item1'}]
        while len(items)!=4:
            item = choice(incorrect)
            if item in used:
                continue
            used.append(item)
            items.append({'item':item, 'indicator':'incorrect', 'id':f'item{len(items)+1}'})
    
    return [{'text':question},{'code':code}], items

"""
def abstract_classes_outcome():
    valid = (
        (
            'import abc',
            f"class BluePrint(abc.ABC):",
            '   @abc.abstractmethod',
            '   def hello(self):',
            '       pass',
            'class GreenField(BluePrint):',
            '   def hello(self):',
            '       print("Welcome to Green Field!")',
            'gf = GreenField()',
            'gf.hello()',
        ),
        'The code will execute without errors, a class using the abstract class'
    )
    invalid = (
        (
            (f'import {choice(["ABC", "abstractclass", "abstractbaseclass"])}','$ModuleNotFoundError'),
            (('import',),'$SyntaxError'),
            (('from abc import class',),'$ImportError'),
        ),(
            ((f"class BluePrint({choice(['abc.abc', 'ABC', 'abc.abstractclass'])}):"),'$NameError'),
            ((f"class BluePrint():",),'The code will execute without error, but BluePrint will not have acted as an abstract class'),
        ),(
            (('    @abc',),"$TypeError: 'module is not callable'"),
            (('    @ABC',),'$NameError'),
            (('    @abc.abstract',),'AttributeError'),   
        ),(
            (('    def hello(self)',),'$syntax error'),
        ),(
            (('',),'$syntax error'),
        ),(
            (('class GreenField(abc):',),'$TypeError'),
        ),
            (('    pass',),'$TypeError'),
    )
    
    items, code = ql.make_outcome_items_code(valid, invalid)
    question = [{'text':'What will be the outcome of the following code?'}]
    question.append({'code':code})
    return question, items 
"""

def class_methods():
    # outcomes
    # @classmethod included -> 
    # number_of_instances = randint(0, 3)
    # position
    # 
    # TypeError: Example.get_internal() missing 1 required positional argument: 'cls'
    # TypeError: Example.get_internal() missing 1 required positional argument: 'self'
    # NameError: name 'cls' is not defined
    code = """class Example:
        __internal_counter = 0

        def __init__(self, value):
            Example.__internal_counter +=1
    
    """
    """
    random_tf = (True, False)
    class_method = choice(random_tf)


        @classmethod
        def get_internal(cls):
            return f'# of objects: {cls.__internal_counter}'

    example1 = Example(10)
    example2 = Example(99)
    print(Example.get_internal())

    """


    pass


    """ 
# question ideas:
# class vs instance variables code outcomes

# magic method code outcome

class Person:
    def __init__(self, weight, age, salary):
        self.weight = weight
        self.age = age
        self.salary = salary
p1 = Person(30, 40, 50)
p2 = Person(35, 45, 55)

print(p1 + p2)

TypeError: unsupported operand type(s) for +: 'Person' and 'Person'

class Person:
    def __init__(self, weight, age, salary):
        self.weight = weight
        self.age = age
        self.salary = salary

    def __add__(self, other):
        return self.weight + other.weight


p1 = Person(30, 40, 50)
p2 = Person(35, 45, 55)

print(p1 + p2)
"""


def magic_method_arithmatic():
    """
    What is printed as a result of this code

    Types of outcomes:
    nothing: (no print statement, but everything else correct)
    value: (print statement and everything else correct)
    error: (no or incorrect method overridden)
    
    incorrect answers can be:
    any of the above, which the correct answer isn't
    incorrect arithmatic based on wrong magic method

    variables:
    [
        ({'category':'person', ['age', 'superpowers', 'salary']}),
        ({'category':'vehicle', ['age', 'speed', 'mass']}),
        ({'category':'dinosaur', ['size', 'roar', 'speed']}),
        ({'category':'book', ['pages', 'age', 'time_to_read']}),
    ]
    methods = ['add', 'sub', 'mult']

    pick correct answer and make question based on that. 
    pick:
    class name
    hence... instance variables
    pick first class variables * 3
    pick second class variables * 3

    pick chosen attribute (number 1,2 or 3)

    method

    parts of string:
    class_name_and_init
class {category}:
    def __init__(self, catvar1, catvar2, catvar3):
        self.catvar1 = catvar1
        self.catvar2 = catvar2
        self.catvar3 = catvar3

    override

    def __{method}__(self, other):
        return self.{chosen_attribute} + other.{chosen_attribute}

    instantiation
    {category[0]}1 = {category}(vals[0], vals[1], vals[2])
    {category[0]}2 = {category}(vals[3], vals[4], vals[5])

    print
    print(category[0]}1 + category[1]}2)

    if correct answer = no printout



    '''
    



    '''

    """

    


    methods = ['add', 'sub', 'mult']






#inheritance question
# outcome of code for inheritance
# method resolution order
"""
class A:
    def info(self):
        print('Class A')

class B(A):
    def info(self):
        print('Class B')

class C(A):
    def info(self):
        print('Class C')

class D(B, C):
    pass

D().info()



class A:
    def info(self):
        print('Class A')

class B(A):
    def info(self):
        print('Class B')

class C(A):
    def info(self):
        print('Class C')

class D(B, C):
    pass

D().info()
TypeError: Cannot create a consistent method resolution order (MRO) for bases A, C



class A:
    def info(self):
        print('Class A')

class B(A):
    def info(self):
        print('Class B')

class C(A):
    def info(self):
        print('Class C')

class D(B, C):
    pass

class E(C, B):
    pass

D().info()
E().info()
(behaving differently as a result of order of superclasses)


"""


#args and kwargs
"""
def combiner(a, b, *args, **kwargs):
    super_combiner(*args, **kwargs)

def super_combiner(*my_args, **my_kwargs):
    print('my_args:', my_args)
    print('my_kwargs', my_kwargs)

combiner(10, '20', 40, 60, 30, argument1=50, argument2='66')


def combiner(a, b, *args, c=20, **kwargs):
    super_combiner(c, *args, **kwargs)
def super_combiner(my_c, *my_args, **my_kwargs):
    print('my_args:', my_args)
    print('my_c:', my_c)
    print('my_kwargs', my_kwargs)
combiner(1, '1', 1, 1, c=2, argument1=1, argument2='1')

"""

# decorators
"""
used in
the validation of arguments;
the modification of arguments;
the modification of returned objects;
the measurement of execution time;
message logging;
thread synchronization;
code refactorization;
caching.

"""

# decorator accepting own attributes
"""
def warehouse_decorator(material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            print('<strong>*</strong> Wrapping items from {} with {}'.format(our_function.__name__, material))
            our_function(*args)
            print()
        return internal_wrapper
    return wrapper


@warehouse_decorator('kraft')
def pack_books(*args):
    print("We'll pack books:", args)


@warehouse_decorator('foil')
def pack_toys(*args):
    print("We'll pack toys:", args)


@warehouse_decorator('cardboard')
def pack_fruits(*args):
    print("We'll pack fruits:", args)


pack_books('Alice in Wonderland', 'Winnie the Pooh')
pack_toys('doll', 'car')
pack_fruits('plum', 'pear')
"""

# decorator stacking
"""
def big_container(collective_material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            our_function(*args)
            print('<strong>*</strong> The whole order would be packed with', collective_material)
            print()
        return internal_wrapper
    return wrapper

def warehouse_decorator(material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            our_function(*args)
            print('<strong>*</strong> Wrapping items from {} with {}'.format(our_function.__name__, material))
        return internal_wrapper
    return wrapper

@big_container('plain cardboard')
@warehouse_decorator('bubble foil')
def pack_books(*args):
    print("We'll pack books:", args)

@big_container('colourful cardboard')
@warehouse_decorator('foil')
def pack_toys(*args):
    print("We'll pack toys:", args)

@big_container('strong cardboard')
@warehouse_decorator('cardboard')
def pack_fruits(*args):
    print("We'll pack fruits:", args)


pack_books('Alice in Wonderland', 'Winnie the Pooh')
pack_toys('doll', 'car')
pack_fruits('plum', 'pear')

"""

#functions with classes
"""
class SimpleDecorator:
    def __init__(self, own_function):
        self.func = own_function

    def __call__(self, *args, **kwargs):
        print('"{}" was called with the following arguments'.format(self.func.__name__))
        print('\t{}\n\t{}\n'.format(args, kwargs))
        self.func(*args, **kwargs)
        print('Decorator is still operating')


@SimpleDecorator
def combiner(*args, **kwargs):
    print("\tHello from the decorated function; received arguments:", args, kwargs)


combiner('a', 'b', exec='yes')

"""

# class decorators

def question2():
    return ('Yep',), 'This be question2'


