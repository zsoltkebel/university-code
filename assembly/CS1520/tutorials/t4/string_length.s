@ TUTORIAL 4, EXERCISE 6
@ Suppose r1 contains the address of a null-terminated string. Write assembly code
@ that computes the length of the string – that is, how many characters it has,
@ not counting the final null character.

.global main
main:
ldr r1, =hello

mov r0, #0
loop:
ldrb r2, [r1], #1
cmp r2, #0
addne r0, #1        @ increment length counter (r0) if r2 is not final null character
bne loop            @ loop if null-terminated string end hasn't been reached

.data
hello: .asciz "hello"
