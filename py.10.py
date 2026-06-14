numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("The largest number is:", largest)