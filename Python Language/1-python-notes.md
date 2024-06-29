# Python Notes

Learn Python Programming Language from it's Basic to Advance Level.

```
Note: This list should be learnt in this Order.
```

# Introduction to python.

## What is Python ?

Python is a high-level, interpreted programming language that was created by Guido van Rossum and first released in 1991. It is known for its simplicity and readability, which makes it an excellent choice for beginners and experienced programmers alike. Python emphasizes code readability by using indentation and a clean syntax, which reduces the need for complex braces and semicolons.

- we need to download a translation service, The Python Interpreter, from the official website. The translation service (Python interpreter is written in C) but it also has many forms like Jython (a python translation service built in java ).
- The C-Python downloaded from python official website comes with the interpreter and also C-Python VM.
- when code is written in a python script (.py) and ran, it goes to the python interpreter, the interpreter converts it to byte code, then passes the bytes to C-Python's VM (Virtual Machine), which runs the code on our devices.
- Why so many Languages ?: Different programming languages are good for building different tools.
- Python strength is in Scripting. Every language has it's pros and cons.
- Then bin() function is used to return the binary number for any number.
- convert a binary back to base 10 using int('0b101', 2).
- The whole point of writing a code is to make it readable.
- python - print, math, data types (int, float)
- operator precendence. (), \*_, _, ...

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

[False, class, finally, is, return, None, continue, for, lambda, try, True, def, from, nonlocal, while, and, del, global, not, with
as, elif, if, or, yield, assert, else, import, pass, break, except, in, raise]

- An expression is a piece of code that produce a value.
- A statement is an entire line of code.

# Built-In Functions

Python provides a set of built-in functions that are available by default without the need for importing any modules. These functions cover a wide range of functionalities and are an integral part of the Python language. Here are some commonly used built-in functions in Python:

- Print: print() is used to output text or variables to the console.

- Type: type() is used to determine the type of an object.

- Len: len() returns the length or the number of elements in an object, such as a string, list, or tuple.

- Range: range() generates a sequence of numbers within a specified range.

- Input: input() is used to read user input from the console.

- round(x)

- abs(x)

# Data Types

Data types are the different categories in which data can be stored, handle and manipulated in python. These data types are objects.

- String(str)
- Integer(int)
- Boolean(bool): Either True or False.
- Float Point(float): Numbers with precisions. E.g 0.122, -2901.23.
- Complex Number(complex): Imaginary numbers. E.g: (89 + 9j)
- None type: The absence of value

## Custom Types

Classes to build our own Custom types in Python.

```Python
    class CustomType:
        def __init__(self):
            ...

```

## Specialized Datatype

Whenever we don't have a python built-in datatype, we can get these specialized datatypes from python packages or modules also from third packages or modules.

# Operator Precedence

- ()
- \*\*
- \*, /
- +, -

# Variable

Variable is used to store data to the computer memory.

Syntax:

```Python
variable_name = "Variable Value"

```

