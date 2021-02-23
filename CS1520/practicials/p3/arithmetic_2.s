.global main @ mark this as the entry
main: @ point of the program
@ calculate the sum A = x^2 + 2axy + y^2
@ initial values
mov r4 , #2 @ x=2
mov r5 , #3 @ y=3
mov r6 , #4 @ a=4

@ r0 = x^2
mov r0, r4 @ r0 = x
mul r0, r4 @ r0 = x^2
@ r1 = y^2
mov r1, r5 @ r1 = y
mul r1, r5 @ r1 = y^2
@ r2 = 2axy
mov r2, #2 @ r2 = 2
mul r2, r6 @ r2 = 2a
mul r2, r4 @ r2 = 2ax
mul r2, r5 @ r2 = 2axy
@ calculating the result in r0 = A = x^2 + 2axy + y^2
add r0, r1 @ r0 = x^2 + y^2
add r0, r2 @ r0 = x^2 + 2axy + y^2

mov r7 , #1 @ make the system call
svc #0 @ to exit the program
.end