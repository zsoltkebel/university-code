.global main
main:
ldr r1, =intstring @ load address of string representing a number to r1

mov r0, #0 @ r0 going to store the result integer number
mov r4, #10 @ multiply by this register each time in the loop

loop:
ldrb r3, [r1], #1 @ load the current character to r3 and r1 <- r1 + 1
cmp r3, #0 @ end of string
beq finish

sub r3, #48 @ retrieve actual number from characted code to r3
mul r0, r4 @ multiply by 10
add r0, r3
bne loop

finish:
mov r7, #1 @ 1 = the code for system call "exit"
svc #0 @ make the system call

.data
intstring: .asciz "102" @ the string representing an integer

@ for some reason result is max 255
