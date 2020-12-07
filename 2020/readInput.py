import os
import sys


def read(input_file_path) -> str:
    with open(input_file_path, 'r') as f:
        return f.read()


#print(read(os.getcwd() + "/Day3/input.txt"))
print(sys.path.append("test"))
