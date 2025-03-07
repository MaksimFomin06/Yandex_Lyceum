def main():
    n = int(input()) #По условию тип переменной - int, но переменная не используется(я бы ее удалил)
    a = list(map(int, input().split())) #два раза задается тип int, второй раз неправильно
    for i in range(0, len(a) - 1, 2):
        a[i], a[i + 1] = a[i + 1], a[i]
    print(*a) #вывод должен быть 'красивым'


if __name__ == '__main__':
    main()