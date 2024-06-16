from itertools import combinations, permutations, product

for a_n_digits, b_n_digits in product(range(1, 9), range(1, 9)):
    a_small = int("1" * a_n_digits)
    b_small = int("1" * b_n_digits)
    a_large = int("9" * a_n_digits)
    b_large = int("9" * b_n_digits)
    assert (
        a_n_digits + b_n_digits - 1  #
        <= len(str(a_small * b_small))
        <= len(str(a_large * b_large))
        <= a_n_digits + b_n_digits
    ), (a_small, b_small, a_n_digits, b_n_digits)
# Thus:          len(a) + len(b) = len(c) - {0,1}
#       len(a) + len(b) - len(c) = -{0,1}
# and:  len(a) + len(b) + len(c) = 9
# so, given len(a):
#       len(b) = -len(a) + len(c) - {0,1}
#       len(b) = -len(a) + (9 - len(a) - len(b)) - {0,1}
#       len(b) = -2*len(a) + 9 - len(b) - {0,1}
#     2*len(b) = -2*len(a) + 9 - {0,1}
#     2*len(b) = -2*len(a) + {8,9}
#       len(b) = -len(a) + {8,9}/2
#       len(b) = {4,5} - len(a)

values: set[int] = set()
digits = set(range(1, 10))
for a_n_digits in range(1, 5):
    for b_n_digits in [4 - a_n_digits, 5 - a_n_digits]:
        for a_digits in combinations(digits, a_n_digits):
            for b_digits in combinations(digits - set(a_digits), b_n_digits):
                c_digits = digits - set(a_digits) - set(b_digits)
                for a_ordered in permutations(a_digits, a_n_digits):
                    for b_ordered in permutations(b_digits, b_n_digits):
                        a = sum(a * 10**i for i, a in enumerate(a_ordered))
                        b = sum(b * 10**i for i, b in enumerate(b_ordered))
                        c = a * b
                        if sorted(str(a) + str(b) + str(c)) == sorted("123456789"):
                            values.add(c)
print(sum(values))
