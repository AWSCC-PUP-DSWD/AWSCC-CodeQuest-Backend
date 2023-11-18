<h1 align="center">Logical Operators</h1>
<hr>

Enough with just some simple **IF**s and **ELSE**s. Let's now  have some **AND**s, **OR**s, and **NOT**s in our code.

<h3 align='center'>❓What are Logical Operators?</h3>

**Logical Operators** are used to perform logical operations on *Boolean* values: `True` and `False`. It connects two or more logical expressions to create a compound and more complex conditions. 

In Python, you can perform logical operations using the following keywords:

- and - to perform logical AND operation
- or - to perform logical OR operation
- not - to perform logical NOT operation

It uses self-explanatory words to express their functions. No more further simplifications, it just doesn't get simpler than this.

### AND

For the expression to be `True`, the two logical expressions **should** both be `True`.

```Python

num1 = 5
num2 = 12

if (num1 % 2 == 0) and (num2 % 2 == 0):
    print("Both numbers are even.")
else:
    print("At least one of the numbers isn't an even number.")
```
Since `num1` is not an even number, the code should print out what's inside the else statement.


### OR

For the expression to be `True`, at least one logical expression **must** be `True`.

```python

age = 33
is_member = True
discount = 15

if (age < 18 or is_member):
    print(f"You are eligible for a {discount}% discount!")
else:
    print("Sorry, you do not qualify for a discount.")
```

In the provided code snippet above, individuals under the age of 18 **or** those who are current members are qualified for a discount.

### NOT

Using `not` will **invert** the truth value of a logical expression. If it is `True`, then it returns `False`, else if it's `False`, then it returns `True`.

```python

gwa = 2.01

if not gwa > 2.00:
    print("Congratulations! You qualify for a Dean's Lister award!")
else:
    print("Sorry, your current GWA falls below the minimum grade requirement.")
```

The logical expression inside the if statement states that if the gwa is **not** higher than 2.0, then you qualify for the award.

---

<h1 align='center'>CHALLENGE TIME!!!</h1>

Create your own simple **rock-paper-scissor** console game! Use logical operators to finish this challenge.

A sample output for this challenge may look like this:

```python
Player1: Rock
Player2: Scissors

Player1 Wins!
```

---

### Additional Resources:

- [Python Logical Operators with Examples](https://www.geeksforgeeks.org/python-logical-operators/)
- [Logical Operators - Programming Fundamentals](https://press.rebus.community/programmingfundamentals/chapter/logical-operators/)
- [The 'not' Boolean Operator in Python](https://www.askpython.com/python/not-boolean-operator)
- [Python Logical Operators](https://www.w3schools.com/python/gloss_python_logical_operators.asp)
