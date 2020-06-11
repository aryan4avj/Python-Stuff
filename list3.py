def take_second(elem):
    return elem[1]

def take_first(elem):
    return elem[0]

if __name__ == '__main__':
    n = int(input())
    lst = [[input().split(),list(map(float, input().split()))] for i in range(n)]
    query_name = input()
    print(lst)