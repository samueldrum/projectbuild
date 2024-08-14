import os

def _createFileInDir(text):
        dirAndfile = text.split("-")
        dirPath = os.path.relpath(dirAndfile[1])
        filename = dirAndfile[2]
        completePath = os.path.join(dirPath, filename)

        if not os.path.exists(dirPath):
            os.makedirs(dirPath)
        
        with open(completePath, "w") as file:
            file.write(f"# {filename} created on {dirPath}")


def _makeDir(text):
    text = text.strip("<>")
    os.system(f"mkdir {text}")
    print(f"dir {text} was created sucessfully")

