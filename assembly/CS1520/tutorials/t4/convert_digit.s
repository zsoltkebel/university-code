ldr r1, =num
ldr r2, =char
ldr r0, [r1]
add r0, #48
strb r0, r2

.data
num: .byte 4
char: .ascii "hello"