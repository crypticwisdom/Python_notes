'''
    This is a python module for testing and learning python syntax.
    - Statements and Keywords, Variables, Variables assignments(unpacking, multiple variables to 1 Literal, multiple variables to more than 1 Literal).
    - Comment (single line comments, multi-line comments, Documentation String.
        used to document a function, method, class, or module, used immediately after defining any of them.
        using a single-tripple quotes '''''' or """ doc """)
    - Line Continuation using backslash(\). Direct Line Continuation and Indirect Line Continuation using (), {}.
    - Multi Line Statements in a single line.
    - Data Types and Data Structures.
    - Type conversions. (Implicit and Explicit Type conversion): converting the value of one data type to another.
'''

if __name__ == '__main__':
    # print("wisdom it will all be fine")
    name = 'wisdom'
    age = 21
    # print("asdas", type(age))
    # print(type(age), type(bin(age)), bin(age))

    # print(int("0o234", 8))

    # multi-line statement.
    '''
        This is a comment, a multi line comment.
    '''

    # lines = ( 1 + 3 +\
    #     2 + 23
    #     + 3
    # )

    # """
    #     wisdom
    # """

    # unpacking
    # a = 3, 3, 4, "tuple"
    # a,b, *others = a
    # print(a, b, others)

    # multi line statements
    # print("kindness"); a = 4; b= 5; c=4; print("wisdom", a, b, c) if True else print("i am waiting for response..."); print('at the end...')

    def do(*args, **kwargs):
        """
            This is a documentation string.
            This is simply a string literal that is used for documenting a function, method, class or module after defining them.
            A document string is used for multiline commenting in python.
            You can access the documentation string of a class, method, function or module, with the __doc__ attribute.
        """
        print(args, kwargs)
        print("this")


    """ print(__name__.__doc__)
        print(do)
    """

    '''# Variables, multiple values to multiple variables.(unpacking)'''

    # a = 1,2
    # print(type(a))
    

    # d = e = f = None

    # d = None; e = None ; f = None 
    # print(f)

    # n = 76j + 2

    # print(isinstance(n, complex))

    # num = '2.00'

    # print(type(float(num)))

    # Python has 5 data types and 4 data structures.
    """
    Data types: (int, str, float, complex, boolean).
    Data Structures: 

        1. Sequences(List and Tuple): This is a data structure that can be accessed indexly or the items, 
        are next to each other in memory, just the way they were assigned.

        2. Collections (Set and Dictionary): these are data structure that are not next to each other in memory.
    """
# print('wisdom ', 7, sep="...", end='|')


"""
    import sys
    print(id(76))

    print(sys.path) when we import a module or package, python checks the sys.path for the it first.
"""
'''
    we use print() function to output data, we can specify where to output the data by specifying it with the file kwarg.
    we use input() function to input data.
'''

'''
Operators:
    These are special symbols used to perform arithemetic and logical operations on operands.
    Arithemetic Operators:  +, -, **, *, /, // for mathematical computations.
    Comparison Operators: Used to compare values, it return either True or False.(<, >, ==, <=, >=).
    Logical Operators: These are python keywords that are used for comparisons. (and, or, is, not).
    Bitwise Operators: 
    Assignment Operators: Used to assign or bind a value to a variable.
    Special Operators: Identity and Membership Operators.
        Identity Operators: use to check if the both operands, values or variable are located on the same part of the memory.
        (is, is not)
        on the same part of the memory and identical. This simply checks if values  are equal in identity
        6 is 6 because they are equal and also has equal data types and in memory(is, is not).

        Membership Operators: This is used to check if a value is in a data structure or string. (in)
'''
# x='7'; y=7  #are different == False
# print(x is y)


# y = 5; i = 3
# y &= 2
# print(y)
# print('i' is 'wisdom')


'''
Namespace and Scope.

Name means Identifier, an identifier is a name given to any entity like, variable, function name, class name, keywords, 
these are all identifiers. And an identifier is a way to access the associated object.

Namespace contains the mapping of identifiers or names to their defined objects.
" In python, you can imagine a namespace as a mapping of every name you have defined to corresponding objects. "

Built-in namespace is a namespace that is created when the python interprter is ran and exists as long as the interpreter
runs, it contains all the built-in names or identifiers built in python. That is why built in functions and classes are
available for us to use from anywhere in our program.
Identifiers or names in the builtin namespace can be accessed from anywhere in our program.

Global Namespace, this is a namespace that contains all the names or identifiers that are created or defined in our module.
Each Module creates its own global namespace.
These diff. namespcaes are isolated. Hence, the same name that may exist in diff. modules does not collides.

Local Namespaces these are spcaes that holds identifiers/names that are defined inside a function or class.
Modules can have various functions and classes. A local namespace is created when a function/class is called, which has all
the names defined in it. similarly is the case with classes.

Different namespaces can co-exist at a given time but are completely isolated.

'''
"""
    import this

    print(this.c)
"""

