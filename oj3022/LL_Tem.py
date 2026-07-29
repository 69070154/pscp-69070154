'''Temperature'''

Tem = float(input())
Let = input()
Ter = input()

k = Tem + 273.15
f = Tem * 9 / 5 + 32
r = Tem * 9/5 + 491.67
fc = (Tem - 32) * 5/9
fk =(Tem + 459.67) * 5/9
fr = Tem + 459.67
kc = Tem - 273.15
kf = Tem * 9/5 - 459.67
kr = Tem * 9 / 5
rc = (Tem - 491.67) * 5/9
rf =  Tem - 459.67
rk = Tem * 5 / 9

if Let =="C" and Ter =="K":
    print(f'{k :.2f}')
elif Let =="C" and Ter =="F":
    print(f'{f :.2f}')
elif Let =="C" and Ter =="R":
    print(f'{r :.2f}')
elif Let =="F" and Ter =="C":
    print(f'{fc :.2f}')
elif Let =="F" and Ter =="K":
    print(f'{fk :.2f}')
elif Let =="F" and Ter =="R":
    print(f'{fr :.2f}')
elif Let =="K" and Ter =="C":
    print(f'{kc :.2f}')
elif Let =="K" and Ter =="F":
    print(f'{kf :.2f}')
elif Let =="K" and Ter =="R":
    print(f'{kr :.2f}')
elif Let =="R" and Ter =="C":
    print(f'{rc :.2f}')
elif Let =="R" and Ter =="F":
    print(f'{rf :.2f}')
elif Let =="R" and Ter =="K":
    print(f'{rk :.2f}')
elif Let =="C" and Ter =="C":
    print(f'{Tem :.2f}')
elif Let =="K" and Ter =="K":
    print(f'{Tem :.2f}')
elif Let =="F" and Ter =="F":
    print(f'{Tem :.2f}')
elif Let =="R" and Ter =="R":
    print(f'{Tem :.2f}')
else:
    print("error")
