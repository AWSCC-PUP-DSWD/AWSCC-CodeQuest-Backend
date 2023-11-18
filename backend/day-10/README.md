<h1 align="center">Exception Handling</h1>

---

While coding, you will occasionally encounter some errors that will appear once you execute your own program, and it's quite frustrating to see it almost every time you click run. For the Day 10, we will learn about the errors and exceptions, and how we can handle it in our program. 

<h3 align='center'>Errors and Exceptions</h3>

Error messages such as `Syntax Error: invalid syntax` or `IndentationError: expected an indented block after function definition on line x` may have already appeared on your terminal when you first start writing code in Python, and these are called the **Errors**. 

Some errors you may encounter in Python includes:

| Error | Description |
| ---   | ---         |
| AttributeError | when an attribute assignment or reference fails 
| KeyError | when a key is not found in a dictionary
| NameError | when a variable is not found in the local or global scope
| KeyboardInterrupt | when the user hits the interrupt key (Ctrl+C or Del)
| SyntaxError | when a syntax error is encountered by the parser
| TabError | when the indentation consists of inconsistent tabs and spaces
| TypeError | when a function or operation is applied to an object of an incorrect type |
| ValueError | when a function gets an argument of correct type but improper value
| ZeroDivisionError | when the second operand of a division or module operation is zero (0) |


But if we detected these errors and prevent them from executing the particular code that will raise an error, it is now called an **exception**.

**Exceptions** are basically errors that are detected and handled during execution. If an error is not detected, it will result in an error message that we have mentioned earlier. 

### How do we detect an error?


```python
age = input("Please enter your age: ")

if (age > 18):
    print("You are not eligible for a discount.")
else:
    print("You are eligible.")

```
If we try to run the code above, it will cause an error if the user inputs a non-digit character:

```
TypeError: '>' not supported between instances of 'str' and 'int'
```

This is because the program only assumes that the input will enter a valid type, and didn't take into account the illegal inputs which can cause fatal errors in our program.

In Python, we can handle exceptions using `try ... except ...` statement like this:

```python
age = input("Please enter your age: ")

try: 
    if (age > 18):
        print("You are not eligible for a discount.")
    else:
        print("You are eligible.")
except TypeError:
    print("Invalid input.")
```

In the code snippet above, the program will first execute the code inside the `try` block. 

- If no exceptions occurs in the `try` block, then the `except` block is skipped and the entire `try` block will be executed.
- If an exception occurs, then the rest of the code inside the `try` block is skipped, and if the error matches the exception named after the `except` keyword, then the `except` block is executed.
- If the error didn't match the exception named after the `except` keyword, then it is considered to be an unhandled exception and an error message will be displayed after the execution stops.

We can also have different `except` block for different exceptions:

```python
try: 
    if (age > 18):
        print("You are not eligible for a discount.")
    else:
        print("You are eligible.")
except TypeError:
    print("Invalid input.")
except ValueError:
    print("Invalid value.")
```

or have many exceptions in a single block:

```python
try: 
    if (age > 18):
        print("You are not eligible for a discount.")
    else:
        print("You are eligible.")
except (TypeError, ValueError):
    print("Invalid input.")
```

It also has an optional `else` block that is executed if no exceptions occured.

```python

def divide(a, b):
    return a / b

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a second number: "))
    quotient = divide(a, b)
except Exception as e:
    print(f"Invalid input: {e}")
else:
    print(f"The quotient is {quotient}")
```

The quotient will be displayed if no errors are encountered in the `try` block.

---

### Additional Resources:

- [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Python - Error Types](https://www.tutorialsteacher.com/python/error-types-in-python)
- [Python Exception Handling](https://www.programiz.com/python-programming/exception-handling)
