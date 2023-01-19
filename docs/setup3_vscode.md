# Getting started with a Python Code Editor

Code editors (or Integrated Development Environment, IDEs) are fantastic resources that make it easy to write and edit code on your laptop. There are many code editors out there, but in this class, we will be using the VS Code editor to write and edit our Python programs. Code editors recognize the programming language we are coding in and highlight the syntax of the code making it easier to "see". In addition, code editors offer code completion options and can even suggest a Pytnon function for you to use based on a few letters. Amazing! IDEs will definitely make your life easier! I receommend learning as much as you can about VS Code to find out its capabilities and how it can help you in writing great code. For now, here are a few instruction to get you started.

In this class, we will be using the Visual Studio Code Editor (VS code). Visual Studio Code is a lightweight but powerful source code editor which runs on your desktop. We will write and edit python code using the Visual Studio code editor. Follow the directions below that are specific to the OS you have installed on your laptop.

## Windows Users Getting Started

Before we can get started with installing the VScode editor, we need to install a basic Unix Operating System on your Windows machine. Windows Subsystem for Linux (WSL) comes with the Windows operating system, but you must enable it and install a Linux distribution before you can begin using it. There are detailed instructions on [setting up a WSL environment here](https://learn.microsoft.com/en-us/windows/wsl/setup/environment). This will allow you to use basic Unix commands in this class including "chmod" for making your python scripts executable, and "make test" to run the tests on your python code to make sure the code is correct.

You will need to complete the steps in the following sections in the instructions above:
* [Getting started](https://learn.microsoft.com/en-us/windows/wsl/setup/environment#get-started})
* [Set up your Linux Username and Password](https://learn.microsoft.com/en-us/windows/wsl/setup/environment#set-up-your-linux-username-and-password)
* [Upgrade packages in the default Ubuntu Linux Distribution](https://learn.microsoft.com/en-us/windows/wsl/setup/environment#update-and-upgrade-packages)
* [Install and set up VS Code](https://learn.microsoft.com/en-us/windows/wsl/setup/environment#use-visual-studio-code)

## Mac Users Getting Started

Because macOS comes with a Linux distribution pre-installed, you will just need to install the Visual Studio Code editor (VScode). Follow the directions on the VS Code website to install the version of [VS Code](https://code.visualstudio.com/) that is appropriate for your laptop.

## Installing the Python extensions for VS Code

Once VS Code is installed you will also need to install an extension for Python. VS Code can be used for programming in many different programming languages, so we will need to tell VSCode that we want to use Python. You can learn more about extensions [here](https://code.visualstudio.com/docs/introvideos/extend). Go the the VS Code menu, Select View -> Extensions, to pull up the "Extensions Market Place" on the left-hand panel. Search for and install "Python" by IntelliSense. This extension works alongside Python in Visual Studio Code to provide performant language support, linters, and debuggers for Python. You will learn about each of these in the days to come. They will be useful in formatting your code to make it beautiful, while also checking for mistakes and errors.

## Specifying the version of Python to use

As we discussed in setup2_python, there are many versions of python. For this class, we are going to use the same version of python to make troubleshooting easy, and ensure that you can easily use all of the Python modules that we will use in this class. Python modules are bits of code, written by other programmers, that we can use in our own programs (more on that to come!). We will use some of these modules to make sure our code is correctly formatted, and also for debugging. But, before we can use these modules, we need to tell VScode which version of Python to use. To do this, you can go to View -> Command Palette. Then in the search box type "Python: Select Interpreter". Choose the most recent version of python that you just installed 3.11.1

Now you are all set to start writing Python code in VS Code!

## Author

Bonnie Hurwitz <bhurwitz@arizona.edu> 

