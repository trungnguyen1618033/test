import string

input_1 = "bbbaacdafe"

input_2 = "aabbb"

input_3 = "bbbbcbaacdafe"


def is_beautiful_string(input_string):
    counts = [0 for x in range(0, 26)]
    for x in input_string:
        y = ord(x) - ord("a")
        counts[y] += 1
    for i in range(len(counts) - 1):
        x = counts[i]
        y = counts[i + 1]
        if x < y:
            return False
    return True


print(is_beautiful_string(input_1))
print(is_beautiful_string(input_2))
print(is_beautiful_string(input_3))
