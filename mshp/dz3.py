def calc_sum_numbers(A = list()):
    if A == []:
        return 0
    else:
        summ = calc_sum_numbers(A[1:len(A-1)])
        summ = summ + A[0]
        return sum


if __name__ == '__main__':
    l = list(map(int, input().split())) #вызов split должен заканчиваться скобками
    summ = calc_sum_numbers(l) #неправильно прописаны названия, должно быть с маленькой буквы
    print("summ = ", summ)