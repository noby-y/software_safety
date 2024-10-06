import textwrap
from cipher import apply_cipher
from os import path

def get_file():
    file_name = input("Please enter the file name you want to encode/decode below:\n")
    while not path.exists(file_name):
        if file_name == 'stop!':
            return 0, 0
        file_name = input("ERROR! File doesn't exist. Try again or write 'stop!' to cancel:\n")
    file = open(file_name)
    file_text = file.read()
    file.close()
    return file_text, file_name

def save_file(file_text, file_name):
    file = open(file_name, "w")
    file.write(file_text)
    file.close()

def shift_text(text):
    shift = input("How many times do you want to shift the text:\n")
    while True: 
        # Check if shift can be converted to int
        try:
            shift = int(shift)
            break
        except ValueError:
            if shift == 'stop!':
                return 0
            shift = input("ERROR! Invalid shift value. Must be a number. Try again or write 'stop!' to cancel:\n")

    return apply_cipher(text, shift)

def decode_text(text):
    print(textwrap.dedent("""
        Choose how you want to decode the file:
            1 - shift by some value
            2 - shift for all values in the range 0-33 (max shift for ukr alphabet)"""))
    decode_method = input()

    while not decode_method in {'1', '2'}:
        if decode_method == "stop!":
            return 0
        decode_method = input("ERROR! Invalid decode method. Must be either 1 or 2. Try again or write 'stop!' to cancel:\n")

    if decode_method == '1':
        return shift_text(text)
    elif decode_method == '2':

        # Try out every shift combination
        result = ""
        for shift in range(1, 34):
            result += f"s-{shift}: {apply_cipher(text, shift)}"
        return result

def choose_action():
    while True:
        print(textwrap.dedent("""
            Choose an action and press Enter:
                1 - Choose file
                2 - Show Credits
                3 - Exit the program"""))
        action = input()
        match action:
            case '1':
                input_text, file_name = get_file()
                if input_text == 0 and file_name == 0:
                    continue
                return input_text, file_name
            case '2':
                print("credits: Noby")
                print()
                continue
            case '3':
                exit(0)
            case _:
                print("Invalid action, try again")
                continue

def process_text(input_text):
    while True:
        print(textwrap.dedent("""
            Choose what to do with the file:
                1 - Read file
                2 - Encode file
                3 - Decode file
                4 - Cancel"""))

        action = input()
        match action:
            case '1':
                print(input_text)
                continue
            case '2':
                output_text = shift_text(input_text)
                if output_text == 0:
                    continue
                return output_text 
            case '3':
                output_text = decode_text(input_text)
                if output_text == 0:
                    continue
                return output_text
            case '4':
                return 0
            case _:
                print("Invalid action, try again")
                continue

def save_result(output_text, input_text, file_name):
    while True:
        print(textwrap.dedent("""
            Please choose what to do with the text output:
                1 - Save in a new file
                2 - Overwrite used file
                3 - Print out
                4 - Go back to main menu"""))

        action = input()
        match action:
            case '1':
                save_file(output_text, f"output_{file_name}")
                continue
            case '2':
                save_file(output_text, file_name)
                continue
            case '3':
                print(f"Input text:\n{input_text}")
                print(f"Output text:\n{output_text}")
                continue
            case '4':
                return
            case _:
                print("Invalid action, try again")
                continue

def main():
    print("============================================")
    print("WELCOME TO THE CAESAR CIPHER ENCODER/DECODER")
    print("============================================")
    while True:
        input_text, file_name = choose_action()
        output_text = process_text(input_text)
        if output_text != 0:
            save_result(output_text, input_text, file_name)

main()
