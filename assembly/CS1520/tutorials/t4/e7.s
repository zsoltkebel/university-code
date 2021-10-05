@ What does [.align 2] directive do?

.align 2

.data
hello: .asciz "hello"
nums: .word 10, 11, 12, 0

@ a word is 4 byte -> 32-bit
@
@ [  h  ]
@ [  e  ]
@ [  l  ]
@ [  l  ]
@
@ [  o  ]
@ [  0  ]
@ [  ■  ]  --|
@ [  ■  ]    |
@            | Next number which is stored in a word (4 bytes)
@ [  ■  ]    |
@ [  ■  ]  --|
@ [     ]
@ [     ]

.data
hello: .asciz "hello"
.align 2                    @ .align n aligns data to the 2^n-byte boundary
nums: .word 10, 11, 12, 0

@ a word is 4 byte -> 32-bit
@
@ [  h  ]
@ [  e  ]
@ [  l  ]
@ [  l  ]
@
@ [  o  ]
@ [  0  ]
@ [  0  ]
@ [  0  ]
@
@ [  ■  ]  --|
@ [  ■  ]    | Next number which is stored in a word (4 bytes)
@ [  ■  ]    |
@ [  ■  ]  --|