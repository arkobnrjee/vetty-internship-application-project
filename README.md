# Arko-Banerjee-Vetty-Intern-Project
A Flask application that renders text files into HTML pages.

# Files in project
<b>app.py</b> - Contains the Python code for running the flask application.

<b>file1.txt</b> - Sample text file for input to app.py.

<b>file2.txt</b> - Sample text file for input to app.py.

<b>file3.txt</b> - Sample text file for input to app.py.

<b>file4.txt</b> - Sample text file for input to app.py.

<b>requirements.txt</b> - Contains package and version requirements to run this project. Install with pip.

# Prerequisites

To run this project, the user should install Python 3, and optionally venv for a virtual running environment.

# Steps to Run
1. Download this project from github and extract the zip folder. Optionally, open the project in a virtual environment with venv.
2. Install requirements.txt using pip (comes with Python 3).
3. Run app.py with Python 3.
4. Open the locally hosted web server link given by app.py to make get queries. For an example get query, see below.

# Get Queries
Get queries on the local web server accept three parameters: file, begin, and end. These specify the file name, the starting line number (1-indexed), and the ending line number (1-indexed). By default, file="file1.txt", begin="begin" (this represents the beginning of the file), and end="end" (this represents the end of the file). For more specifics, look at the documentation for app.py.

A valid link would be localhost:5000/?file=file2.txt&begin=4&end=6 (the web server may be different).
