<h1 align="center">Classes and Objects</h1>

From Day 12-14, we'll start learning about Object-Oriented Programming (OOP), and for today, we'll talk about **classes** and **objects**.

---

<h3 align='center'>What is Object-Oriented Programming?</h3>

**Object-Oriented Programming**, abbreviated as **OOP**, stands out as one of the most popular programming paradigms widely used by developers in software development today. It utilizes the concepts of classes and objects to organize code into reusable blueprints or *classes* which are then used to initialize instances of an *object*.

Think of a class as a blueprint for creating a structure of a particular data or object. It has a state (*attributes*) and behaviours (*methods*).

For example, we want to create a structure that stores data from a student. 

```python
student1_name = "Juan Dela Cruz"
student1_age = 20
student1_sex = "Male"
student1_is_enrolled = True
student1_classes = []
student1_offenses = []
```

Without classes, we may do something like the code snippet above, copying and pasting it for every additional student info that we will create.

Fortunately, it can be done easily with the use of classes.

#### Class Declaration

To use a class in Python:

```python
class Student:
    def __init__(self):
        pass    
```

Now that's a lot of new stuffs going on here. It isn't complete yet, and it doesn't do anything yet, but let's examine every line of the code.

```python
class Student:
```

We use the keyword `class` to declare a class followed by the class name,

```python
    def __init__(self):
```

we use `def` to declare a function, and we name it `__init__` to indicate that we are implementing the **initialization** of the class. The `self` being a default parameter for a class method which represents the *object* of the class itself,

```python
    pass
```

then use `pass` as a placeholder for now.

Now, we will initialize some attributes to the object inside the `__init__` method we just declared.

#### Constructor

```python
class Student:
    def __init__(self, name, age, 
        is_enrolled, offenses):
        self.name = name
        self.age = age
        self.is_enrolled = is_enrolled
        self.classes = classes
        self.offenses = offenses
```

Let's pause here again as we just added a bunch of texts in our previous code.

```python
    def __init__(self, name, age, 
        is_enrolled, classes, offenses):
```

First, we added some additional *parameters* in our `__init__` method. You will notice that we added the info that we need in a student, and then assign it to a same name in the `self`:

```python
        self.name = name
        self.age = age
        self.is_enrolled = is_enrolled
        self.classes = classes
        self.offenses = offenses
```

Remember that the `self` is referring to the object that gets created when we instantiate it, and then we'll store the student info being passed as parameters to *that* object's states, which can be accessed in `self`. 

In case you're wondering, we aren't strictly restricted to only use the same name as the parameter, but that's just a simpler way of doing it.

If you are new with this concept and is still struggling to absorb it, [this may help you understand it more clearly.](https://www.mygreatlearning.com/blog/python-init/#:~:text=The%20python%20__init__,object%20of%20the%20class%20itself.) 

#### Instantiation

Now that we're done with defining the class and its `__init__` method, we can now instantiate an object.

To instantiate an object, we can do this:

```python

student1 = Student("Juan Dela Cruz", 20, True, [], [])
```
We are essentially calling the class `Student`, and passing some arguments into it. The arguments will be received by the `__init__` method of the class, which will then store its value in the `student1`, the name of the new object we just instantiated.

If we want to access `student1`'s properties, we will use the `.` dot notation.

```python
print(f"Name: {student1.name}")
print(f"Age: {student1.age}")
print(f"Status: {'Enrolled' if student1.is_enrolled else 'Not Enrolled Yet'}")
print(f"Classes: {student1.classes}")
print(f"Offenses: {student1.offenses}")
```

<sup>You can try running the code in `day-12-classes.py` located in this folder.</sup>

After running the code, you can see that it outputs the arguments that we passed when we call the class.

#### Class Methods

We can also create methods in the class to have more behaviours in the object.

The `__init__` is a special class method that gets executed when we instantiate an object, and we can declare another method just like `__init__`:

```python
class Student:
    def __init__(self, name, age, 
        is_enrolled, classes, offenses):
        self.name = name
        self.age = age
        self.is_enrolled = is_enrolled
        self.classes = classes
        self.offenses = offenses
    
    # add a new class to the student
    def add_class(self, new_class):
        self.classes.append(new_class)
```
We created a new method that adds new classes to the student. To use it:

```python
student1.add_class("Math")
```

and the "Math" class is now added to the student's list of classes. We can check it by printing out the student's classes:

```python
print(student1.classes)
```

And that's it! We now learned about creating classes, instantiating objects, declaring constructors, and adding methods.

---

### Additional Resources

- [What is object-oriented programming? OOP explained in depth](https://www.educative.io/blog/object-oriented-programming)
- [Python Classes and Objects](https://www.w3schools.com/python/python_classes.asp)