<h1 align="center">Servers and Routing in Flask</h1>
<hr>

## Introduction to Flask

Flask is a micro web framework for Python. It's like a toolbox for building web applications. Think of it as a way to create web pages or web services using Python. Flask is known for its simplicity and ease of use. 

<br>

## Setting Up a Flask App 
To start using Flask, you need to create a Flask app. It's like setting up your workspace. You tell Python that you're going to build a web application. The `Flask(__name__)` line creates your app.

Installing Flask:
```python
pip install flask
```

Using Flask:
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'
```

<hr>
<br>

## Routing

Routing in web development refers to the process of mapping URLs (Uniform Resource Locators) to specific actions or views in a web application. It allows you to determine what content or functionality should be displayed when a user accesses a particular URL. Dynamic URLs play a crucial role in modern web applications by allowing you to handle various resources and parameters using a single route. Let's break down the concepts of routing and dynamic URLs:

### Basic Routing:

- In a web application framework like Flask or Django, you define routes to specify how the application should respond to different URLs. Each route is associated with a particular view function.

- When a user accesses a specific URL, the web framework matches the URL to a defined route and invokes the corresponding view function.

Example:
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the home page!'

@app.route('/about')
def about():
    return 'This is the about page.'

@app.route('/contact')
def contact():
    return 'You can contact us at contact@example.com.'

if __name__ == '__main__':
    app.run()
```

- In this example, we've defined three routes ('/', '/about', and '/contact') that map to different view functions.

<br>

### Dynamic URLs:

- Dynamic URLs, also known as parameterized URLs, allow you to handle variable parts of a URL. These variables are extracted from the URL and passed as arguments to the view function.

- Dynamic URLs are often used to build flexible web applications that can handle different resources or entities using a single route.

Example:
```python
from flask import Flask

app = Flask(__name__)

@app.route('/user/<username>')
def user_profile(username):
    return f'Welcome, {username}!'

if __name__ == '__main__':
    app.run()
```

- In this example, we define a dynamic URL '/user/<username>' where '<username>' is a variable part of the URL. When a user accesses a URL like '/user/johndoe', 'johndoe' is extracted as the 'username' parameter and passed to the 'user_profile' view function.

- Dynamic URLs can handle various values and provide a way to access specific resources or data by incorporating these values into the URL.

Routing and dynamic URLs are fundamental in building web applications, allowing you to create clean and user-friendly URLs, handle different resources efficiently, and provide a smooth user experience. Web frameworks like Flask and Django make it easy to define and manage routes and dynamic URLs.

<hr>
<br>

## Decorators

Decorators in Python are a powerful and flexible way to modify or enhance the behavior of functions or methods without changing their source code. Decorators are often used in web frameworks like Flask and Django to add functionality to views, such as authentication, logging, and access control. Here's an explanation of decorators with code examples:

<br>

### Basic Decorator Structure:

A decorator is a function that takes another function as an argument and returns a new function that usually extends or modifies the behavior of the original function. Decorators are applied using the "@" symbol before a function definition.

Here's a basic decorator structure:

```python
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        # Code to be executed before the original function
        result = original_function(*args, **kwargs)
        # Code to be executed after the original function
        return result
    return wrapper_function

@decorator_function
def some_function():
    # Original function code
    pass
```

In this example, `decorator_function` is a decorator that takes `some_function` as its argument and returns a new function `wrapper_function`. `wrapper_function` can perform actions before and after `some_function`. When you decorate `some_function` with `@decorator_function`, the behavior of `some_function` is modified.

<hr>
<br>

### Example Decorator - Timing Function Execution:

Let's create a decorator that measures the time it takes to execute a function:

```python
import time

def timing_decorator(original_function):
    def wrapper_function(*args, **kwargs):
        start_time = time.time()
        result = original_function(*args, **kwargs)
        end_time = time.time()
        print(f"{original_function.__name__} ran in {end_time - start_time} seconds")
        return result
    return wrapper_function

@timing_decorator
def slow_function():
    time.sleep(2)

slow_function()  # Output: slow_function ran in 2.002163887023926 seconds
```

In this example, the `timing_decorator` decorator measures the time taken to execute the decorated function. When you call `slow_function()`, the decorator records the time it takes to run and displays the result.

Decorators can be used for a wide range of purposes, including logging, authentication, access control, and more. They allow you to keep your code clean and modular by separating concerns and applying modifications to functions without altering their core functionality.

<hr>

### Additional Resources:

* <a href="https://www.geeksforgeeks.org/flask-app-routing/">Flask App Routing</a>

* <a href="https://www.programiz.com/python-programming/decorator">Python Decorators</a>




