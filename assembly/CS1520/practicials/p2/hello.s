.global main

main:
mov r7, #4
mov r0, #1
ldr r1, =message
mov r2, #16
svc 0

mov r7, #1
svc 0

.data
message: .ascii "what's up, doc?\n"

.end
