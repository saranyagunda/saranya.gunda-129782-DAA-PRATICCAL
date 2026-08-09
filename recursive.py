import time

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


n = 5

start = time.perf_counter()
result = factorial(n)
end = time.perf_counter()

print("Recursive Result:", result)
print("Actual Execution Time:", end - start, "seconds")
print("Time Complexity: O(n)")
