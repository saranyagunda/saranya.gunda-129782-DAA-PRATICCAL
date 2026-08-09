import time

def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


n = 5

start = time.perf_counter()
result = factorial(n)
end = time.perf_counter()

print("Iterative Result:", result)
print("Actual Execution Time:", end - start, "seconds")
print("Time Complexity: O(n)")