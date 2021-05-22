"""
This program contains the code to run the Flask application. It creates a locally hosted web server and provides the user with the link. It processes get requests made by the user.

URL Parameters
    - file: This field is for the name of the input text file. It can be just a file name, or a path. The program renders this file into an HTML page.
        If not specified, the program renders the file "file1.txt", one of the sample files provided in this project.
    - begin: If the user wishes only for a certain section of the file to render, this variable is to specify the start line number.
        - If not specified, the program starts at the beginning of the file. This can also be accomplished by setting the begin field to the word "begin".
        - If the file is empty, this parameter is ignored and nothing is rendered (though no error is thrown).
        - IMPORTANT NOTE: The field begin is 1-indexed. That is, counting lines starts at 1, not 0.
    - end: If the user wishes only for a certain section of the file to render, this variable is to specify the end line number.
        - If not specified, the program terminates at the end of the file. This can also be accomplished by setting the end field to the word "end".
        - If the file is empty, this parameter is ignored and nothing is rendered (though no error is thrown).
        - IMPORTANT NOTE: The field begin is 1-indexed. That is, counting lines starts at 1, not 0.

Exceptions Thrown
    - If the file provided does not exist (or if the field is left empty and file1.txt does not exist), an error is thrown.
    - If the file contains characters that cannot be decoded by Python, an error is thrown.
    - If the begin parameter is set to a non-integer value besides the word "begin", an error is thrown.
    - If the end parameter is set to a non-integer value besides the word "end", an error is thrown.
    - If the begin and end parameters do not define a valid range, an error is thrown.
        - This can happen if either parameter is out of the file's range, or if begin > end.
        - If the file is empty, both parameters are ignored and nothing is rendered, though no error is thrown.
        
Some examples of valid queries (note that the server name may vary):

localhost:5000
    - Renders the entirety of file1.txt
localhost:5000/?file=file2.txt&begin=2&end=3
    - Renders line 2 and 3 of file2.txt
localhost:5000/?file=/Users/username/a.txt?begin=7
    - Renders Lines 7 through the end of the file /Users/username/a.txt (This only works if the given file actually exists).
localhost:5000/?file=file4.txt&begin=begin&end=end
    - Renders the entirety of file4.txt. It was not necessary to set begin=begin or end=end, but this is valid.
"""


from flask import Flask, Response, request
from os import path

app = Flask(__name__)
@app.route('/')


def index():
    # Get URL parameters.
    filename = request.args.get("file", default="file1.txt", type=str)
    begin = request.args.get("begin", default="begin", type=str)
    end = request.args.get("end", default="end", type=str)
    
    # First exception case: file does not exist.
    if not path.exists(filename):
        return "Error: the file " + filename + " could not be found. Please check the name and location of the file and try again."

    with open(filename, "r") as input_file:
        # Second exception case: file contains unreadable characters.
        try:
            lines = input_file.readlines()
        except UnicodeDecodeError:
            return "Error: the file " + filename + " contains unreadable characters and could not be decoded."
        
        # If the file is empty, just return an empty file.
        if not len(lines):
            return ""
        
        # Determine beginning and end points.
        begin_line = 0
        end_line = len(lines) - 1
        if begin != "begin":
            # Check invalid inputs.
            try:
                begin_line = int(begin) - 1
            except ValueError:
                return "Error: the URL parameter \"begin\" must either have an integer value, or must be set to the word \"begin\". Please check the \"begin\" parameter and try again."
        if end != "end":
            try:
                end_line = int(end) - 1
            except ValueError:
                return "Error: the URL parameter \"end\" must either have an integer value, or must be set to the word \"end\". Please check the \"end\" parameter and try again."

        # Finally, we also need to make sure the bounds are functional.
        if begin_line < 0:
            return "Error: the URL parameter \"begin\" must be positive. Please check the \"begin\" parameter and try again."
        if begin_line >= len(lines):
            return "Error: the URL parameter \"begin\" cannot exceed the number of lines in the file. Please check the \"begin\" parameter and try again."
        if end_line < 0:
            return "Error: the URL paramter \"end\" must be positive. Please check the \"end\" parameter and try again."
        if end_line >= len(lines):
            return "Error: the URL paramter \"end\" cannot exceed the number of lines in the file. Please check the \"end\" parameter and try again."
        if begin > end:
            return "Error: the URL parameter \"begin\" cannot exceed the parameter \"end\". Please specify a valid interval of lines to render and try again."
        content = "<br>".join(lines[begin_line : end_line + 1])
        return Response(content, mimetype="text/html")


if __name__ == "__main__":
    app.run()
