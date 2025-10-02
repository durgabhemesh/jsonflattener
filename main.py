# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from pack.utils import *
from pack.stringutils import *
import json

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def flatten(d,pkey="",sep="_"):
    dd={}

    for k,v in d.items():
        newkey = f"{pkey}{sep}{k}" if pkey else k

        if isinstance(v,dict):
            dd.update(flatten(v,newkey,sep))

        elif isinstance(v, list):
            for i, item in enumerate(v):
                if isinstance(item, dict):
                    dd.update(flatten(item, f"{newkey}{sep}{i}", sep))
                else:
                    dd[f"{newkey}{sep}{i}"] = item

        else:
            dd[newkey]=v
    return dd



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(add(1, 2))
    print(st("CHEK"))
    dd={}
    with open("data/data.json","r") as f:
        dd=json.load(f)
        print(flatten(dd))



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
