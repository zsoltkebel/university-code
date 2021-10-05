ldr r1, =destarr
ldr r2, =srcarr
loop:
ldr r0, [r2], #4
str r0, [r1], #4
cmp r0, #0
bne loop

.data
destarr: .word 0, 0, 0, 0, 0
srcarr: .word 7, 6, 5, 4, 0
