def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


sample_list = [9, 2, 3, 5, 8]
result = sum_list(sample_list)
print("Sum of samplelist :", result)

