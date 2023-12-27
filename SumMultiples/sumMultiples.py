def sum_of_multiples(n, k):
    total_sum = 0

    # Iterate from k to n
    for i in range(k, n + 1):
        if i % k == 0:
            total_sum += i

    # Return the final sum
    return total_sum
n_value = 10
k_value = 3
result = sum_of_multiples(n_value, k_value)
print(result)
