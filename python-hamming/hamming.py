
# get the hamming distance between two strands of DNA
# if DNA strands have equal length
    # count different nucleotides
    # print the result

string_a = 'GAGCCTACTAACGGGAT'
string_b = 'CATCGTAATGACGGCCT'


def map_strings(str_a, str_b):
    d = dict();
    d['strand_a'] = list(map(str, str_a))
    d['strand_b'] = list(map(str, str_b))
    return d

def get_difference(strand_a, strand_b):
    print(strand_a)
    print(strand_b)
    return sum(i != j for i, j in zip(strand_a, strand_b))

def count_different_nucleotides():
    strands = map_strings(string_a, string_b)
    print(strands)
    strand_a = strands['strand_a']
    strand_b = strands['strand_b']

    if len(strand_a) == len(strand_b):
        print('yes')
        result = get_difference(strand_a, strand_b)
        print(result)
    else:
        print('DNA strands of different length cant\'t be used!')

count_different_nucleotides()
