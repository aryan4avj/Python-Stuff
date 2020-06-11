
if __name__ == '__main__':      #for input like 2\n 2\ 3\n
    n = int(input())
    arr = list()
    for i in range(n):
        arr.append(int(input()))
    z = max(arr)
    while(arr.count(z)):
        arr.remove(z)
    print(max(arr))



# if __name__ == '__main__':      #for input like 5\n 2 3 3 4 5 5
#     n = int(input())
#     inpt = input().split()
#     arr = []
#     for elm in inpt:
#         arr.append(int(elm))
#     z = max(arr)
#     while(arr.count(z)):
#         arr.remove(z)
#     print(max(arr))


# if __name__ == '__main__':      #for input like 5\n 2 3 3 4 5 5
#     n = int(input())
#     arr = list(map(int, input().split()))
#     arr =  [i for i in arr if i != max(arr)]
#     print(max(arr))
