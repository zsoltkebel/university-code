
def custom_hash(x):
    return x % 7


def hash_list(values):
    l = [[] for _ in range(7)]

    for value in values:
        l[custom_hash(value)].append(value)

    return l


print(hash_list([643, 7422, 7458, 5231, 32532, 6237, 899, 655]))
