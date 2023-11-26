# Q1: Create a function in Python that takes two strings as input and
# determines if they are anagrams. Utilize a hash table to efficiently
# compare the character frequencies in the two strings.

def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2):
        return False

    char_freq_1 = {}
    char_freq_2 = {}

    for char in str1:
        char_freq_1[char] = char_freq_1.get(char, 0) + 1

    for char in str2:
        char_freq_2[char] = char_freq_2.get(char, 0) + 1

    return char_freq_1 == char_freq_2


string1 = "listen"
string2 = "silent"

if are_anagrams(string1, string2):
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")