# a=2
# print(id(a))
# print(id(2))

# a = a+8

# print(id(a))
# b = 2
# print(id(b))

"""
A Scope is a portion of a program from where a namespace can be accessed directly without any prefix.

"""

a = 100
# here in the global scope( which contains the built-in and the global namespaces),
# we can access the built-in and global namespaces but, not any local or nested local namespaces.
def hello():
    """
        over here we can access built-in, globals and local namespaces but, we can't change 
        the values of the built-in and global names/identifier instead we end up creating new names/identifiers 
        that will now be among the local name space.

    """
    a = 67
    print("local scope:", a)
    def hi():
        """
            over here we can access all namespaces but, we can't make changes to the built-in, global and the parent local
            namespace, which is the hello function namespace.
            This has a co-existing/nested-local namespace.

            The only way we can make changes to the global namespaces inside of this co-existing or parent local namespaces,
            is by using the "global" keyword to tell the python interpreter that we are referring to the global namespace.

            To access and be able to make changes to the parent local namespace we need to use the keyword "nonlocal".
        """
        nonlocal a
        a = 9
        
        print("co-existing local scope:", a)
    hi()

print(hello())

print("Global Scope:", a)

'''
    When we call on an identifier, python interpreter checks from the present scope namespace to the higher scope namespaces.

'''

'''
    Python Control Flow:
    if...elif...else: only if the test_expression evaluates to True then will the if block be run else, the elif, else,
    the else block will be finally ran. (for making decisions). 

    Note: Only one block of code is ran in the ..if..elif..else.. statement.

    for loop( used in looping or iterating over an iterable(objects that can be looped over or travresed))
        - sequence are objects that are in order in memory, just the way they are defined, they stay and can be accessed,
        that way.
        (Iterating over a sequence is called Traversal).

    for..else : the else block is only executed when the for..block has finished executing. Indentation is used to mark,
    block of codes in the python control flow.

    while loop: While loop is used to iterate when, we don't know the number of times we need to iterate beforehand.
    If the test exprepssion evaluates to True then, the while block will be ran, and it is important to always increment the 
    counter n+=1.

    while...else: is same as the for..else statement, if only the test_expression evaluates to False or if the while block
    has completed it process then, will the else block be ran.

    Continue and Break Statement(Keywords): these keywords are used in a For or While Loop.
    Continue keyword : This is used to return to the while/for loop statement, without executing the code after it.
    in a while loop or for loop ...if n == 3: \n continue \n print(324)
    Once the if statement is True on a certain iteration, the interpreter comes across the Continue keyword,
    it will immediately restart the iteration.

    Break keyword : This is used to exit from while/for loop statement, without executing the code after it and also the else
    block, if defined.
    in a while loop or for loop ...if n == 3: \n Break \n print(324)
    One the if statement is True on a certain iteration, the interpreter comes across the Break keyword,
    it will immediately exit the entire loop block of code.

    Pass Statement (Keyword): This is a null statement. while comments are ignore by interpreters, this statement is not ignored but does
    nothing, No Operation (NOP). Pass is just a plcaholder for functionality to be added later. 

'''

n = 0
secret = 1


# for i in range(3):
#     inp = int(input("Enter a value 0-9: "))
#     if inp == secret:
#         print("You won")
#         break
#     else:
#         print("Keep it up")
#         continue    
# else:
#     print("we are done..", flush=True)

# while n < 2:
#     inp = int(input("Enter a value 0-9: "))
#     if inp == secret:
#         print("You won")
#         break
#     else:
#         print("Keep it up")
#         n += 1
# else:
#     print("Trying else statement...")

# for i in {4, 5}:
#     print(i)

