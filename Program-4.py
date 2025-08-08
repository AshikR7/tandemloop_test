"""
Get the total count of number listed in the dictionary which is multiple of [1,2,3,4,5,6,7,8,9]
  (examples)
  input: [1,2,8,9,12,46,76,82,15,20,30]
  Output:
    {1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}
"""

def count_multiples():
    max_length = int(input("How many numbers do you want to enter? "))
    numbers = []

    for i in range(max_length):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)
    result = {}
    for i in range(1, 10):
        count = sum(1 for num in numbers if num % i == 0)
        result[i] = count
    print(result)

count_multiples()
