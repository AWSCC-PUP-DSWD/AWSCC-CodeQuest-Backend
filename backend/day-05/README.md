<h1 align="center">Randomization</h1>
<hr>

<h2 align="center">Introduction to Randomization</h2>

* Randomization is the process of generating values or outcomes that lack predictability and follow no discernible pattern. It is widely employed in computer science and mathematics to introduce unpredictability into various contexts. Randomization finds applications in diverse fields, including gaming, simulations, and security.

<br><br>
		
### The `random` Module
* The `random` module is a fundamental tool in programming that provides various functions for generating random values or introducing randomness into your code. This module allows you to perform tasks like generating random numbers, shuffling sequences, and making choices randomly.
  
* To use the `random` module, you need to import it into your program. Importing the `random` module is essential to access these functionalities and add unpredictability to your code.
```Python
# How to import the random module
import random
```

<br>
<hr>

There are numerous methods available within the random module, but for our current focus, we will specifically delve into the `randint()`, `choice()`, and `shuffle()` functions.

<br>

### Generating Random Numbers

* The `random.randint(a, b)` function is a convenient feature provided by the `random` module in Python. This function allows you to generate random integers within a specified range, inclusive of both "a" and "b." In other words, it can produce random integers that fall between the values of "a" and "b," including "a" and "b" themselves.
 
```Python
import random
random_number = random.randint(1, 10) # Selects a random number from 1-10
print(random_number)
```
<br>

### Random Choices

* The `random.choice()` function is a valuable feature provided by the `random` module in Python. It allows you to select a random element from a sequence, such as a list or tuple. This function is handy for scenarios where you want to introduce randomness or unpredictability by choosing a random item from a given collection.
```Python
import random
colors = ["Red", "Green", "Blue", "Yellow"]
choice = random.choice(colors)  # Selects a random color from the list
print(choice)
```
<br>

### Shuffling Sequences

* The `random.shuffle()` function is a useful tool provided by the `random` module in Python. This function allows you to shuffle the elements of a sequence, typically a list. It randomizes the order of the elements within the sequence, providing a way to introduce randomness and unpredictability.
```Python
import random
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(numbers)  # Shuffles the list
print(numbers)
```
<br>
<hr>

#### Remember:

* We use `random.shuffle()`, `random.randint()`, and `random.choice()` instead of just `shuffle()`, `choice()`, and `randint()` because these functions are part of the `random` module in Python. Since they are not built-in functions but are provided by the `random` module, you need to prefix the function names with the module name (`random.`) to indicate where Python should find them. This ensures that Python looks in the `random` module for these specific functions, preventing naming conflicts with other functions or variables in your code.

#### Additional Resources:

* <a href="https://www.w3schools.com/python/ref_random_randint.asp">random.randint()</a>

* <a href="https://www.w3schools.com/python/ref_random_shuffle.asp">random.shuffle()</a>

* <a href="https://www.w3schools.com/python/ref_random_choice.asp">random.choice()</a>

<hr>

<h1 align="center">CHALLENGE TIME!!!</h1>

<p align="center">Create a Rock, Paper, Scissors game. Try it yourself first before searching online for answers.</p>

<br>

Hints:

* When taking user input for your choice (Rock, Paper, or Scissors), remember to use the `.lower()` method to convert the input to lowercase. This ensures that the game works regardless of whether the user types 'Rock', 'rock', 'RoCk', or any other combination of capitalization.

Sample Code:
```Python
ask = input("Enter your name: ").lower()
print(ask)
```
Output:
```Python
Enter your name: bAcK EnD
back end
```
<br><br>

*  Create a list and make the computer choose from the items inside the list.

Sample Code:
```Python
import random
names_list = ["John", "Mark", "Dave", "James"]
computer_choice = random.choice(names_list)
print(computer_choice)
```
Output:
```Python
Dave
```
