def quick_sort(a):
    if len(a) <= 1:
        return a

    pivot = a[0]

    left = []
    right = []

    for x in a[1:]:
        if x < pivot:
            left.append(x)
        else:
            right.append(x)

    return quick_sort(left) + [pivot] + quick_sort(right)


a = list(map(int, input("Enter elements: ").split()))

a = quick_sort(a)

print("Sorted array:", a)