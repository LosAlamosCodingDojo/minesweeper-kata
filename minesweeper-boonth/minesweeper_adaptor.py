"""
minesweeper adaptor, used for testing

this module lets us test minesweeper.py without having to know how
minesweeper.py works internally

"""

import os
import subprocess
import sys
import tempfile

python_exe = sys.executable
script = 'minesweeper.py'

def run_minesweeper(input_string):
    """Given a string, give it to minesweeper as a file, and return the
    output of minesweeper as a string."""

    # create temporary file, write input string to file, and close file
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(input_string)
    temp_file.close()

    # call minesweeper with temporary file, while capturing standard out
    pipe = subprocess.Popen([python_exe, script, temp_file.name], 
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    # get standard out
    output = pipe.communicate()[0]

    # delete temporary file
    os.unlink(temp_file.name)

    return output

