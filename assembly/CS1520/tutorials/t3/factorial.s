@ Write assembly code that computes the factorial F
@ of the positive number N stored in
@ register r1: F = N*(N-1)*...*3*2*1.
@ The result should be stored in r0

mov r1, #10
mov r2, #1   @ counter
mov r0, #1
loop:
mul r0, r2
add r2, #1
cmp r2, r1
ble loop