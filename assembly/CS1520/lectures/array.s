mov r0 , #0         @ r0 will hold the sum
ldr r1 , = nums     @ r1 is the array address
loop:

ldr r2 , [r1]       @ load the current element in r2
add r1 , #4         @ advance r1 to the next element

ldr r2 , [r1] , #4  @ does the same as above (special use of ldr)

add r0 , r2         @ add r2 to the sum
cmp r2 , #0
bne loop            @ if r2 is not zero , repeat

.data
nums: .word 10 , 11 , 12 , 19 , 0  @ the array


@ load and increment instruction:
ldr r2, [r1]        @ r2 <- [r1]
ldr r2, [r1], #4    @ r2 <- [r1], and r1 <- r1 + 4

@ store and increment instruction:
str r2, [r1]        @ [r1] <- r2
str r2, [r1], #4    @ [r1] <- r2, and r1 <- r1 + 4
