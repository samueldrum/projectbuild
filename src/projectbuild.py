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
import re
import argparse
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

        self.parser = argparse.ArgumentParser(description="Process the .pb file")
        self.filename = sys.argv[1]
        # The argument for the pb file
        self.parser.add_argument("file", type=str, help=f"Processing {self.filename}")
        # The argument for version
        self.parser.add_argument("--version", type=str, help="The projectbuild version")

        # The create argument, to create the file
        self.parser.add_argument("--create", action="store_true",  help="Create the project structure")


        self.args = self.parser.parse_args()

        if not self.args.file.endswith(".pb"):
            raise TypeError("This isn't a .pb file")
        
        if self.args.create:
            self.__create()

        

    
    def __create(self):
        
        with open(self.args.file, "r") as file:
            content = file.read().strip().split("\n")

        for text in content:
            if re.match(PATTERNSDIR, text):
                _makeDir(text)
                
            if re.match(PATTERNSFILE, text):
                _createFileInDir(text)


            
    

if __name__=="__main__":
    pbread = PBReader()
