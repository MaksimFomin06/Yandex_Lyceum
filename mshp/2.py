def main(): #ошибка синтаксиса, нужно двоеточие
    n = int(input())
    a = []
    sum = 0
    a = list(map(int, input().split()))
    for i in range(n): #ошибка синтаксиса, нужно двоеточие
        sum+= a[i] ** 2
    if sum // 10000 >= 1 and sum // 10000 <= 9:
        print("YES")
    else: #ошибка синтаксиса, нужно двоеточие
        print("NO")


if __name__ == "__main__": #ошибка синтаксиса, нужно двоеточие
    main()