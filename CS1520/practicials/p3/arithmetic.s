.global main @ mark this as the entry
main: @ point of the program
@ calculate the sum S = m + (m+1) + . . . + n
@ using the formula S = (n+m) *( n-m+1)/2
mov r4 , #1 @ m=1
mov r5 , #10 @ n=10
mov r0 , r4 @ r0 = m
add r0 , r5 @ r0 = m+n
mov r1 , r5 @ r1 = n
sub r1 , r4 @ r1 = n-m
add r1 , #1 @ r1 = n-m+1
mul r0 , r1 @ r0 = (m+n ) ( n-m+1)
lsr r0 , #1 @ r0 = (m+n ) ( n-m+1)/2
mov r7 , #1 @ make the system call
svc #0 @ to exit the program
.end