ldr r1 , = number    @ load r1 with the address of number (address)
ldr r0 , [r1]        @ load r0 with the value at number (data at address)

add r0 , #3          @ add 3 to r0 (r0 = 13)

str r0 , [r1]        @ store r0 at number

@ declare a data section
.data                @ everything after the .data directive consists of data declarations
number: .word 15     @ define number

@ .word is a directive defining how the data following it is to be laid out in memory.
@ .word means a 4-byte "word", the size of an ARM register. So the number 15 is
@ stored in memory as a 32-bit value.