- We are binding the value "Variable Value" to the variable_name.
- Variables are written in snake case.
- Variables are created with numbers, alphabets and underscore.
- You can't start a variable with a number.
- \_ (underscore in python means it's private)

## Constants in Python

- By convention constants are written with all capital letters.

```Python
NAME = "Wisdom"
```

- It means this constant is not meant to change.

## Double underscore

- You create a variable with double underscore. \_\_name = 'wisdom'

## Assign multiple values to multiple varibales

```Python
a, b, c = 1, 2, 3
```

# Expression

- An expression is a piece of code that performs some form of action.
  Expression
  An expression is any combination of variables, constants, operators, and functions that can be evaluated to produce a value. Expressions are used to perform computations and return results. They are a key building block in programming because they represent values and computations.

Examples of expressions in Python:

- 2 + 3 - This is a simple arithmetic expression that evaluates to 5.
- x \* y - If x and y are variables, this expression evaluates to the product of x and y.
- "Hello" + " " + "World" - This string concatenation expression evaluates to "Hello World".
- len([1, 2, 3]) - This function call expression evaluates to 3.
- a > b - This comparison expression evaluates to a boolean value (True or False) based on the values of a and b.

# Statement

A statement is a complete line of code that performs some action. Statements are the building blocks of a program and include expressions, but they also include control structures, function definitions, and other elements that instruct the computer to perform specific operations.

- Assignment statement: x = 5
- Control flow statement (if statement):

```python if x > 3:
    print("x is greater than 3")
```

- Loop statement:

```python
    for i in range(5):
    print(i)
```

- import statement:

```python
    import math
```

# Data Types

## String Data Type

Sequence of characters stored within a single, double or triple quotes. E.g:

```Python
'Cryptic Wisdom'
" Is a"
""" Python Programmer."""
```

### String Methods

String Methods are used to perform extra action on a string.

- .lower() -> "String".lower() => 'string".
- .upper()
- .capitalize()
  ...

## Integer Data Type

- Whole numbers without precisions. E.g 1, -1, -344, 122322.

### Integer Methods

- isnumeric()
-

## Float Data Type

Numbers with precisions. E.g 0.122, -2901.23.

## Boolean Data Type

Either True or False.

## Complex Data Type

Imaginary numbers. E.g: (9j + 6).

# Type Conversion

- This is the automatic conversion of data to specific type usually to a type that is bigger.
- The Python Interpreter handles Type conversions.
  Example: integer to float.

# Type Casting

- Conversion from float to integer.
- Manual type conversion in Python. That is, a conversion the programmer does by him/her self.
- Mostly converting from bigger data type to smaller, but can be in any form.

```python
    print(3 * 2.0) # output: 6.0 (Python interpreter performed a type conversion here.)

    print(int(3 * 2.0)) # output: 6
    # after python interpreter performed a type conversion, the programmer then performed a type casting.
```

# Control Flow

Control flow in Python refers to the order in which statements are executed in a program. It determines the flow or sequence of execution based on conditions and loops. Control flow allows you to control the path of execution and make decisions in your program based on certain criteria.

Python provides several control flow structures that enable you to control the execution of statements:

- Conditional Statements (if, elif, else):

```Python
    # Note: Only the block that meets the condition will run.
    if condition1:
        # code block executed if condition1 is true.
    elif condition2:
        # code block executed if condition2 is true.
    else:
        # code block executed if neither condition1 nor condition2 is true.
```

- Tenary (Short hand if statement):

```Python
variable = 'Statement to run if the condition is True' if  condition else 'Statement to run if condition is false'
```

- Loops (for, while): Loops allow you to repeatedly execute a block of code.

Structure of for-loop and while loops:

```Python
    for item in iterable:
        # code block executed for each item in the iterable

    while condition:
        # code block executed as long as the condition is true
```

- Break and Continue: The 'break' statement is used to exit a loop prematurely, stopping the loop's execution. The 'continue' statement is used to skip the rest of the loop's code for the current iteration and move to the next iteration.

- Exception Handling (try, except, else, finally): Exception handling allows you to handle errors or exceptions that may occur during the execution of your program. The 'try' block contains the code that might raise an exception, and the 'except' block handles the exception if it occurs. The 'finally' block is used to specify code that should always be executed, whether an exception occurs or not. The else block is used to perform code if no exception was caught

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

## Loops

```Python
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

```

# Escape Sequences

```python
name = "My name is W\"isdom \\ "
```

- \t --> a tab.
- \n --> newline
- \\ --> \

# String Slicing

- Used for creating a sub-string from a string.

```python
# syntax: [start:stop:stepover]
name = 'Wisdom'
print(name[0::-1]) # ==> modsiW
comments = "I am good"
comments[0:4] # "I am" => index 4 is exclusive.
```

# Immutability

- Strings are immutable, that is, we cannot change the value of an item in a string.

# Operators

- Arithmetics Operators:

  - (+, -, /, \*, %, \*\*, //)
  - // -> It returns the number of times a number divides the certain number.
  - % -> It returns the remainder of a division.

- Augmented Assignment Operators:
  - (=, +=, -=, /=, //=, \*=, \*\*=, %=) New: (:= (Walrus Operator - used for assigning a value to a variable inside a statement))

```Python
    # walrus: new in python.
   while (entered := input("Enter your name: ")) != "quit":
       print(entered)
```

- Logical Operators:

  - (and, or)

- Comparison Operators:

  - (==, <, >, <=, >=)

- Identity Operators:

  - (is, is not)

- Membership Operators:

  - (in, not in)

- Bitwise Operators:

  - This haven't been studied.

- Conditions and Chained Conditions:

  - Condition refers to a statement or an expression that evaluates to either true or false. This uses conditional operators, e.g >, < ...

  - Chained conditions, also known as compound conditions or multiple conditions, refer to using multiple conditions together to create more complex logic (condition) in programming. This uses 'and' or 'or' logical operators.

## Operator Precedence:

Operator precedence in Python defines the order in which operators are evaluated when multiple operators are present in a single expression.

- Parentheses: Expressions enclosed in parentheses (...expr...) have the highest precedence. They are evaluated first, and the result is used in further calculations.

- Exponentiation: The exponentiation operator '\*\*' has the next highest precedence. It is used to raise a number to a power.

- Unary Operators: Unary operators like positive + and negative - sign have the next highest precedence. They are applied to a single operand.

- Multiplication, Division, and Modulo: Multiplication \*, division /, and modulo % operators have the same precedence and are evaluated from left to right.

- Addition and Subtraction: Addition + and subtraction - operators have the same precedence and are evaluated from left to right.

- Bitwise Shifts: Bitwise shift operators << and >> have the same precedence and are evaluated from left to right.

- Bitwise AND, OR, XOR: Bitwise AND &, OR |, and XOR ^ operators have the same precedence and are evaluated from left to right.

- Comparison Operators: Comparison operators like <, >, <=, >=, ==, and != have the same precedence and are evaluated from left to right.

- Boolean Operators: Boolean operators and, or, and not have the lowest precedence among the logical operators.

It's important to note that within an expression, operators with higher precedence are evaluated before operators with lower precedence. If operators have the same precedence, their evaluation order is determined by their position from left to right.


## Python List

A list is a versatile and commonly used data structure that allows you to store and manipulate a collection of items. Lists are mutable, meaning you can add, remove, or modify elements within them.
- Used to hold sequence of values.
- It is ordered that is, It stores it's element just the way they were entered in the list.
- It's elements can be changed.

### Create a List:

```Python
   container1, container2 = [1,2], list(1,2)
```

### Accessing List Elements:

```Python
    print(container1[0]) => 1
```

### Modifying List Elements:

```Python
    container1[1] = 332
```

### List Operations:
  - Concatenation (+): Adding 2 or more list objects together.
    ```Python
       a, b = [2,4,5], [43,65]
       print(a + b) => [2,4,5,43,65]
    ```
  - Repition (\*): Repeat a list a certain number of times.
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
- .append(): Adds an element to the end of the list.
- .extend(): Appends elements from an iterable to the end of the list.
- .insert(index, item): Inserts an element at a specific index.
- .remove(x): Removes the first occurrence of a specified element.
- .pop(): Removes and returns the element at a specific index, or the last element if no index is specified.
- .index(x): Returns the index of the first occurrence of a specified element.
- .count(x): Returns the number of occurrences of a specified element in the list.
- .sort(): Sorts the elements of the list in ascending order.-
- .reverse(): Reverses the order of the elements in the list. a[::-1]
- .copy(): Returns a shallow copy of the list.
- .clear(): Removes all elements from the list.

To see the complete list of methods available for any Python object, you can use the dir() function or access the Python documentation.

### Sort a list in Place:
The list.sort() method sorts the original list in place. It means that the sort() method modifies the order of elements in the list.
The sorted() can also be used to sort the list but it will return a new list.

```Python
    data_set = [2, 3, 5, 4, 1]
    data_set.sort()
    print(data_set) => [1, 2, 3, 4, 5]

    data_set2 = [2, 4, 3, 1]
    data_set2.sort(reverse=True)
    print(data_set2) => [4, 3, 2, 1]

```

- By default, the '.sort()' method sorts the elements of a list using the less-than operator (<). In other words, it places the lower elements before the higher ones.
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
    print(companies) # => [('Apple', 2019, 260.2), ('Google', 2019, 134.81), ('Facebook', 2019, 70.7)]

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

**An error occurs when the number of variable is less than the element in the sequence on the right hand side**

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
  By putting the asterisk (\*) in front of a variable name, you’ll pack the leftover elements into a list and assign them to a variable. For example:

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

# Dictionary:

- Used to hold key-value pairs.
- It is unordered.

# Dictionary Data Structure

A Python dictionary is a powerful data structure that allows you to store and retrieve data using key-value pairs.

## Creating a Dictionary

container = {"name": "Wisdom"}

# OR

container = dict(name='key1')

## Accessing Dictionary Values

print(container['name'])

## Modifying Dictionary Values

container['name'] = "George"

## Adding and Removing Key-Value Pairs:

```Python
    container['age'] = 23

    # Remove
    del container['age']
```

## Dictionary Methods

- keys(): Returns a list of all the keys in the dictionary.
- values(): Returns a list of all the values in the dictionary.
- items(): Returns a list of key-value tuples representing all the items in the dictionary.
- get(): Retrieves the value associated with a key, or a default value if the key is not found.
- pop(): Removes and returns the value associated with a specified key.
  E.g: dict_obj.pop('key')
- update(): Updates a dictionary with key-value pairs from another dictionary or an iterable. E.g: dict_obj.update({'age': 43}) # if key exists it will update the value else it creates the value
- setdefault(): Retrieves the value associated with a given key, or inserts a default value if the key is not found.
- popitem(): Removes the last item inserted in the dictionary, and returns an arbitrary key-value pair from the dictionary.
- fromkeys(): Creates a new dictionary with specified keys and a default value.

# Iterating Over a Dictionary

```Python
    for key in my_dict:
        print(key)  # Output: apple, carrot, orange

    for value in my_dict.values():
        print(value)  # Output: a fruit with a crunchy texture, a root vegetable, a citrus fruit

    for key, value in my_dict.items():
        print(key, "-", value)  # Output: apple - a fruit with a crunchy texture, carrot - a root vegetable, orange - a citrus fruit
```

## Dictionary Comprehension

Just like how you can use list comprehension to create lists in a concise and efficient way, you can also use dictionary comprehension to create dictionaries. Dictionary comprehension allows you to create dictionaries based on an iterable while defining both the keys and their corresponding values in a single line of code. Here's how you can use dictionary comprehension in Python:

```Python
    # Example 1: Creating a dictionary of squares
    squares_dict = {num: num ** 2 for num in range(1, 6)}
    print(squares_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

    # You can also Filter
    # Example 2: Creating a dictionary with even numbers as keys and their squares as values
    even_squares_dict = {num: num ** 2 for num in range(1, 11) if num % 2 == 0}
    print(even_squares_dict)  # Output: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}


```

# Tuple Data Structure.

A tuple is an ordered, immutable collection of elements enclosed in parentheses ().

- Tuple:
  - Used to hold sequence of unique values.
  - It is ordered that is, It stores its element just the way they were entered in the tuple
  - once a tuple is created you can't make changes to it.
  - It is faster than a LIST data type.
  -

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

## Tuple Unpacking and Packing

```Python
    my_tuple = 1, 2, 3, 4, 5, 6  # Tuple packing: Packing all values to 1 variable name.
    a, b, c, *variable= my_tuple  # Tuple unpacking: Spreading values to different variable names.
    print(a, b, c, variable)      # Output: 1 2 3, (4, 5, 6 )
```

## Tuple Operations

- Concatenation (+): Adding 2 or more tuples together.

```Python
    (1,2,3) + (4, 5, 6) # => (1, 2, 3, 4, 5, 6)
```

- Repetition (\*):

## Tuple Methods:

Tuples have a few built-in methods available:

- count(): Returns the number of occurrences of a specified element in the tuple. E.g: tuple_obj.count('item_in_tuple_obj') # Return the number of times 'item_in_tuple_obj' occured in the 'tuple_obj'.
- index(): Returns the index of the first occurrence of a specified element in the tuple. E.g tuple_obj.index('item_in_tuple_obj') # return the index of the first occurence of 'item_in_tuple_obj'

## Tuple Comprehension

```Python
    my_tuple = (x for x in range(5))
    print(type(my_tuple))    # Output: <class 'generator'>
    print(tuple(my_tuple))   # Output: (0, 1, 2, 3, 4)

    # ------------
    even_tuple = tuple(x for x in range(10) if x % 2 == 0)
    print(even_tuple)    # Output: (0, 2, 4, 6, 8)
```

# Set Data Structure

In Python, a set is an unordered collection of unique elements. Sets are mutable, which means you can add or remove
elements from them. Sets are represented by curly braces {} or by using the set() function.

- Set:
  - Used to hold sequence of unique values.
  - It is unordered that is, It doesn't store its element just the way they were entered in the set.
  - Does not support indexing.
  - No Duplicate record.

## Creating a Set

```Python

    fruits = {'apple', 'banana', 'orange'}
    print(fruits)  # Output: {'orange', 'banana', 'apple'}

    numbers = set([1, 2, 3, 4, 5])
    print(numbers)  # Output: {1, 2, 3, 4, 5}
```

## Set Comprehension

```Python
    tags = {'Django', 'Pandas', 'Numpy'}
    lowercase_tags = {tag.lower() for tag in tags}
    print(lowercase_tags)
```

## Removing an Items

```Python
    fruits = {'apple', 'banana', 'orange'}
    fruits.add('grape')
    print(fruits)  # Output: {'orange', 'banana', 'grape', 'apple'}

    fruits.remove('banana')
    print(fruits)  # Output: {'orange', 'grape', 'apple'}

    fruits.discard('kiwi')
    print(fruits)  # Output: {'orange', 'grape', 'apple'}
```

## Set Operation

### Set Union

The union of two sets returns a new set that contains combination of the two sets but those element are unique.

- Use union() method or set union operator (|) to union two or more sets.

```Python
    s1 = {'Python', 'Swift', 'Java'}
    s2 = {'Dart', 'Javascript', 'Java'}
    s3 = {'Golang', 'Rust', 'Haskell', 'R', 'C#'}

    s = set1.union(s2, s3)
    print(s) # Output: {'Python', 'Swift', 'Java', 'Dart', 'Javascript', 'Golang', 'Rust', 'Haskell', 'R', 'C#'}

- The union() method accepts one or more iterables while the set union operator (|) only accepts sets.
```

```Python
    s1 = {'Python', 'Java'}
    s2 = {'C#', 'Java'}
    s3 = {'Golang', 'Swift', 'Python'}

    s = s1 | s2 | s3

    print(s)
```

### Advantage of the union() method over the (|) operator:

- The union() method can take in other iterables and converts it to set.
  E.g: set1.union(set2)

- The (|) operator only allows sets. E.g: set1 | set2 | set3.

set1 | list1 # Output: TypeError

## Set Intersection (&):

-

## Set Differences (-):

- This is used to return the difference between 2 sets A and B.

```python
set_1 = {1,2,3,4,5,6,7}
set_2 = {4,5,6,7,8}

print(set_1.difference(set_2)) # => {1,2,3,8}
```

## Set Symmetric Difference symmetric_difference() method and the symmetric difference operator (^):

-

## Set Subset

-

## Set Superset:

-

## Set Disjoint:

-

##

# Iterable and Iterator

Iterables is an object that can be looped over.

- list
- tuple
- dictionary
- set
- files
- generators

Any object with **iter**() method, means that object can be looped over / is an iterable.

- Iterator: is an object with a state so that it remembers where it is during iteration, they know how to get their next value with the **next**() which is one of the magic methods of an Iterator | next() which is a built-in function that calls the '**next**()' method.

- iter(iterable) -> returns an iterator object which we can then use the 'next()' to get the next element in the sequence, and once each element has been accessed, it is then lost or removed from the state. When the iterator is exhausted i.e when we have accessed all of it's element, and we try to access an element again from it, a 'StopIteration' Exception will be thrown

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
    function_name(argument1, argument2)
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

## map(), filter(), reduce()

The map(), filter() and reduce can be used on any Iterable object.

- map(function, iterable): This is used to perform a function on every item of an iterable passed to it, it/to return a new iterator object An object that has the ''''**next**()''' method. Works on all python iterable.

```Python
   container = [2, 3, 4]
   calculation_response = map(lambda x: x**2, container)
   # The above statement yeilds an iterator object"<map object at 0x10bf88670>".

   # Convert the iterator to a list
   print(list(calculation_response)) => # [4, 9, 16]
```

- filter(function, iterable) built-in function -> Use the Python filter(fn, iterable) function to filter an Iterable. The function "fn()" is ran on every element on the iterable and returns 'True' where any element meets the condition. A new iterator object is returned after using filter object.

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

# General Information

### Garbage Collection:

When the del keyword is used to delete an object, the interpreter simply, unbinds the object from the variable or removes the variable name from the corresponding namespace. The object however continues to exist in memory and if no other variable name is bound to it, it is later automatically destroyed.
This automatic destruction of unreferenced objects in python is called garbage collection.
Garbage collection is the destruction of unreferenced objects in python.
