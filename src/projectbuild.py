"""
(Project Build) is a 'compiler' that gonna compile a .pb extension file
to build your project structure

Example:

mainfile.pb

<dir1>

-dir1-file.py
-dir1-file1.py

<dir2>

-dir2-file.py


That's gonna create a project structure like

dir1/
    file.py
    file1.py

dir2/
    file.py

"""

import sys
import configparser
import re
import os
from osCommand.oscommand import (
    _createFileInDir,
    _makeDir
)
from samfile.SamF import SamfReader

CONFIGPATTERNS = SamfReader()

CONFSAMFPATTERNS = CONFIGPATTERNS.read("patterns.samf")

PATTERNSDIR = CONFSAMFPATTERNS["Patterns"]["dirPat"]
PATTERNSFILE = CONFSAMFPATTERNS["Patterns"]["filePat"]


class PBReader:
    def __init__(self):

        self.pbfile = sys.argv[1]

        if len(sys.argv) < 2:
            raise TypeError("You didn't pass the file name")
        
        if not self.pbfile.endswith(".pb"):
            raise TypeError("This isn't a .pb file")

        
                    

    
    def create(self):
        
        with open(self.pbfile, "r") as file:
            content = file.read().strip().split("\n")
        if self.pbfile.endswith(".pb"):
            for text in content:
                if re.match(PATTERNSDIR, text):
                    _makeDir(text)
                    
                if re.match(PATTERNSFILE, text):
                    _createFileInDir(text)
        else:
            pass
    
# Structure project ['<dir1>', '', '-dir1-file.py', '-dir1-file1.py', '', '<dir2>', '', '-dir2-file.py']
# Files ['', 'OutroDir', 'file.py']
if __name__=="__main__":
    pbread = PBReader()
    pbread.create()