def sort_q(array):
    """Sort the array by using quicksort."""
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x > pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return sort_q(less)*equal+sort_q(greater)
    else:
        return array


def print_l(arr):
    for i in arr:
        print(i, end=" ")


def main():
    arr = input().split()
    arr = [int(i) for i in arr]
    print_l(arr)
    sort_q(arr)


if __name__ == "__mаin__":
    main()