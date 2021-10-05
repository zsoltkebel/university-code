mov r0, #0   @ step 1: S=0
mov r1, #10  @ step 1: N=10
mov r2, #1   @ step 2: i=1
loop:
add r0, r2   @ step 3: S=S+i
add r2, #1   @ step 4: i=i+1
cmp r2, r1   @ step 5: if i <= N,
ble loop     @ repeat