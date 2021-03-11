def distance(string_a: str, string_b: str):
    if len(string_a) == len(string_b):
        count = 0

        for i in range(0, len(string_a), 1):

            if string_a[i] != string_b[i]:
                count += 1
        return count

    else:
        print('DNA strands of different length cant\'t be used!')
        return -1
