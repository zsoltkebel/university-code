@ TUTORIAL 4, EXERCISE 5
@ Suppose r1 contains the address of an array of positive integers,
@ whose last element is 0 (0 only appears as the last element in the array,
@ and nowhere else). Write assembly code that finds the maximum number
@ in the array and stores it in r0.

mov r0, #0
ldr r1, =nums
loop:
ldr r2, [r1], #4    @ load next element
cmp r2, r0
movgt r0, r2
cmp r2, #0
bne loop

.data
nums: .word 1, 3, 10, 6, 0
