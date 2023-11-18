<h1 align="center">Modules and Packages</h1>
<hr>

Code organization is crucial for maintaining and reusing code efficiently. We'll explore how Python's modules and packages help us achieve this.

<hr>
<br>

### Module Definition and Creation
A module is a self-contained Python file that holds code elements like variables, functions, and classes. Modules keep code organized and maintainable.
   - Creating Modules
     - We'll create a module (e.g., `math_operations.py`) with functions (e.g., `add` and `subtract`) and demonstrate how to use it in another Python script.
     
     Example Code:
     ```python
     # name of file: math_operations.py
     def add(a, b):
         return a + b

     def subtract(a, b):
         return a - b
     ```
     ```python
     # name of file: main.py
     import math_operations

     result_add = math_operations.add(5, 3)
     result_subtract = math_operations.subtract(10, 4)
     ```
<hr>
<br>

### Built-in Modules
Python offers built-in modules for various tasks. These modules provide specialized functions for common operations.
   - Using the `math` Module 
     - We'll use the `math` module to calculate the square root of a number, showcasing how built-in modules save coding time.
     
     Example Code:
     ```python
     import math

     result_sqrt = math.sqrt(16)
     ```
     
<hr>
<br>

### Organizing Code with Packages
   - What are Packages?
     - Packages are directories that group related modules together, making it easier to manage larger projects.
       
   - Creating and Using Packages
     - We'll create a package (e.g., `mypackage`) with multiple modules and illustrate how to use the modules within the package.
       
     Example Code:
     ```python
     mypackage/  # folder name
     ├── __init__.py  # file 
     ├── module1.py   # file 
     ├── module2.py   # file 
     ```
     ```python
     # name of file: main.py
     from mypackage import module1, module2

     result1 = module1.some_function()
     result2 = module2.another_function()
     ```

<hr>
<br>

### Selective Imports
Python allows us to import only the specific functions or variables we need from a module. This reduces memory usage and enhances code clarity.

Example Code:
```python
from math_operations import add

result_add = add(8, 2)
```
```python
from math_operations import subtract

result_subtract = subtract(15, 5)
```

<hr>

#### Additional Resource:

* <a href="https://www.machinelearningplus.com/python/python-module-packages/">Python Modules and Packages</a>

<hr>
<br>

<h1 align="center">CHALLENGE TIME!!!</h1>

You are tasked with creating a module that calculates the area of a circle based on its radius. You should import this module and use it to find the area of a circle with a radius of 5.

<br>

Example Code:

```python
# name of file: square_area.py

def calculate_area(side):
    return side * side
```
```python
# name of file: main.py
from square_area import calculate_area

side = 5
area = calculate_area(side)
```

