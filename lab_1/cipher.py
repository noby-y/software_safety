
def apply_cipher (text, shift):
    text_cipher = ''

    alphabet_latin = [
        [65, 90],   # lowercase
        [97, 122],  # uppercase
    ]
    alphabet_ukr_upp = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
    alphabet_ukr_low = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'

    for char in text:
        char_code = ord(char)
        not_english = False 

        if char_code in { 1168, 1028, 1030, 1031 } or ( 1040 <= char_code <= 1103 and char_code not in { 1066, 1067, 1069 }):
            not_english = True 

        if not_english:
            if char.isupper():
                idx = alphabet_ukr_upp.index(char)
                idx = (idx + shift) % 33
                char = alphabet_ukr_upp[idx]
            else:
                idx = alphabet_ukr_low.index(char)
                idx = (idx + shift) % 33
                char = alphabet_ukr_low[idx]

        else:
            for alph in alphabet_latin:
                if alph[0] <= char_code <= alph[1]:

                    char_code -= alph[0]
                    char_code = (char_code + shift) % (alph[1] - alph[0] + 1)
                    char_code += alph[0]

                    break
            char = chr(char_code)    
        text_cipher += char

    return text_cipher
