<h1 align="center">Day 2: Basic Data Types and User Inputs</h1>
<hr>

<h2 align='center'>Data Types</h2>

Let's start your Day 2 of Backend Development with the introduction to **Basic Data Types**.

### ❓ What is a Data Type?

- You can think of data type as an attribute, or as the name suggests, a *type*, associated with the data being used within our program, and it tells the compiler or interpreter how its value should be treated.

### 👀 Common Data Types

There are various data types present in different programming languages, but here are the most basic forms of data types that you should be aware of:

#### Integer
- often shortened as *int*, it is a data type representing any whole numbers.

To have a variable with integer data type in Python, initialize it with any integer value:

```Python
my_int = 10
```

You may remember that Python has [type inference](https://en.wikipedia.org/wiki/Type_inference), so you don't need to specify its data type when declaring any variables.

#### Float
- represents numbers with floating point.

To have a variable with data type in Python:
```Python
my_float = 1.23
```

#### Character
- often shortened as *char*, it represents a single character. 

Although Python doesn't have a character data type, instead, it uses a data type called **string**.

#### String
- often shortened as *str*, it represents a sequence of characters. You may declare a string enclosed in single, double, or triple quotes.

```Python
my_str = 'Hello, AWSCC!'
my_str1 = "Hello, DSWD!"
my_str2 = '''Hello, Backend!'''
```

#### Boolean
- often shortened as *bool*, it represents the two Boolean values: `True` or `False`. This can be very useful for logical operations and conditions.

```python
my_bool = True
your_bool = False
```

#### Null Type
- a special kind of data type that only represents a single value: `None`. This is used when a variable does not contain any value.

```python
null = None
```
<hr>

<h3 align='center'>User Inputs</h3>

You learned in Day 1 that we can print an output simply by using `print()`. This time, let's learn how to take an input from the user. 

To take an input from the user, you can simply use (*and you might have guessed it already*) `input()`.


Here's a simple Python code that uses `input()` to ask the user their age and store it in the `age` variable.

```Python

age = input("Enter your age: ")
print(f"You're {age} years old.")
```

You can try running it in `day-2-input.py` inside this folder.

---

<h1 align='center'>CHALLENGE TIME!!!</h1>

Since you are now familiarized with the basic data types and the `input()` function, it's time for you to take on some challenges:

Write a Python program that prompts the user to enter three integer values and then calculates and displays their sum.

The output may look like this:

```
Enter the first number: 5
Enter the second number: 19
Enter the third number: 11

Sum: 35
```

---

### Additional Resources
- [What are Data Types and Why Are They Important?](https://amplitude.com/blog/data-types)
- [Programming Fundamentals: Data Types](https://press.rebus.community/programmingfundamentals/chapter/data-types/)
- [Python Basic Input and Output](https://www.programiz.com/python-programming/input-output-import)