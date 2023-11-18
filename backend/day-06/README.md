<h1 align="center">➰Loops➰</h1>

It's time to explore one of the most important element in programming: **loops**. 

For today, we'll learn about for-loops and while-loops and how we can use it to build an even more entertaining program as we progress in our Python learning journey!

---

<h3 align='center'>❓What is a Loop?</h3>

In computer programming, loop is a control structure that allows you to execute a sequence of instructions **repetitively**.

Suppose we have a problem where we need to print out numbers from 0 to 100. If we don't know anything about loops, we may approach the problem like this:

```python
i = 0
print(i)
i += 1
print(i)
i += 1
print(i)
i += 1
print(i)
# ...
```

While this manual repetition could technically get the job done considering we're only copying and pasting 2 lines of codes, it's not a recommended practice. And this is where the power of **loops** come into play. 

In Python, we have two types of loops: a *for* loop, and a *while* loop.

#### For Loop

A **for** loop is used to iterate over an iterable object (list, tuple, range, etc). We'll talk about lists and tuples in the next day.

Here's an example code that uses a **for** loop to print out numbers from 0 to 100:

```python
for i in range(101):
    print(i)
```

The `i` serves as the loop variable that will get its value incremented after every iteration.

It's worth noting that when using `range()`, you need to specify one more than your desired endpoint to include that value in the loop. Hence, in this case, we pass 101 to ensure the loop prints numbers up to 100.

#### While Loop

A **while** loop is another type of loop in Python that repeatedly executes a block of code as long as the base condition is met.

Here's an example code that uses a **while** loop to print out numbers from 0 to 100:

```python
i = 0
while (i <= 100):
    print(i)
    i += 1
```

In a while loop, you don't have a dedicated loop variable; instead, you must declare a variable (in this case, `i`) used in the loop's condition. The condition here specifies that as long as `i` is less than or equal to 100, the loop continues to print the value of `i` and then increments it by 1. This process continues until the condition is no longer satisfied.

#### Else in Loops?

Weirdly enough, in Python, we can also use an `else` clause in loops which will execute when the loop's condition is no longer met. Note that the `else` will not get executed if the loop is terminated using `break` statement.

---

<h1 align='center'>CHALLENGE TIME!!!</h1>

For today's challenge, let's code the popular children game, **FizzBuzz**!

Rules of Fizz Buzz:
- if a number is divisible by 3, print 'Fizz'
- if a number is divisible by 5, print 'Buzz'
- if a number is both divisible by 3 and 5, print 'FizzBuzz!'

Your task is to prompt the user a limit for the range of numbers to be printed out, and apply the rules of Fizz Buzz in it.

A sample output may look like this:

```
Limit: 20

1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz!
16
17
Fizz
19
Buzz
```
---

### Additional Resources:

- [Loops - Learn Python](https://www.learnpython.org/en/Loops)
- [Python for Loop](https://www.programiz.com/python-programming/for-loop)

