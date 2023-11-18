<h1 align="center">File Handling</h1>
<hr>

Files are a fundamental part of software development. They are used to store and retrieve data. In this lesson, we'll explore how to interact with files in Python.

<hr>
<br>

## File Handling Basics 
File handling involves two essential operations: reading data from files and writing data to files. Reading allows us to access existing data, while writing enables us to store new data.

<br>

### Reading Files
To read data from a file, we open the file, access its contents, and then close it. Properly closing a file is important to free up system resources.

Example Code:
```python
# Open a file for reading
with open('sample.txt', 'r') as file:
    content = file.read()
    print(content)
```

In this example, we open a file ('sample.txt') in read mode ('r') using the `with` statement. The `read()` method is then used to read the entire content of the file into the variable `content`. Finally, we print the content.

<br>

Additional Example - Reading Lines:
```python
# Open a file for reading
with open('sample.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # Use strip() to remove newline characters
```

This example reads the file line by line using `readlines()`. The `strip()` method is applied to remove newline characters from each line before printing.

<br>

### Writing to Files
Writing to files is essential for storing data. We open a file for writing, add data to it, and then close it. Modes like "w" and "a" determine whether data is overwritten or appended.

Example Code:
```python
# Open a file for writing
with open('output.txt', 'w') as file:
    file.write("Hello, World!\n")
```

Here, we open a file ('output.txt') in write mode ('w') using the `with` statement. We then use the `write()` method to add the text "Hello, World!" to the file. The '\n' represents a newline character.

<br>

Additional Example - Appending to a File:
```python
# Open a file for appending
with open('output.txt', 'a') as file:
    file.write("Appending more text!\n")
```

This example opens the same file in append mode ('a') and appends the text "Appending more text!\n" to the existing content.

<br>

### File Handling Best Practices
Properly closing files is a best practice to prevent resource leaks. The `with` statement ensures automatic file closure, enhancing code robustness.

The `with` statement automatically takes care of closing the file when the code block is exited, even if an exception occurs. This practice ensures that system resources are efficiently managed.

<hr>

## Additional Resources:

* <a href="https://www.w3schools.com/python/python_file_handling.asp">File Handling W3Schools</a>

* <a href="https://www.youtube.com/watch?v=Uh2ebFW8OYM">Python Tutorial: File Objects - Reading and Writing to Files</a>

<hr>
<br>
   
<h1 align="center">CHALLENGE TIME!!!</h1>

In a text file, provide students with a list of names, one name per line. Ask them to create a Python program that reads the names, sorts them alphabetically, and writes the sorted names back to the file.

<br>

 #### Hint:

* You can read the names from the file using the `.readlines()` method. This function reads each line in the file and returns a list of lines, making it easier to work with line-based data. To write the sorted names back to the file, consider using the `.writelines()` method, which allows you to write a list of strings back to the file.
