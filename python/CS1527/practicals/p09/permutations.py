
def permutation(s1: str, s2: str):
    letters1: dict = {}
    letters2: dict = {}

    for c in s1:
        try:
            letters1[c] = letters1[c] + 1
        except KeyError:
            letters1[c] = 1

    for c in s2:
        try:
            letters2[c] = letters2[c] + 1
        except KeyError:
            letters2[c] = 1

    return letters1 == letters2


def permutation2(s1: str, s2: str):
    letters1 = set(s1)
    letters2 = set(s2)

    return letters1 == letters2



print(permutation2('catdog', 'dogcat'))
print(permutation2('catdog', 'dogcate'))
