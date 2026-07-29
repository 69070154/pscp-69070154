'''Brick'''

a = int(input())
b = int(input())
brick = int(input())
brick1 = brick // 5
if brick1 >= b:
    ais = brick - (b * 5)
    if a >= ais:
        print(ais)
    else:
        print("-1")
elif brick1 <= b:
    true = b - brick1
    aos = b - true
    gg = brick - (aos * 5)
    if a >= gg:
        print(gg)
    else:
        print("-1")
