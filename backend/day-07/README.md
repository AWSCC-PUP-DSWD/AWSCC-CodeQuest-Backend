<h1 align="center">Lists, Tuples, and Dictionaries</h1>
<hr>
<br>

<h2 align="center">Introduction to Data Structures</h2>

* Data structures in Python are essential tools for storing, organizing, and managing data efficiently. They offer diverse ways to store and retrieve data, tailored to specific needs. These structures enable data manipulation, efficient searching, and complex data modeling, ensuring optimal performance and maintainability in Python programs.

<hr>
<br>

## Lists
In Python, a list is an ordered collection of elements. Lists are one of the most commonly used data structures and are versatile, allowing you to store a sequence of values, such as numbers, strings, or even other lists. Lists are mutable, meaning you can change their content (add, remove, or modify elements) after they are created. Lists are defined using square brackets `[]` and elements within the list are separated by commas.

<br>

#### Creating a List:

To create a list in Python, enclose the elements within square brackets.
```Python
my_list = [1, 2, 3, 4, 5]
```

<br>

#### Accessing Elements:
  
You can access elements of a list by their index. Python uses zero-based indexing, so the first element is at index 0, the second at 1, and so on.
```Python
first_element = my_list[0]  # Access the first element
```
<br>

#### Modifying Lists:

Lists are mutable, so you can add, remove, or change elements.
   - Adding Elements
     - Append an element to the end of the list:
       ```Python
       my_list.append(6)
       ```
     - Insert an element at a specific index:
       ```Python
       my_list.insert(2, 7)  # Inserts 7 at index 2
       ```
   - Removing Elements:
     - Remove the last element:
       ```Python
       my_list.pop()
       ```
     - Remove a specific element by value:
       ```Python
       my_list.remove(4)  # Removes the first occurrence of 4
       ```
   - Changing Elements:
     - Modify an element by assignment:
       ```Python
       my_list[1] = 10  # Changes the second element to 10
       ```
<br>

#### List Slicing:

You can create sublists by slicing a list. This allows you to extract a portion of the list.
```Python
sub_list = my_list[1:4]  # Creates a sublist with elements from index 1 to 3
```

<br>

#### List Functions and Methods:
  
Python provides various functions and methods for list manipulation. For instance, you can sort a list, find its length, and concatenate two lists using the `sorted()`, `len()`, and `+` functions, respectively.
```Python
sorted_list = sorted(my_list)
list_length = len(my_list)
concatenated_list = my_list + [8, 9]
```
<hr>
<br>

## Tuples
In Python, a tuple is an ordered collection of elements, much like a list. However, tuples are distinct from lists in one significant way: they are immutable. This means that once you create a tuple, you cannot change its content. Tuples are defined using parentheses `()` and elements within the tuple are separated by commas. Tuples are often used to group related data that should not change.

<br>

#### Creating a Tuple:
To create a tuple in Python, enclose the elements within parentheses.
```python
my_tuple = (1, 2, 3, "apple", "banana")
```

<br>

#### Accessing Elements:
You can access elements of a tuple using zero-based indexing, similar to lists.
```python
first_element = my_tuple[0]  # Access the first element
```

<br>

#### Tuples are Immutable:
Unlike lists, you cannot modify the elements of a tuple. Once a tuple is created, it cannot be changed, which means you can't add, remove, or change elements within it.
```python
my_tuple[1] = 10  # This will raise a TypeError because tuples are immutable.
```

<br>

#### Tuple Packing and Unpacking:
Tuples are often used for packing and unpacking values. For example, you can create a tuple with multiple elements and then assign those elements to individual variables.
```python
person = ("Alice", 30, "New York")
name, age, city = person  # Unpack the tuple into variables
```

<br>

#### Tuple Functions and Methods:
Tuples have several built-in functions and methods for various operations, such as finding the length and counting occurrences of an element.
```python
tuple_length = len(my_tuple)
count_apple = my_tuple.count("apple")
```

<hr>
<br>

## Dictionaries
In Python, a dictionary is a data structure used for storing and organizing data in the form of key-value pairs. Each key in a dictionary is associated with a value, creating a mapping between keys and their corresponding data. Dictionaries are flexible and allow you to efficiently retrieve, update, and manage data based on specific keys.

<br>

#### Creating a Dictionary:
To create a dictionary in Python, enclose key-value pairs within curly braces `{}`. Each pair consists of a key followed by a colon `:` and its corresponding value.
```python
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
```

<br>

#### Accessing Values:
You can access the values in a dictionary using the associated keys.
```python
name = my_dict["name"]  # Access the value associated with the "name" key
```
*  It's important to note that dictionary keys are case-sensitive.

<br>

#### Modifying Dictionaries:
Dictionaries are mutable, so you can add, change, or remove key-value pairs.
   - Adding a Key-Value Pair:
     
     To add a new key-value pair, simply assign a value to a new key.
     ```python
     my_dict["gender"] = "Female"  # Adds a new key-value pair
     ```

   - Changing a Value:
     
     You can change the value associated with an existing key.
     ```python
     my_dict["age"] = 31  # Updates the value associated with the "age" key
     ```

   - Removing a Key-Value Pair:
     
     To remove a key-value pair, use the `del` statement.
     ```python
     del my_dict["city"]  # Removes the key-value pair with the key "city"
     ```

<br>

#### Dictionary Methods:
Python provides a variety of methods to perform operations on dictionaries. For example, you can retrieve all keys, values, or items (key-value pairs) from a dictionary using methods like `keys()`, `values()`, and `items()`.
   ```python
   keys_list = my_dict.keys()      # Returns a list of keys
   values_list = my_dict.values()  # Returns a list of values
   items_list = my_dict.items()    # Returns a list of key-value pairs
   ```
<hr>

### Additional Resource:

* <a href="https://www.tutorialspoint.com/List-vs-tuple-vs-dictionary-in-Python">Lists, Tuples, and Dictionaries</a>

<hr>
<br>

<h1 align="center">MINI PROJECT!!!</h1>

This will be the **first** requirement in the CodeQuest: 30 Days of Backend.

Create a basic shopping list program in Python. This program should allow users to add items to a shopping list, view the list, and remove items as needed.

<br>

Output:
```python
Options:
1. Add item to the shopping list
2. View shopping list
3. Remove item from the shopping list
4. Quit
Enter the number of your choice: 1
Enter the item you want to add: Apples
Apples has been added to your shopping list.

Options:
1. Add item to the shopping list
2. View shopping list
3. Remove item from the shopping list
4. Quit
Enter the number of your choice: 1
Enter the item you want to add: Milk
Milk has been added to your shopping list.

Options:
1. Add item to the shopping list
2. View shopping list
3. Remove item from the shopping list
4. Quit
Enter the number of your choice: 2
Your shopping list:
Apples
Milk

Options:
1. Add item to the shopping list
2. View shopping list
3. Remove item from the shopping list
4. Quit
Enter the number of your choice: 3
Enter the item you want to remove: Apples
Apples has been removed from your shopping list.

Options:
1. Add item to the shopping list
2. View shopping list
3. Remove item from the shopping list
4. Quit
Enter the number of your choice: 2
Your shopping list:
Milk

Options:
1. Add item to the shopping list
2. View shopping list
3. Remove item from the shopping list
4. Quit
Enter the number of your choice: 4
Goodbye!
```
