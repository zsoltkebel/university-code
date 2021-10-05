mov r0, #1    @ output device (1: std output)
ldr r1, =msg  @ address of the string
mov r2, #15   @ number of bytes in the string
mov r7, #4    @ 4 = code for write system calls
svc #0        @ make the system call (0 doesnt matter, its a convention, number is ignored)

mov r7, #1    @ 1 = code for exit system call
svc #0        @ make the system call

.data
msg: .asciz "What's up doc?\n"  @ the string