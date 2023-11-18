<h1 align="center">Virtual Environment</h1>

---

A common practice when developing programs in Python is to set up a working environment by installing Python and the required third-party libraries and modules all in one place. This approach is typically convenient for beginners as it eliminates the need to configure their own environment, which can be complex. However, it's essential to eventually grasp this process because relying solely on this approach can lead to frustrating dependency issues and challenges in the long run.

### What is a Virtual Environment?

A **virtual environment** is like a sandbox for your Python projects. It allows you to create isolated, self-contained environments where you can install the specific packages and dependencies your project needs. This isolation prevents conflicts between different projects and ensures that you can easily manage your project's environment, no matter how many you have.

---

### How to Setup a Virtual Environment in Python

1. Installation

    To install virtual environment, run this command in your terminal:

    ```cmd
    pip install virtualenv
    ```

2. Initialization

    To use it, go to the root of your project directory and run the following command:

    ```cmd
    python -m venv <virtual-env-name>
    ```

    replacing `<virtual-env-name>` with the actual name of the virtual environment folder that will be created after you run the command.

3. Activation

    To activate the virtual environment, run the following command:

    If you're in Linux or MacOS:

    ```bash
    source <virtual-env-folder>/bin/activate
    ```

    If you're in Windows (cmd):
    
    ```cmd
    <virtual-env-folder>/Scripts/activate.bat
    ```

    Powershell:

    ```powershell
    <virtual-env-folder>/Scripts/Activate.ps1
    ```

This will activate your virtual environment, and `(<virtual-env-name>)` will now appear in your terminal.

---

### Installing Packages in Virtual Environment

Now that you're inside the virtual environment, you can install packages just as you would in your system-wide Python installation. For example:

```bash
pip install package_name
```

This will install the package within your virtual environment, keeping it isolated from other projects.

---

### Saving Your Dependencies

To save your project's dependencies to a requirements.txt file for easy sharing and reproducibility, use the following command:

```bash
pip freeze > requirements.txt
```

or, if `requirements.txt` is available and you want to install all the packages needed in a specific project, you can run the following command to install everything listed in `requirements.txt` file:

```bash
pip install -r requirements.txt
```

And that's it! We have learned about setting up our own virtual environment in Python, as well as installing and saving the packages in a file.

---

### Additional Resources:

- [How to Setup a Virtual Environment in Python - And Why It's Useful](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)
- [Python and Virtual Environments](https://csguide.cs.princeton.edu/software/virtualenv)