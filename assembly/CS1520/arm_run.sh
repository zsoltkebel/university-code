#!/bin/bash
# created by: Zsolt Kebel

# This is a shell script to make it easier to assemble, link and run ARM source code in Codio.

# After saving the above file, we need to give it execute permission to make it runnable.
# You can set the execute permission as follows:
# $ chmod +x  my_script.sh //add execute permission

# use:
# $ ./arm_run.sh path/to/file

echo "Assembling and running file: $1.s"

arm-linux-gnueabi-gcc -o $1 $1.s # assemble, compile, link
if [ $? -eq 0 ]; then
    qemu-arm -L /usr/arm-linux-gnueabi/ $1 # running executable
    result=$?

    echo "Run successful."
    echo "Result: $result"
fi
