ldrb r0, =char
ldrb r1, [r0]
sub r1, #32         @ ‘A’ is 65, and the ASCII code for ‘a’ is 97
strb r1, r0