"""
    Function : This is an entity that performs a certain task.
    Function header: This is the part that carries the function definition keyword, function identity, and the parameters.
    Document String: Used for documenting or tellin about the function. 
    Function body: This is the main part of the code that contains statements and expression for the entity.
    Scope of a variable is the portion of the program where the variable can be recognized.
    Life time of a variable is the period throughout which the variable exist in memory.
    Types of Function: Built in function and Custom Function/user defined function.


    Positinal Arguments: These are arguments that are called with a function in the same position it was defined as a Parameter.
    Arguments: These are values that are passed when calling a function.
    Parameters: These are variable or placeholder that are used in function definition.
    Default Parameters: These are parameters that are given a value during function definition.
    
    Keyword Argument: These type of aruments are used with a variable name and value when calling a function.
    Function Arbitrary Arguments: sometimes we don't know in advance the number of arguments that will be passed into a
    function. python allows us to handle this kind of situation through function calls with an arbitrary number of argument.
    In the function definition, we use an asterisk(*) before the parameter name to denote this kind of argument.

    return keyword: This is a keyword that is used to return a value from a function or to exit a function block.

    Function Recursion: a function is said to be recursive when it is used in it self.

    Lambda function is a one line function. It does not need an identifier. It also does not use the def or return keyword.
    A lambda function is also known as an Anonymous function.
    example ( num = lambda param, param2 : "yes" if param > param2 else "nope" )
    num(2, 3)
    A lambda function can be used where a function is required as an argument. map(), filter(), functools.reduce()

    Map function: this is used to apply the same function to items in a sequence.
    if two sequences are passed as argument in this function, it simply applies the lambda/custom function on each item
    of the 2 or more sequences specified.

    it needs / require it first argument which is a lambda or def function and a second are arbitrary argument would be a sequence.
    Stops when the shortest iterable is exhausted.
    It simply applies the same function to all the items in a sequence, the returns an iterator object which can be converted
    to a list.

    Filter function : This is used to filter a set of items that does not reach the specified condition in a function.
    The filter function takes in only 2 arguments, the lambda function and also the iterable.

    Reduce function : Apply a function of two arguments cumulatively to the items of a sequence or iterable, from left to right,
     so as to reduce the iterable to a single value. For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) 
     calculates ((((1+2)+3)+4)+5). If initial is present, it is placed before the items of the iterable in the calculation, and serves as a default when the iterable is empty.


"""
lo = [1,2,3,4,5]

print(list(filter(lambda x:x > 3, lo )))


# def hello(*args, **kwargs):
#     f = [ i.upper() for i in args ]
#     for i in kwargs.items():
#         k, v = i
#         print(k, v) 
#     return f


# print(hello('wisdom', "Hi how are you doing", name="wisdom", surname="nwachukwu"))

greet = lambda x : print("Hello" + x)
#  find the total of 1 or 2 or more sequence 
l1 = [2, 3, 5, 6, 7, 0]
l2 = [2, 1, 5, 7, 8]

print(list(filter(lambda x: bool(x) , l1)))
# def mu(l, m):
#     a = list(l) + list(m)
#     su = 0
#     for i in a:
#         su += i
#     return su

# def mu(l, m):
#     print('s')
#     return l * m
# lambda
# mu = lambda x, y : sum(x) + sum(y) 

#  map function

# print(list(map(mu, l1, l2)))
# print(mu(l1, l2))

# print(list(map(lambda x : x % 2, l1)))
# k = ' wisdom '.join(['i', 'am', 'Here'])

# print(list(map(lambda x : x.capitalize() if x is not ' ' else 'b', k)))

# print(list(filter(lambda x: x == 9, l1)))

# import functools

# print(list(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])))

# print([ y + x for y in ['a', 'c'] for x in ['s', 'k']])

# v = ['a', 'c']; k = ['s', 'k']

# p = []

# for i in v:
#     for l in k:
#         p.append(i + l)
#     p.append(i + l)
# print(p)

"""
    Data Types:
    Number : integer, float, decimal, complex ...
    List: mutable data type, items can be modified and deleted. |list comprehension| reminder->[ x+y for x in [''] for y in ['']]
    Tuple : immutable data-types, items cannot be modified once created.
    String : immutable data type, items cannot be modified. |format() method, format specification, they separated by ":" inside
    the placeholder ->{}. e.g "this is |{0:<10}|".format('wisdom')
    Dictionary: key value pair. Dictionary comprehension.
    Set: this holds only unique value.
    frozenset: immuatable set.

    Diction Comprehension: this is an elegant way of creating a dictionary object from an iterable.
    It consist of an expression pair (key:value) followed by a for statement inside a curly braces. it optionally can
    take an if stmt and also more for loop stmt.

"""

print({f"k:{x}": x*2 for x in range(3)})

# print("this is {:e} {} {}".format(9, 'as', 'sas'))
# o = frozenset([1,2,3,4])
# print('o.__doc__)

