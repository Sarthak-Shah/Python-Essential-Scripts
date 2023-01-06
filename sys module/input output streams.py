import sys

"""
What's Python Console:
The Python console is a command-line interface for interacting with the Python interpreter. It allows you to enter 
Python commands and execute them immediately, as well as to load and run Python scripts.

To start the Python console, open a terminal or command prompt and enter the command python. This will launch the Python
 interpreter and you will see a prompt where you can enter Python commands.
"""

"""
sys.stdin and sys.stdout are file objects in Python that represent the standard input and output streams, respectively.
sys.stdin is used to read input from the console or from a script, and sys.stdout is used to write output to the console 
or to a script.
Here's an example of how you can use sys.stdin and sys.stdout:

How to close stdin ?
    For UNIX based systems (Linux, Mac):
    Hello, you can type : Ctrl+d
    Ctrl+d closes the standard input (stdin) by sending EOF.
"""


def basicStdinStdout():
    # read multiple lines of input from stdin
    lines = sys.stdin.readlines()

    # process the input
    output = []
    for line in lines:
        # remove leading and trailing whitespace
        line = line.strip()
        # split the line into words
        words = line.split()
        # reverse the words and join them back together
        reversed_line = ' '.join(reversed(words))
        # add the reversed line to the output
        output.append(reversed_line)

    # write the output to stdout
    for line in output:
        sys.stdout.write(line + '\n')
        # print(line)

    # flush the output buffer
    sys.stdout.flush()

"""
You can also use the input() function to read input from the console, and the print() function to write output to the 
console. These functions use sys.stdin and sys.stdout under the hood.
For example, the following code is equivalent to the code above:
"""
def inputPrint():
    # read a line of input from the console
    line = input()
    # write a line of output to the console
    print(line)

"""
where do python save sys.stdout.write() data ?
    By default, the data written to sys.stdout using the write() method is printed to the console. However, 
    you can redirect sys.stdout to a file or to another stream, in which case the data will be written to the file or 
    stream instead of the console.
Here's an example of how you can redirect sys.stdout to a file:
"""


def stdoutToFile():
    # open a file for writing
    with open("stdoutTofile output.txt", "w") as f:
        # redirect stdout to the file
        some_ip = input("Enter something to get stored at file ! :  ")
        sys.stdout = f
        # write some data to stdout
        sys.stdout.write("Hello, student !\n")
        sys.stdout.write("This is a test by Sarthak Shah.\n")
        sys.stdout.write(some_ip)

    # stdout is automatically restored to the console when the with block ends

"""
This code opens a file called output.txt for writing, and then redirects sys.stdout to the file using the sys.stdout = f 
statement. Any data written to sys.stdout using the write() method will be written to the file instead of the console.

You can also redirect sys.stdout to a stream other than a file, such as a socket or a pipe. This allows you to write 
data to the stream using the write() method, and read the data from the stream using the appropriate functions for the 
stream.
"""

if __name__ == "__main__":
    stdoutToFile()
