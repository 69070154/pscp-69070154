'''ปราสาท'''
import math
def main():
    '''function'''
    x = int(input())
    l = math.ceil(math.sqrt(x))
    num = x - (l - 1) ** 2
    if not num % 2:
        print(2 * l - 3)
    else:
        print(2 * l - 2)
main()
