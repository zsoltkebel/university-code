# Author: Zsolt Kébel
# Date: 26/01/2021

def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True


num = int(input("Number: "))

print(num, "is prime?", is_prime(num))
