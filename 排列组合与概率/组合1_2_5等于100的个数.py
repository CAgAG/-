"""
    x + 2y + 5z = 100
        -> x + 5z = 100 - 2y
            -> 100 - 2y 是偶数 且 x + 5z <= 100
                -> z=[0...20]

    分析:
        z=0, x=[0, 2, 4 ... 100], len= (100+2)/2
        z=1, x=[1, 3, 5 ... 95], len = (95+2)/2
        z=2, x=[0, 2, 4 ... 90], len= (90+2)/2
        ...
        z=19, x=[1, 3, 5], len=(5+2)/2
        z=20, x=0, len=(0+2)/2
"""


def comb():
    count = 0
    z = 0
    while z <= 100:
        count += (z + 2) // 2
        z += 5
    return count


if __name__ == '__main__':
    print(comb())
