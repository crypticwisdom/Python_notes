# Python Notes
Learn Python Programming Language from Basics to Advance.

```        
Note: This list should be learnt in this Order.
```

# Introduction to python. 

## What is python ?

Python is a high-level, interpreted programming language that was created by Guido van Rossum and first released in 1991. It is known for its simplicity and readability, which makes it an excellent choice for beginners and experienced programmers alike. Python emphasizes code readability by using indentation and a clean syntax, which reduces the need for complex braces and semicolons.

## Why python, What can python do ? 
Python is a versatile programming language that can be used for a wide range of applications. Here are some of the things Python can do:

- Web Development
- Data Analysis and Visualization.
- Machine Learning and Artificial Intelligence
- Scientific Computing
- Scripting and Automation
- Game Development
- Desktop GUI Applications
- Networking and Internet Protocols
- Scripting for Software and System Administration
- Education and Learning

These are just a few examples of what Python can do. 


# Python syntax
Python syntax refers to the set of rules and conventions that define the structure and formatting of Python code. Following the correct syntax is crucial for writing valid and executable Python programs. Here are some key aspects of Python syntax.

- Indentation
- Statements and Lines
- Comments
- Variables and Data Types
- Function Definitions

# Python comment
- Single Line Comment. #
- Multi-Line Comment. """ ... """

# Keywords
Python keywords, also known as reserved words, are words that have special meaning and predefined functionality in the Python language. These keywords cannot be used as identifiers (e.g., variable names or function names) because they are reserved for specific purposes within the language.

[False, class,  finally, is, return, None, continue, for, lambda, try, True, def, from, nonlocal, while, and, del, global, not, with
as, elif, if, or, yield, assert, else, import, pass, break, except, in, raise]

# Built-In Functions
Python provides a set of built-in functions that are available by default without the need for importing any modules. These functions cover a wide range of functionalities and are an integral part of the Python language. Here are some commonly used built-in functions in Python:

- Print: print() is used to output text or variables to the console.

- Type: type() is used to determine the type of an object.

- Len: len() returns the length or the number of elements in an object, such as a string, list, or tuple.

- Range: range() generates a sequence of numbers within a specified range.

- Input: input() is used to read user input from the console.


# Variable
Variable is used to store data to computer memory.

Syntax:
```Python
variable_name = "Variable Value"
```

# Data Types
Data types are the different categories in which data can be stored, handle and manipulated in python. These data types are objects.

- String(str)
- Integer(int)
- Boolean(bool): Either True or False.

- Float Point(float): Numbers with precisions. E.g 0.122, -2901.23.

- Complex Number(complex): Imaginary numbers. E.g: (89 + 9j).


# Basic Data Structures
These are forms in which 1 variable can hold more than 1 values.

- List: 
  - Used to hold sequence of values. 
  - It is ordered that is,  It stores it's element just the way they were entered in the list. 
  - It's elements can be changed.

- Tuple: 
  - Used to hold sequence of unique values. 
  - It is ordered that is,  It stores it's element just the way they were entered in the tuple.

- Set: 
  - Used to hold sequence of unique values. 
  - It is unordered that is,  It doesn't store it's element just the way they were entered in the set.

- Dictionary:
  - Used to hold key-value pairs.
  - It is unordered.

# Type Conversion
- This is the automatic conversion of data to specific type usually to a type that is bigger.
- The Python Interpreter handles Type conversions.
Example: integer to float.


# Type Casting
- Conversion from float to integer.
- Manual type conversion in Python. That is, a conversion the programmer does by him/her self.
- Mostly converting from bigger data type to smaller, but can be in any form.


