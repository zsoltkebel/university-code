### How to assemble and run ARM code in [Codio](https://codio.co.uk)

1. Run the assembler, create .o file

    `arm-linux-gnueabi-as -o <filename>.o <filename>.s`

2. Creat an executable file from source code

    `arm-linux-gnueabi-gcc -o <filename> <filename>.s`

3. Run the executable file

    `qemu-arm -L /usr/arm-linux-gnueabi/ <filename>`

### Example

To assmeble and run hello.s:

`arm-linux-gnueabi-gcc -o hello hello.s`

`qemu-arm -L /usr/arm-linux-gnueabi/ hello`

### Useful terminal commands

The number stored in register r0 is used as the “result” of the program. After we run any
command in the terminal, we can see what the result of the command was, by typing the following command:

`echo $?`

Prints the numerical value corresponding to the result of the last command executed. Here we use the program’s result to communicate
the result of our computation.

### How to assemble ARM code on Mac [(source)](https://www.quora.com/How-do-I-run-ARM-Assembly-language-on-a-Mac)

You just can't run it on a Mac since most Macs don't have ARM CPUs. If you install Xcode with iOS support, you can compile ARM code:

1. Create a assembly file with “.s” extension

    `$ touch hello.s`

2. compile with llvm-gcc

    `$ clang -arch armv7s -c hello.s`

resulting file is ARM object file

$ file foo.o

foo.o: Mach-O object arm

and you can disassemble it

`$ otool -v -t foo.o`

### Useful commands
command | description
------- | -----------
`arm-linux-gnueabi-as -o <filename>.o <filename>.s` | Run the assembler, translate hello.s into a file containing machine instructions that the computer can run. hello.o, contains the CPU instructions corresponding to our assembly program
`arm-linux-gnueabi-gcc -o <filename> <filename>.s` | Compile and create executable file.
`qemu-arm -L /usr/arm-linux-gnueabi/ <filename>` | Run the executable
`echo` | Repeats what you tell it to repeat
`$?` | The numerical value corresponding to the result of the last command executed
