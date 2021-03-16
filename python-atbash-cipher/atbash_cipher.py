alphabet = 'abcdefghijklmnopqrstuvwxyz'
reversed_alphabet = alphabet[::-1]


def encode(input: str):
    punct_and_space = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    for elem in input:
        if elem in punct_and_space:
            input = input.lower().replace(elem, "")
        else:
            input = input.lower()

    result = []

    for i in range(len(input)):

        if input[i].isdigit():
            found_index = input[i]
        else:
            found_index = alphabet.find(input[i])

        result.append(found_index)

    encoded_string = ''

    for j in range(len(result)):
        if j % 5 == 0 and j != 0:
            encoded_string = encoded_string + " " + reversed_alphabet[result[j]]

        elif type(result[j]) == str:
            encoded_string = encoded_string + result[j]
        else:
            encoded_string = encoded_string + reversed_alphabet[result[j]]

    return encoded_string.strip()


def decode(encoded_string):
    encoded_string = encoded_string.replace(' ', '')

    result = []

    for i in range(len(encoded_string)):
        index_in_encoded = reversed_alphabet.find(encoded_string[i])
        result.append(index_in_encoded)

    decoded_string = ''

    for j in range(len(result)):
        decoded_string = decoded_string + alphabet[result[j]]

    if len(result) >= 5:
        return decoded_string
    else:
        return decoded_string
