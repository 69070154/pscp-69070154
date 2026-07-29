'''Surprising vote'''
def main():
    '''function'''
    total = float(input())
    max_1 = float(input())
    min_1 = max(0.0,total - 2 * max_1)
    if (max_1 - min_1) > 2:
        print("Surprising")
    else:
        print("Not surprising")
main()
