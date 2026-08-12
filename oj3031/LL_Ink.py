'''INK'''
import math
def main():
    '''function'''
    s,n = map(int, input().split())
    for _ in range(n):
        x,y = map(int, input().split())
        r = x**2 + y**2
        area = 3.1416 * r
        t = area / s
        print(math.ceil(t))
main()
