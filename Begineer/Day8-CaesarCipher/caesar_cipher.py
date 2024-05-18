import os
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    cipher_text = ""
    if direction == "decode":
        shift *= -1
    for i in range(len(text)):
        if text[i] in alphabet:
            alpha_index = alphabet.index(text[i])
            if alpha_index + shift >= 26:  # > 25
                alpha_index -= 26
            cipher_text += alphabet[alpha_index + shift]
        else:
            cipher_text += text[i]

    print(f"The {direction}ed text is {cipher_text}")

end_it = False

while not end_it:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    caesar(text, shift, direction)

    result = input("Do you want to do it again? yes/no\n")
    if result == "no":
        end_it = True
    elif result == "yes":
        os.system('clear')
