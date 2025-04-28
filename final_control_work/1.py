import math


def count_even_divisors(n):
    if n == 0:
        return 0

    divisors = set()
    sqrt_n = math.isqrt(abs(n))
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            if i % 2 == 0:
                divisors.add(i)
            counterpart = n // i
            if counterpart % 2 == 0:
                divisors.add(counterpart)

    return len(divisors)


def main():
    numbers = []
    while True:
        line = input().strip()
        if line == "":
            break
        try:
            num = int(line)
            numbers.append(num)
        except ValueError:
            pass

    result_dict = {}
    for num in numbers:
        count = count_even_divisors(num)
        if count not in result_dict:
            result_dict[count] = []
        result_dict[count].append(num)

    for key in result_dict:
        result_dict[key].sort()

    print(result_dict)


if __name__ == "__main__":
    main()