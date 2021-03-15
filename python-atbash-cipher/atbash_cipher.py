# function inversing indexes of alphabet
# encoding => comparing input to alphabet list and find indexes of used letters
# store indexes used
# compare to reversed list. use the letters at stored index (reversed alphabet letter)




string = 'no'


def encode(input: str):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    reversed_alphabet = alphabet[::-1]

    print('reversed_aphabet: ', reversed_alphabet)
    print('input: ', input)
    # print('input len: ', len(input))
    print(alphabet)
    # print('alphabet len: ', len(alphabet))
    result = []

    for i in range(len(input)):
        # print('In i loop', i, alphabet[i])

        print('i: ', i)
        print('alphabet.find: ', alphabet.find(input[i]))
        found_index = alphabet.find(input[i])
        print('found_index: ', found_index)
        result.append(found_index)

    print('result: ', result)

    encoded_string = ''

    for j in range(len(result)):
        encoded_string = encoded_string + reversed_alphabet[result[j]]
        print('encoded_string: ', encoded_string)

    print('oput loop j: ', encoded_string)
    return encoded_string

def decode():
    encoded_string = encode(string)
    print('///////////////////////////')
    print('in decode function - result: ', encoded_string)





    #
    #     # for j in range(len(alphabet_list), 0, 1):
    #     #     encoded_alphabet = []
    #     #     print('in j loop before permutation', encoded_alphabet)
    #     #
    #     #     encoded_alphabet[j] = alphabet_list[i]
    #     #
    #     #     print(alphabet_list)


# encode(string)
decode()