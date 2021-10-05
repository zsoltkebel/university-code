# System calls
Each system call has a numerical code.

code | system call |
---- | ----------- |
1 | exit the program
3 | read data from an input device and store it in memory
4 | write data stored in some location in memory to some output device

Make system call using the `svc #0` instruction.

Before doing that, you must store the code for the system call in `r7` and extra information that the system call needs in `r0` and `r1`.

After the system call is done, registers `r0` and `r12` may be changed.

# Loading literal large values into registers
This won't work:
```assembly
mov r0, #877766
```
Use this instead:
```assembly
ldr r1, =number
ldr r0, [r1]

...

.data
number: .word 877766
```
Equivalent:
```assembly
ldr r0, =#877766
```