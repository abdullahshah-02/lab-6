
# Q2: Write a Python function that takes a list of integers as
# input and returns a dictionary where keys are unique numbers
# from the list, and values are the frequencies of those numbers.


def count_frequencies(numbers):
    frequency_dict = {}

    for number in numbers:
        frequency_dict[number] = frequency_dict.get(number, 0) + 1

    return frequency_dict


numbers_list = [1, 2, 3, 1, 2, 4, 5, 1, 2, 6, 7, 7, 8]

result = count_frequencies(numbers_list)
print(result)
