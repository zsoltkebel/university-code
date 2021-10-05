@ tutorial 4, exercise 3
ldr r1, =nums
ldr r0, [r1]
ldr r0, [r1], #4

.data
nums .word 3, 4, 5, 6

@ number stored in r0 after execution: 3?

@ tutorial 4, exercise 4
ldr r1, =nums
ldr r0, [r1], #4
ldr r0, [r1], #4

.data
nums .word 3, 4, 5, 6

@ number stored in r0 after execution: 4?