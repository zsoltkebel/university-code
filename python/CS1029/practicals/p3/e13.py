# Author: Zsolt Kébel
# Date: 23/10/2020

import collections

# question 7
A = {0, 2, 4, 6, 8, 10}
B = {1, 1, 2, 3, 4, 5, 6}
C = {4, 5, 6, 7, 8, 9, 10}

print("question 7")
print(f"a) {A & B & C}")
print(f"b) {A | B | C}")
print(f"c) {(A | B) & C}")
print(f"d) {(A & B) | C}")

# question 9
set1 = {1, 3, 5}
set2 = {1, 2, 3}

print("question 9")
print(f"{set1.symmetric_difference(set2)}")

# question 12
multiset_A = collections.Counter("aaabbc")
multiset_B = collections.Counter("aabbbdddd")

print("question 12")
print(f"a) {multiset_A | multiset_B}")
print(f"b) {multiset_A & multiset_B}")
print(f"c) {multiset_A - multiset_B}")
print(f"d) {multiset_B - multiset_A}")
print(f"e) {multiset_A + multiset_B}")
