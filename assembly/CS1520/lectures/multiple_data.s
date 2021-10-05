ldr r1 , = mass
ldr r0 , [r1]       @ r0 = [mass]
ldr r3 , = accel
ldr r2 , [r3]       @ r2 = [accel]
mul r4 , r0 , r2    @ r4 = r0 * r2
ldr r5 , = force
str r4 , [r5]       @ [force] = r4
.data
mass: .word 5
accel: .word 7
force: .word 0
