def main():
    n = int(input()) #задается тип str, а по условию int
    for i in range(1, n + 1): #по условию нужно чтобы цикл проходился от 1 до n включительно
        print(i**2, end=" ") #вывод должен быть в одну строку
    print()


if __name__ == "__main__":
    main()