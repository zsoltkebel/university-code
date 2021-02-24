# Author: Zsolt Kébel
# Date: 23/02/2021

def subsets(set, i=0, ):
    if i >= len(set):
        return set

    sub = set
    element = sub.pop(0)

    if len(set) == 2:
        sub = {1, 2}
        return [element, set]
    else:
        return [element].append(subsets(sub.append(element), i))
        # return [subsets(set.pop(i)), subsets(set[1:]), subsets(set.remove(1))]


s = [1, 2, 3]
print(subsets(s))
