<h1 align="center">Pillars of OOP</h1>

---

After learning about two of the four pillars of OOP, we'll now continue with the last two pillars that we haven't covered yet.

Recall that there are **Four Pillars of OOP**:

1. Abstraction ☑️
2. Inheritance ☑️
3. Polymorphism
4. Encapsulation

**Abstraction** is the way of hiding the implementation details and only show what the function really does.

**Inheritance** is the way of *inheriting* properties and methods from the parent class to avoid duplicating and hard to maintain codes.

### Polymorphism

The word **polymorphism** comes from the Greek words that mean "many shapes". It is the [capacity of existing in different forms](https://www.etymonline.com/word/polymorphism). In OOP, it means that methods and functions can also be implemented in many different forms.

Let's modify our code in the previous day to focus more on the use of polymorphism.

We will make a `product` method wherein `BasicCalculator` can only handle 3-digit integers, and we'll make the limit go up to 8 digits in the `ComplexCalculator`:

```python
class BasicCalculator:
    def sum(self, numlist: list):
        _sum = 0

        for num in numlist:
            _sum += num

        return _sum
    
    def _digits(self, number):
        digit = 0
        while number != 0:
            digit += 1
            number //= 10

        return digit
    
    def product(self, numlist):
        _product = 0
        
        for num in numlist:
            if self._digits(num) > 3:
                raise ValueError("Basic Calculator can only handle 3 digits.")
            _product *= num

class ComplexCalculator(BasicCalculator):
    def power(base, exponent):
        return base ** exponent

    def abs(number):
        if number >= 0:
            return number
        return -number
```

We created a private method `_digits` in `BasicCalculator` that will count the number of digits in the list, and a `product` method that will multiply all the elements inside the passed list.

If the number of digits inside the list is greater than 3, then the program will raise an error and it will stop the execution.

Now, how can we modify the method to accept 8 digits in the `ComplexCalculator` class? By using **polymorphism**.

The `ComplexCalculator` can have its own implementation of the `product` while still inheriting some methods in the parent class.

We can do it by declaring the method with the same name inside the subclass:

```python
class ComplexCalculator:
    def power(base, exponent):
        return base ** exponent

    def abs(number):
        if number >= 0:
            return number
        return -number
    
    def product(self, numlist):
        _product = 1
        
        for num in numlist:
            if self._digits(num) > 8:
                raise ValueError("Complex Calculator can only handle 8 digits.")
            _product *= num

        return _product
```

If we try to run this code:

```python
basic = BasicCalculator()
print(basic.product([9825, 3412, 5531, 7658]))
```

It will raise an error saying that the Basic Calculator can only handle numbers up to 3 digits, but if we instead use the `product` of `ComplexCalculator`:

```python
complex = ComplexCalculator()
print(complex.product([9825, 3412, 5531, 7658]))
```

It will output the product of the given list. You can also try experimenting with the code provided in `day-14-polymorphism.py` located in this folder.

### Encapsulation

We arrived in the fourth and last pillar of OOP: **encapsulation**.

Encapsulation is a way of restricting access to some parts of your code, primarily to avoid undefined and unintended behaviors. It is considered a good practice to *encapsulate* an object to mark what parts can be *safely* modified or accessed and what should remain off-limits.

In Python, nothing can be private. Everything can be accessed if anyone is determined to do so. But we do have naming conventions to mark whether a property or method is part of public access or not. Using an underscore `_` prefix will indicate that it is a special attribute and therefore should not be accessed or modified unless you know what you're doing.

We already achieved this in our variables and names that have underscore prefixes.

Let's create a new example. Suppose we're retrieving students information and we're storing their `birthdate` property in a [unix time](https://en.wikipedia.org/wiki/Unix_time):

```python
from datetime import datetime

class Student:
    def __init__(self, name, birth_yr, birth_mo, birth_day):
        self.name = name
        self._birthdate = self._to_unixtime(birth_yr, birth_mo, birth_day)

    def _to_unixtime(self, yr, mo, d):
        return datetime(yr, mo, d).timestamp()        

student1 = Student("John", 2002, 10, 20)
print(student1._birthdate)
```

If we try to access `student1._birthdate`, we can only have a numerical value and we didn't actually received the data that we want. This is because we designed the `birthdate` to not be accessible in public. If we want it to be accessed externally, we can define a function that returns the value that it expects:


```python
from datetime import datetime

class Student:
    def __init__(self, name, birth_yr, birth_mo, birth_day):
        self.name = name
        self._birthdate = self._to_unixtime(birth_yr, birth_mo, birth_day)

    def _to_unixtime(self, yr, mo, d):
        return datetime(yr, mo, d).timestamp()

    def birthdate(self):
        return datetime.fromtimestamp(self._birthdate).strftime("%B %d, %Y")

student1 = Student("John", 2002, 10, 5)
print(student1.birthdate())
```

and it will output:

```cmd
October 05, 2002
```

And we can make it look like a property using the `@property` decorator:

```python
@property
def birthdate(self):
    return datetime.fromtimestamp(self._birthdate).strftime("%B %d, %Y")
```

We can now discard the `()` when accessing this method:

```python
print(student1.birthdate)
```

That's it! We successfully encapsulated the birthdate of the `Student` objects and implemented our own method to access the protected variable while executing some instructions before returning the expected value.

---

### Additional Resources

- [The Four Pillars of Object-Oriented Programming](https://www.freecodecamp.org/news/four-pillars-of-object-oriented-programming/)
- [Python @property decorator](https://www.programiz.com/python-programming/property)
- [Polymorphism in Python](https://www.geeksforgeeks.org/polymorphism-in-python/)
- [Encapsulation in Python](https://www.geeksforgeeks.org/polymorphism-in-python/)