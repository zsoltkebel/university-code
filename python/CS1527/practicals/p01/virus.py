# Author: Zsolt Kébel
# Date: 26/01/2021

# A Python program that takes no input and produces a copy of its own source code as its only
# output (this is like a computer virus that can replicate itself).

import os

counter = 0
for filename in os.listdir():
    if filename.startswith("virus") and filename.endswith(".py"):
        counter += 1

with open("virus.py", "r") as source, open(f"virus_{counter}.py", "a") as target:
    content = source.read()
    print(content)
    target.write(content)

source.close()
target.close()
