input_1 = [1, 2, 3, 1, 1, 3]

input_2 = [1, 1, 1, 1]

input_3 = [1, 2, 3]


def all_pairs(arr):
    results = []
    for i in range(len(arr)):
        x = arr[i]
        for j in range(i + 1, len(arr)):
            y = arr[j]
            if x == y:
                results.append([i, j])
    print(results)
    return results


all_pairs(input_1)
all_pairs(input_2)
all_pairs(input_3)
