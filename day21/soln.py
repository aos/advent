# Day 21
# What is the lowest non-negative integer value for register 0 that causes the
# program to halt after executing the fewest instructions?


def run(p1):
    seen = set()
    last = -1
    c = 0  # Reg 1

    while True:
        a = c | 65536  # Reg 3
        c = 6780005

        while True:
            c = (((c + (a & 255)) & 16777215) * 65899) & 16777215

            if 256 > a:
                if p1:
                    return c

                elif c not in seen:
                    seen.add(c)
                    last = c
                    break

                else:
                    return last
            else:
                a //= 256


# Part 1
print('Fewest instructions:', run(True))

# Part 2
print('Last non-repeating:', run(False))
