@ Calling functions (bl)
@ Returning from functions (bx)
@ Using the stack to make nested function calls work properly (push and pop)

@ functions are subroutines that have return value (result)

@ EXAMPLE 1

.global main:
ldr r1, =string
b length
return:
@ ...

ldr r1, =other_string
b length @ BUG: infinite loop ! subroutine always return to return label above
@ ...

.data
string: .asciz "Some string"  @ 0 terminated string

@ arguments: r1 string address
@ returnsL r0 string length
length:
mov r0, #0
loop:
ldrb r2, [r1], #1
cmp r2, #0
addne r0, #1
bne loop
b return

@ inflexible: return address is hardcoded
@ can only return to the location marked with the return label
@ so we cannot call it from multiple places in opur code
@ THATS BAD!



@ =================
@ - lr register (r14) is dedicated to storing the return address in function calls. (lr = link register)
@ - bl (branch and link) branches to a label, and stores the address of the next instruction in lr
@ - bx (branch and exchange) returns from a function

@ EXAMPLE 

.global main
main:
ldr r1, =string
bl length
@ no need for a return label
@ ...
ldr r1, =other_string
bl length @ OK now
@ ...

@ arguments: r1 string address
@ returnsL r0 string length
length:
mov r0, #0
loop:
ldrb r2, [r1], #1
cmp r2, #0
addne r0, #1
bne loop
bx lr @ continue execution from after the function call


@ registers could still be unintentionally overwritten (r2 etc.)
@ solution is to save every register at first to the stack and then restore them


@ better soilution to implement a function:

@ arguments: r1 string address
@ returnsL r0 string length
length:
push {r1, r2} @ SAVING registers that we going to be using
mov r0, #0
loop:
ldrb r2, [r1], #1
cmp r2, #0
addne r0, #1
bne loop
pop {r1, r2} @ RESTORING registers that we used
bx lr @ continue execution from after the function call


@ with this method you can't have nested functions - couse infinite loop (there is only one lr which gets changed)


@ CORRECT FUNCTIONS:

@ arguments: r1 string address
@ returns: (nothing)
print_str:
push {r0-r7, lr}    @ save link register too
bl length       @ r0 = string length
                @ set up system call to print
mov r2, r0      @ r2 = number of bytes to print
                @ r1 = address of the string
mov r0, #1      @ r0 = output device (1 = std output)
mov r7, #4      @ r7 specifies system call (4 = write)
svc #0          @ make the system call
pop {r0-r7, lr}
bx lr           @ good to go, lr restored


@ arguments: r1 string address
@ returnsL r0 string length
length:
push {r1, r2, lr} @ SAVING registers that we going to be using
mov r0, #0
loop:
ldrb r2, [r1], #1
cmp r2, #0
addne r0, #1
bne loop
pop {r1, r2, lr} @ RESTORING registers that we used
bx lr @ continue execution from after the function call


@ cmp has to be called after each function call as they
@ might alter the cpsr (curretn program state register) that stores the result of comparison

@ do not change these registers:
r13
r14 @ lr
r15