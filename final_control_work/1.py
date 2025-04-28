import math


def count_even_divisors(n):
    if n == 0:
        return 0
    n = abs(n)
    count = 0
    sqrt_n = math.isqrt(n)
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            if i % 2 == 0:
                count += 1
            counterpart = n // i
            if counterpart != i and counterpart % 2 == 0:
                count += 1
    return count


def main():
    import sys
    numbers = []
    for line in sys.stdin:
        stripped_line = line.strip()
        if stripped_line == "":
            continue
        try:
            num = int(stripped_line)
            numbers.append(num)
        except ValueError:
            pass
    
    result_dict = {}
    for num in numbers:
        count = count_even_divisors(num)
        if count > 0:
            count -= 1
        if count not in result_dict:
            result_dict[count] = []
        result_dict[count].append(num)
    
    for key in result_dict:
        result_dict[key].sort()
    
    print("{")
    keys = sorted(result_dict.keys())
    for i, key in enumerate(keys):
        print(f"  {key}: [")
        for j, num in enumerate(result_dict[key]):
            if j != len(result_dict[key]) - 1:
                print(f"    {num},")
            else:
                print(f"    {num}")
        if i != len(keys) - 1:
            print("  ],")
        else:
            print("  ]")
    print("}")


if __name__ == "__main__":
    main()