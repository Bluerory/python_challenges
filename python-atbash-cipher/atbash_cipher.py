# function inversing indexes of alphabet
# encoding => comparing input to alphabet list and find indexes of used letters
# store indexes used
# compare to reversed list. use the letters at stored index (reversed alphabet letter)
#
string = 'testing123testing'
#
alphabet = 'abcdefghijklmnopqrstuvwxyz'
reversed_alphabet = alphabet[::-1]

def encode(input: str):

    punct_and_space = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    for elem in input:
        if elem in punct_and_space:
            input = input.lower().replace(elem, "")
        else:
            input = input.lower()

    print('input after lower() and replace(): ', input)
    print('input len: ', len(input))

    result = []

    for i in range(len(input)):
        print(input[i])
        if input[i].isdigit():
            found_index = input[i]
        else:
            found_index = alphabet.find(input[i])

        result.append(found_index)

    print('result: ', result)

    encoded_string = ''

    for j in range(len(result)):
        if j % 5 == 0 and j != 0:
            encoded_string = encoded_string + " " + reversed_alphabet[result[j]]
            print("added space - index: ", j)
        elif type(result[j]) == str:
            encoded_string = encoded_string + result[j]
        else:
            encoded_string = encoded_string + reversed_alphabet[result[j]]
        print(j)
    print('encoded_string: ', encoded_string)

    return encoded_string.strip()


def decode(encoded_string):

    encoded_string = encoded_string.replace(' ', '')
    print('///////////////////////////')
    print('in decode function - encoded_string: ', encoded_string)

    result = []

    for i in range(len(encoded_string)):
        index_in_encoded = reversed_alphabet.find(encoded_string[i])
        result.append(index_in_encoded)
    print('result: ', result)

    decoded_string = ''

    for j in range(len(result)):
        decoded_string = decoded_string + alphabet[result[j]]

    print(decoded_string)

    if len(result) >= 5:
        return decoded_string
    else:
        return decoded_string

encode(string)