@ Write assembly code that computes the absolute value of
@ the number in register r1, and stores the result in r0.

mov r1, #-15
mov r0, r1
cmp r1, 0
mullt r0, #-1