def caesar_cipher(text, shift, decrypt=False):
    lowercase_alphabet = "abcdefghijklmnopqrstuvwxyz"
    if decrypt:
        shift = 26 - shift
    shifted_lowercase_alphabet = lowercase_alphabet[shift:] + lowercase_alphabet[:shift]
    uppercase_alphabet = shifted_lowercase_alphabet.upper()
    translation_table = str.maketrans(lowercase_alphabet + uppercase_alphabet,
                                      shifted_lowercase_alphabet + uppercase_alphabet)
    encrypted_text = "[Output]: " + text.translate(translation_table)

    return encrypted_text


actions = {
    "1": (False, "Encrypt this: "),
    "2": (True, "Decrypt this: "),
    "3": (None, "Exiting program.")
}

while True:
    opt = input("Would you like to: [1] Encrypt or [2] Decrypt with Caesar's Cipher [3] Exit program.")
    if opt in actions:
        action, prompt = actions[opt]
        if action is not None:
            shifted = input("How many letters should be shifted?")
            if shifted.isdigit():
                shifted = int(shifted)
                promptinput = input(prompt)
                print(caesar_cipher(promptinput, shifted, decrypt=action))
        else:
            print(prompt)
            break
