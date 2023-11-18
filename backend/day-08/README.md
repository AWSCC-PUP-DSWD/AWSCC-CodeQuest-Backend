<h1 align="center">Functions and Debugging Techniques</h1>

---

<h3 align='center'>❓What is a Function?</h3>

A **function** is a self-contained reusable block of code that can be called to execute a set of specific instructions. It provides modularity (*separation of functionality into independent modules*) and reusability, contributing to a well-organized and reliable code structure, which is considered good programming practice.

You have already seen and used a function already. `print()` and `input()` are among the numerous **built-in functions** that Python provides, and we will learn how you can build your own, too.

---

Suppose we want to calculate the average of values in a given list. We might initially do something like this:

```python
my_list = [5, 9, 2, 3, 1]

sum = 0
avg = 0

for num in my_list:
    sum += num

avg = sum / len(my_list)
print(avg)
```
<sup>You can try to execute this code in `day-8-avg.py` file located in this folder.</sup>

The code is doing its task perfectly, and it runs with no errors, but what if we need to compute the averages for multiple lists?Copying and pasting this code repeatedly would eventually lead to a cluttered and hard-to-maintain code. In such cases, it's best to create our own custom **function** that can be reused as often as needed.

To declare a function, we need these three things:

- Function Name
- Parameter List
- Function Body

A **function name** is just simply the name of the function that we will create. In this case, we'll name it `avg` since its job is to get the average of a list.

We will need to use the keyword `def` to define a function in Python.

```python
def avg
```

The code is not complete yet, and we need to add the next thing: **Parameter List**.

A **parameter** is a special variable given as an input to a function which will be used inside the function body.

In this case, we want to have a **list** as a parameter which we will name as `numlist`.

To define a parameter in the function declaration, place it within `()` after the function name. We will also need to add a colon `:` to start the **function body** on the next line.

```python
def avg(numlist):
    # function body ...
```

A **function body** is the block of code that the function will execute once it gets called.

In this case, we'll just use the same code as before, with some minor modifications:

```python
def avg(numlist):
    sum = 0
    avg = 0

    for num in numlist:
        sum += num

    avg = sum / len(numlist)
```

We use `numlist` in the for loop and `len()` since it is the list that gets passed once the function gets called.

To call the function:

```python
my_list = [5, 9, 2, 3, 1]
my_avg = avg(my_list)
```

We are passing `my_list` as an **argument** to the `avg` function, which will become the value of the parameter `numlist` inside the function.

An **argument** is the value that gets passed in the function call.

If we try to run the code above and print the value of `my_avg`, you will notice that it will display `None`. This is because a function needs to **return** something after the code gets executed. In this case, we have to return the value of `avg`.


```python
def avg(numlist):
    sum = 0
    avg = 0

    for num in numlist:
        sum += num

    avg = sum / len(numlist)
    return avg      # <-- returning the value of avg 
```

Now, when we run this code:

```python
my_list = [5, 9, 2, 3, 1]
my_avg = avg(my_list)
print(my_avg)
```

The returned value in `avg(my_list)` is now stored in `my_avg` variable, which will get displayed in the next line.

---

<h3 align='center'>🐞 Debugging Techniques 🐞</h3>

As we continue to further improve our skills as a developer, we will also inevitably encounter some challenging bugs and errors that we must solve to make everything work quite right. With this in mind, it's considered an essential skill for a developer to learn **debugging**.

Here are some debugging techniques that can help you:

- Print Debugging
    - This may be the most common debugging the most developers use. It includes using print statements to check the current value or state of a variable/element. By doing that, they will get an idea on what part of the code things get a little messy.

- Using a Debugger Tool
    - This includes using breakpoints and watching variables currently being used in the program execution to check for the state of the entire or part of the program that may be causing the issue.

    - If you're using Visual Studio Code, you can check out [this video](https://www.youtube.com/watch?v=7qZBwhSlfOo) to learn more about the Debugger Tool in your text editor.

While the debugging technique will really depend on you, the developer, it's still very beneficial to know some of the other options that may help you in such cases where you encounter a really complicated problem.

---


### Additional Resources:

- [Computer Programming - Functions](https://www.tutorialspoint.com/computer_programming/computer_programming_functions.htm)
- [Modular programming: beyond the spaghetti mess](https://www.tiny.cloud/blog/modular-programming-principle/)
- [Debugging - Full Stack Python](https://www.fullstackpython.com/debugging.html)
- [8 debugging methods you need to know about](https://www.shakebugs.com/blog/app-debugging-methods/#Brute_force_method)