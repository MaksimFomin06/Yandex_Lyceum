def main():
    arr = input().split()
    arr = [int(i) for i in arr]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]: #должно быть сравнение а не сложение, иначе условие всегда будет истинным
                arr[i], arr[j] = arr[j], arr[i]
    print(*arr, end="\n") #убрал непонятный для меня вывод


if __name__ == "__main__":
    main()