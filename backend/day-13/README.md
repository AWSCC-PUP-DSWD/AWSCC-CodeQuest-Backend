<h1 align="center">Pillars of OOP</h1>

---

Continuing with our introduction to Object-Oriented Programming, we will now learn about the **Four Pillars of OOP**.

OOP is a big topic and we definitely can't put all of that in just a couple of days, but we aim to familiarize you with its concept that may help you in solving or approaching a problem.

After learning how to create a class, instantiate an object, and define a constructor, we will now dive deeper into the principles that govern this paradigm to help you gain a clear understanding as to how OOP enforces reusable and organized modeling of real-world concepts.

<h3 align='center'>The Four Pillars of OOP</h3>

Here are the four pillars of OOP:

1. Abstraction
2. Inheritance
3. Polymorphism
4. Encapsulation

We will learn the four pillars of OOP in two consecutive days starting today.

#### Abstraction

**Abstraction** in OOP means hiding away  unnecessary information for a user or developer. This includes hiding the implementation details to something like a function so you don't have to fully understand *how* it is doing it - you only need to know what it does.

Do you know how just by using `print()`, we can print texts in the terminal? 

What about file handling? How does Python make it so easy to open a file just by using `open()`?

We mostly don't know *how* Python does it, but we also don't really *need* to understand the magic behind it. And that's the power of **abstraction**, it only shows what's important for you.

This is very much what classes do. Let's create a `Calculator` class that will do some calculations for us:

```python
class Calculator:
    pass
```

Since we won't be adding anything into it at the initialization, it's okay to drop the `__init__` method for now.

What if we want it to get the sum of a list? We can do something like this:

```python
class Calculator:
    def sum(self, numlist: list):
        _sum = 0

        for num in numlist:
            _sum += num

        return _sum
```

Our calculator now has a method to get the sum of a list! Let's try it by instantiating a new Calculator object and using its `sum` method:

```python
numbers = [5, 10, 15, 20, 25]
my_calculator = Calculator()

sum = my_calculator.sum(numbers)
print(sum)
```
<sup>You can try to run this code in `day-13-abstraction.py` inside this folder.</sup>

And it should print out `75`.

The way we did it is by hiding away the implementation of the `sum` method. They don't exactly need to know that we use for loop, created a local variable, added the numbers in each iteration, then returning that number after execution. They just need to know that it gets the sum of a list - and that's the whole point of **abstraction**.

### Inheritance

After learning about abstraction, we can now move on to **inheritance**.

**Inheritance** is the way of *inheriting* a property or method from another object. This enforces reusability and better code organization since objects who share a common functionality can all just inherit from a parent class, which promotes more efficient code maintenance, as changes and updates only need to be made in the base class that others inherit from.

Say we want to create a `BasicCalculator` and a `ComplexCalculator`, let's start by creating their own classes and adding the `sum` method that we just created a while ago:

```python
class BasicCalculator:
    def sum(self, numlist: list):
        _sum = 0

        for num in numlist:
            _sum += num

        return _sum
```

```python
class ComplexCalculator:
    def sum(self, numlist: list):
    _sum = 0

    for num in numlist:
        _sum += num

    return _sum
```

Both of them have the same method, and it works perfectly fine. So, how does inheritance really *improve* this code?

In our example, the two classes only have a single method that share the same function, but if we are to add multiple methods like `difference`, `product`, `quotient`, etc. then that's where things can get a little messy since we now have lots of duplicate codes.

To use inheritance in our code, let's just declare the `sum` method inside the `BasicCalculator` class and let the `ComplexCalculator` inherit from it, and we just need to put the name of the parent class inside a parentheses in the declaration of the child class:

```python
class BasicCalculator:
    def sum(self, numlist: list):
        _sum = 0

        for num in numlist:
            _sum += num

        return _sum

class ComplexCalculator(BasicCalculator):
    pass
```

And that's it! Even though we haven't declared anything inside the `ComplexCalculator`, it now inherits all the properties and methods from the `BasicCalculator` class that has an existing `sum` method.

We can try this by running this code:

```python
basic = BasicCalculator()
complex = ComplexCalculator()

print(basic.sum([1, 2, 3]))
print(complex.sum([1, 2, 3]))
```

<sup>You can try to run this code in `day-13-inheritance.py` inside this folder.

You will notice that they will both print out `6`. Now if we are to add additional methods that our two calculators share, then we can just create it inside the parent class, in this case the `BasicCalculator` and it will just be automatically inherited by the subclasses.

At this point, our two classes `BasicCalculator` and `ComplexCalculator` have no differences at all, so we'll have to add methods that is unique tot the `ComplexCalculator`. Note that `BasicCalculator` will not be having any unique methods since it is just a base calculator that the complex calculator is upgraded from.

```python
class ComplexCalculator(BaseCalculator):
    def power(base, exponent):
        return base ** exponent

    def abs(number):
        if number >= 0:
            return number
        return -number
```

And we just created the unique methods for `ComplexCalculator`. Any methods declared inside the subclass will not be present in the parent class, but any methods and properties that we declare inside the parent class will also be present in its subclasses.

### Additional Resources

- [Pillars of OOP](https://dev.to/kedark/pillars-of-oops-in-python-k6a)
- [The Four Pillars of Object-Oriented Programming](https://www.freecodecamp.org/news/four-pillars-of-object-oriented-programming/)