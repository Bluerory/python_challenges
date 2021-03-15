# function inversing indexes of alphabet
# encoding => comparing input to alphabet list and find indexes of used letters
# store indexes used
# compare to reversed list. use the letters at stored index (reversed alphabet letter)
#
# string = 'no'
#

def encode(input: str):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    reversed_alphabet = alphabet[::-1]
    input = input.lower()
    print('input: ', input)
    print('input len: ', len(input))

    result = []

    for i in range(len(input)):

        found_index = alphabet.find(input[i])

        result.append(found_index)

    print('result: ', result)

    encoded_string = ''

    for j in range(len(result)):
        encoded_string = encoded_string + reversed_alphabet[result[j]]

    print('encoded_string: ', encoded_string)

    return encoded_string


def decode():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    reversed_alphabet = alphabet[::-1]

    encoded_string = encode(string)
    print('///////////////////////////')
    print('in decode function - result: ', encoded_string)

    result = []

    for i in range(len(encoded_string)):
        index_in_encoded = reversed_alphabet.find(encoded_string[i])
        result.append(index_in_encoded)
    print(result)

    decoded_string = ''

    for j in range(len(result)):
        decoded_string = decoded_string + alphabet[result[j]]

    return decoded_string
