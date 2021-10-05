@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@
@ Read a string from the terminal .
@ ( only the first 99 characters are read )
@
@ arguments : r1 : address of string used to
@ store result
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@
read_str:
push {r0-r7 , lr}
mov r0 , #0 @ 0 = std input ( termina l )
mov r2 , #100 @ max num o f bytes to read
mov r7 , #3 @ 3 = " read " system call
svc #0 @ make the system c a l l
pop {r0-r7 , lr }
bx lr
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@
@ Print an integer on the screen , followed
@ by a newline . ( uses C library function )
@
@ arguments : r1 : integer to be printed
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@
.global printf
print_num:
push {r0-r3 , lr}
ldr r0 , =fmt
bl printf
pop {r0-r3 , lr}
bx lr
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@


@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@
@ arguments: r1 string representing a number
read_num:
push {r1-r4, lr}
ldr r1 , =input
bl read_str @ read input from t e rmina l

mov r0, #0 @ r0 going to store the result integer number
mov r4, #10 @ multiply by this register each time in the loop

loop:
ldrb r3, [r1], #1 @ load the current character to r3 and r1 <- r1 + 1
cmp r3, #10 @ end of string
beq finish

sub r3, #48 @ retrieve actual number from characted code to r3
mul r0, r4 @ multiply by 10
add r0, r3
bne loop

finish:
pop {r1-r4, lr}
bx lr
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@

.global main
main:
bl read_num
mov r1, r0

bl print_num @ print the ASCII code of
@ the first character
mov r7 , #1
svc #0
.data
fmt: .asciz "%d\n"
input: .space 100
