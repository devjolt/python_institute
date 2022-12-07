# question ideas:
# class vs instance variables code outcomes

# magic method code outcome
"""
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


