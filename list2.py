def take_second(elem):
    return elem[1]

def take_first(elem):
    return elem[0]

if __name__ == '__main__':
    n= int(input())
    lst = [[input(),float(input())] for i in range(n)]
    lst = sorted(lst, key=take_first)
    z = min(lst, key=take_second)
    lst = [i for i in lst if i[1]!=z[1]]
    z = min(lst, key=take_second)
    t = [i[0] for i in lst if i[1]==z[1]]
    print(*t, sep='\n')
        