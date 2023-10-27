"""Reads the instructions from instructions.py file"""


def readFromInstructions():
    with open("stored_data/instructions.txt", "r", encoding="utf-8") as file_handler:
        contents = file_handler.read()
        print()
        print(contents)
        return contents
