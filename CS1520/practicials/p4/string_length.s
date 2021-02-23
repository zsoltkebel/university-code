@ An assembly code that computes the length of the string referenced in r1
@ Calculates the number of characters it contains not counting the final null character.

.global main
main:
ldr r1, =hello

mov r0, #0
loop:
ldrb r2, [r1], #1
cmp r2, #0
addne r0, #1        @ increment length counter (r0) if r2 is not final null character
bne loop            @ loop if null-terminated string end hasn't been reached

mov r7, #1 @ 1 = the code for system call "exit"
svc #0 @ make the system call

.data
hello: .asciz "hello"