# Operators
- Arithmetics Operator:
  - (+, -, /, *, %, **, //)
  - // -> It returns the number of times a number divides the certain number.
  - % -> It returns the remainder of a division.

- Assignment Operator:
  - (=, +=, -=, /=, //=, *=, **=, %=)

- Logical Operator:
  - (and, or)

- Comparison Operator:
  - (==, <, >, <=, >=)

- Identity Operator:
  - (is, is not)

- Membership Operator:
  - (in, not in)

- Bitwise Operators:
  - This haven't been studied.

- Conditions and Chained Conditions:
  - Condition refers to a statement or an expression that evaluates to either true or false. This uses conditional operators, e.g >, < ...
  
  - Chained conditions, also known as compound conditions or multiple conditions, refer to using multiple conditions together to create more complex logic in programming. This uses 'and' or 'or' logical operators.

## Operator Precedence: 
Operator precedence in Python defines the order in which operators are evaluated when multiple operators are present in a single expression.
Parentheses: Expressions enclosed in parentheses ( ) have the highest precedence. They are evaluated first, and the result is used in further calculations.

- Exponentiation: The exponentiation operator ** has the next highest precedence. It is used to raise a number to a power.

- Unary Operators: Unary operators like positive + and negative - sign have the next highest precedence. They are applied to a single operand.

- Multiplication, Division, and Modulo: Multiplication *, division /, and modulo % operators have the same precedence and are evaluated from left to right.

- Addition and Subtraction: Addition + and subtraction - operators have the same precedence and are evaluated from left to right.

- Bitwise Shifts: Bitwise shift operators << and >> have the same precedence and are evaluated from left to right.

- Bitwise AND, OR, XOR: Bitwise AND &, OR |, and XOR ^ operators have the same precedence and are evaluated from left to right.

- Comparison Operators: Comparison operators like <, >, <=, >=, ==, and != have the same precedence and are evaluated from left to right.

- Boolean Operators: Boolean operators and, or, and not have the lowest precedence among the logical operators.

It's important to note that within an expression, operators with higher precedence are evaluated before operators with lower precedence. If operators have the same precedence, their evaluation order is determined by their position from left to right.


# String Data Type
Sequence of characters stored within a single, double or triple quotes. E.g: 
```Python
'Cryptic Wisdom'
" Is a"
""" Python Programmer."""
```


## String Methods
String Methods are used to perform extram action on a string.

- .lower() -> "String".lower() => 'string".
- .upper()
- .capitalize()
...


# Integer Data Type
- Whole numbers without precisions. E.g 1, -1, -344, 122322.

## Integer Methods
- 


# Float Data Type
Numbers with precisions. E.g 0.122, -2901.23.


# Boolean Data Type
Either True or False.


# Complex Data Type
Imaginary numbers. E.g: (9j + 6).


# Control Flow
Control flow in Python refers to the order in which statements are executed in a program. It determines the flow or sequence of execution based on conditions and loops. Control flow allows you to control the path of execution and make decisions in your program based on certain criteria.

Python provides several control flow structures that enable you to control the execution of statements:

- Conditional Statements (if, elif, else):
```Python
    # Note: Only the block that meets the condition will run.
    if condition1:
        # code block executed if condition1 is true
    elif condition2:
        # code block executed if condition2 is true
    else:
        # code block executed if neither condition1 nor condition2 is true

```
- Tenary (Short hand if statement): 
```Python
variable = 'Statement to run if the condition is True' if  condition else 'Statement to run if condition is false'
```

- Loops (for, while): Loops allow you to repeatedly execute a block of code.

Structure of for and while loops:
```Python
    for item in iterable:
        # code block executed for each item in the iterable

    while condition:
        # code block executed as long as the condition is true
```

- Break and Continue: The 'break' statement is used to exit a loop prematurely, stopping the loop's execution. The 'continue' statement is used to skip the rest of the loop's code for the current iteration and move to the next iteration.

- Exception Handling (try, except, else, finally): Exception handling allows you to handle errors or exceptions that may occur during the execution of your program. The 'try' block contains the code that might raise an exception, and the 'except' block handles the exception if it occurs. The 'finally' block is used to specify code that should always be executed, whether an exception occurs or not.

```Python
    try:
    # code that might raise an exception
    except ExceptionType:
        # code executed if the specified exception occurs
    else:
        # code to be executed if there was no exception but if there was an error, this block won't run.
    finally:
        # code executed regardless of whether an exception occurs or not
```


# Iterable and Iterator
Iterables is an object that can be looped over.
- list
- tuple
- dictionary
- set
- files
- generators

Any object with __iter__() method, means that object can be looped over / is an      iterable.

- Iterator: is an object with a state so that it remembers where it is during iteration, they know how to get their next value with the __next__() which is one of the magic methods of an Iterator | next() which is a built-in function that calls the '__next__()' method.

- iter(iterable) -> returns an iterator object which we can then use the 'next()' to get the next element in the sequence, and once each element has been accessed, it is then lost or removed from the state. When the iterator is exhausted i.e when we have accessed all of it's element, and we try to access an element again from it, a 'StopIteration' Exception will be thrown

## Loops
for i in range(x):
    print(i)
    if i == 3:
        break 
    else:
        continue


counter = 0
while counter == 90:
    if counter == 34:
        break
    else:
        continue


# Functions and Lambda (Anonymous Function):
A function is used to group a block of code.

Syntax:
```Python
    # Function definition
    def function_name(parameter1, parameter2, *args, **kwargs):
        # Block of code to run.
        
        # *args is used to hold values in a tuple.

        # kwargs is used to hold key-value pairs

        return value_to_return 


    # Function invokation
    function_name(argument1m argument2)
```

## Lambda Function (Anonymous Function)
- Lambda functions are functions without name and are written with the 'lambda' keyword.

Syntax:
```Python
    # Lambda function definition
    func = lambda parameter1, parameter2: parameter1 * parameter2

    # Invokation
    func(parameter1, parameter2)
```

# Python List
 a list is a versatile and commonly used data structure that allows you to store and manipulate a collection of items. Lists are mutable, meaning you can add, remove, or modify elements within them. 

- Create a List:
 ```Python
    container1, container2 = [1,2], list(1,2)
 ```

- Accessing List Elements:
```Python
    print(container1[0]) => 1
```

- Modifying List Elements:
```Python
    container1[1] = 332
```

- List Operations:
  - Concatenation (+): Adding 2 or more list objects together.
    ```Python 
       a, b = [2,4,5], [43,65]
       print(a + b) => [2,4,5,43,65]
    ```
  - Repition (*): Repeat a list a certain number of times.
    ```Python 
       a = [2,4,5]
       print(a * 3) => [2, 4, 5, 2, 4, 5, 2, 4, 5]
    ```
  - Slicing (:): Use slicing to extract a portion of a list. It allows you to specify a range of indices to retrieve a sublist.
    ```Python 
       a = [2, 4, 5, 3]
       print(a[:2]) => [2, 4, 5]
    ```

## List Methods:
- append(): Adds an element to the end of the list.
- extend(): Appends elements from an iterable to the end of the list.
- insert(): Inserts an element at a specific index.
- remove(): Removes the first occurrence of a specified element.
- pop(): Removes and returns the element at a specific index, or the last element if no index is specified.
- index(): Returns the index of the first occurrence of a specified element.
- count(): Returns the number of occurrences of a specified element in the list.
- sort(): Sorts the elements of the list in ascending order.-
- reverse(): Reverses the order of the elements in the list. a[::-1]
- copy(): Returns a shallow copy of the list.
- clear(): Removes all elements from the list.

To see a complete list of methods available for a any Python object, you can use the dir() function or access the Python documentation. 

### Sort a list in Place:
The list.sort() method sorts the original list in place. It means that the sort() method modifies the order of elements in the list.

```Python
    data_set = [2, 3, 5, 4, 1]
    data_set.list()
    print(data_set) => [1, 2, 3, 4, 5]

    data_set2 = [2, 4, 3, 1]
    data_set2.list(reverse=True)
    print(data_set2) => [4, 3, 2, 1]

```

- By default, the sort() method sorts the elements of a list using the less-than operator (<). In other words, it places the lower elements before the higher ones.
- If a list contains strings, the sort() method sorts the string elements alphabetically.
```Python

    guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']
    guests.sort(reverse=True)
    print(guests) => ['James', 'Jennifer', 'John', 'Mary', 'Patricia', 'Robert']

```

```Python
    # Sort the companies revenue from smallest to the highest
    companies = [('Google', 2019, 134.81),
             ('Apple', 2019, 260.2),
             ('Facebook', 2019, 70.7)]
    

    companies.sort(key=lambda container: container[2])
    print(companies) => [('Apple', 2019, 260.2), ('Google', 2019, 134.81), ('Facebook', 2019, 70.7)]

```

## Python sorted() built-in function
- The Python sorted() function is used to sort iterables.
- This works same as the .sort() method, but the sorted() built-in function returns a new list object.
- To return the new sorted list from the original list, you use the sorted() function.

## Python slicing:
Lists support the slice notation that allows you to get a sublist from a list:

Syntax:
```Python
    # list_[begin: end: step]

    container = [21,45,76]
    print(container[0: 1: 1]) # => [21, 45, 76]
```


## Python List Unpacking (sequence unpacking):
Basically, you can assign elements of a list (and also a tuple) to multiple variables. For example:
```Python
    colors = ['red', 'blue', 'green']
    red, blue, green = colors
```
This statement assigns the first, second, and third elements of the colors list to the red, blue, and green variables.

__An error occurs when the number of variable is less than the element in the sequence on the right hand side__
```Python
    colors = ['red', 'blue', 'green']
    red, blue = colors
```
Error:
```Python 
    ValueError: too many values to unpack (expected 2)
```


## Unpacking and packing:
If you want to unpack the first few elements of a list and don’t care about the other elements, you can:

- First, unpack the needed elements to variables.
- Second, pack the leftover elements into a new list and assign it to another variable.
By putting the asterisk (*) in front of a variable name, you’ll pack the leftover elements into a list and assign them to a variable. For example:

```Python
   colors = ['red', 'blue', 'green']
    red, blue, *other = colors

    print(red, blue, other)

    # Result: red blue ['green']
```

## List Comprehension
```Python
    colors = ['red', 'blue', 'green']
    red = [item for item in colors if item == "red"]

    print(red)
    # Result: ['red']
```

## map(), filter(), reduce()
The map(), filter() and reduce can be used on any Iterable object.
- map(function, iterable): This is used to perform a function on every item of an iterable passed to it, it/to return a new iterator object An object that has the ''''__next__()''' method. Works on all python iterable. 

```Python 
   container = [2, 3, 4]
   calculation_response = map(lambda x: x**2, container)
   # The above statement yeilds an iterator object"<map object at 0x10bf88670>".

   # Convert the iterator to a list
   print(list(calculation_response)) => # [4, 9, 16]
```


- filter(function, iterable) built-in function -> Use the Python filter(fn, iterable) function to filter an Iterable. The  function "fn()" is ran on every element on the iterable and returns 'True' where any element meets the condition. A new iterator object is returned after using filter object.

```Python 
   container = [2, 3, 4]
   calculation_response = filter(lambda x: x**2 == 16, container)
   # The above statement yeilds an iterator object "<filter object at 0x10bf88670>".

   # Convert the iterator to a list
   print(list(calculation_response)) => # [4]
```

- reduce(function, iterable): This is not a built-in function instead it is import from the standard python library. It is used to reduce an iterable to a single value. Example: 

```Python
    from functools import reduce 

    container = [1, 2, 4, 3]
    summer = reduce(lambda x, y: x + y, container)
    # 1 + 2 = 3,
    # 3 + 4 = 7, 
    # 7 + 3 = 10.
    print(summer) # => 10
```

# Tuple Data Structure.
 a tuple is an ordered, immutable collection of elements enclosed in parentheses ().

Creating a Tuple:
To create a tuple, you can enclose elements within parentheses () and separate them with commas. Alternatively, you can create a tuple without using parentheses by simply separating the elements with commas.

```Python
    # Method 1
    my_tuple = (1, 2, 3)
    
    # Method 2
    my_tuple = 1, 2, 3

```

## Accessing Tuple

```Python
    print(my_tuple[0])     # Output: 1
    print(my_tuple[2])     # Output: 3
```

## Tuple Unpacking

```Python
    my_tuple = 1, 2, 3  # Tuple packing: Packing all values to 1 variable name.
    a, b, c = my_tuple  # Tuple unpacking: Spreading values to different variable names.
    print(a, b, c)     # Output: 1 2 3
```

## Tuple Operations
- Concatenation (+): Adding 2 or more tuples together.
```Python
    (1,2,3) + (4, 5, 6) # => (1, 2, 3, 4, 5, 6)
```
- Repetition (*):


## Tuple Methods:
Tuples have a few built-in methods available:

- count(): Returns the number of occurrences of a specified element in the tuple.
- index(): Returns the index of the first occurrence of a specified element in the tuple.


# Dictionary Data Structure


# Set Data Structure





















# General Informations

# Garbage Collection:
When the del keyword is used to delete an object, the interpreter simply, unbinds the object from the variable or removes the variable name from the corresponding namespace. The object however continues to exist in memory and if no other variable name is bound to it, it is later automatically destroyed.
This automatic destruction of unreferenced objects in python is called garbage collection.
Garbage collection is the destruction of unreferenced objects in python.
