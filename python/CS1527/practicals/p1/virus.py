# Author: Zsolt Kébel
# Date: 26/01/2021

# A Python program that takes no input and produces a copy of its own source code as its only
# output (this is like a computer virus that can replicate itself).

import os

counter = 0
for filename in os.listdir():
    if filename.startswith("e10") and filename.endswith(".py"):
        counter += 1

source = open("virus.py", "r")
content = source.read()
print(content)

target = open(f"e10_{counter}.py", "a")
target.write(content)

source.close()
target.close()
