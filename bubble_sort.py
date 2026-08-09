n = int(input("Enter number of elements: "))
a = list(map(int, input("Enter elements: ").split()))

for i in range(n - 1):
    for j in range(n - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print("Sorted array:", a)