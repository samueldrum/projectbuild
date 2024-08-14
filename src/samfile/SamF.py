import re

class SamfReader:
    """This class is just for put your variable into a samf file"""

    def read(self, path):
        # Check if the file is .samf
        if not path.endswith(".samf"):
            raise ValueError("This file is not a 'samf' file")
        
        # Read the file content
        with open(path, "r") as file:
            content = file.read().strip().split("\n")
        
        # The first line is the Section
        the_first = content[0]
        dict_ = {}

        # Check and process the section
        if re.search(r"<.*>", the_first):
            key = the_first.strip("<>")
            dict_[key] = {}
            
            # Precess each line after the section process
            for line in content[1:]:
                if "=" in line:
                    sub_key, sub_value = map(str.strip, line.split("=", 1))
                    
                    # Convert the numeric values into a integer value
                    if sub_value.isnumeric():
                        sub_value = int(sub_value)
                    if sub_key.isnumeric():
                        sub_key = int(sub_key)

                    # Put them in a dictionary
                    dict_[key][sub_key] = sub_value

                else:
                    raise TypeError("You have too put the = symbol attribute")
        
        if re.search(r"<<.*>>", the_first):
            return eval(the_first.strip("<>"))
        
        return dict_

