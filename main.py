from string import ascii_lowercase

ALPHABET = list(ascii_lowercase)
SHIFT = 389012391290831902309125890123089190
OPTIONS = (
    (0, "encrypt", lambda msg, shift: caesar_algorithm(msg, shift, 1)),
    (1, "decrypt", lambda msg, shift: caesar_algorithm(msg, shift, 0)),
)


def choose_option(options_list):
    for option_element in options_list:
        print(f"{option_element[0]}: {option_element[1]}\n")
    
    while True:
        try:
            user_option = int(input("Choose an option: "))

            option = None
            for menu_option in options_list:
                if menu_option[0] == user_option:
                    option = tuple(menu_option)

            if option is None:
                raise ValueError()
            else:
                return option
        except ValueError:
            print("Invalid option, try again")


def caesar_algorithm(msg, shift, operation_code):
    final_msg = ""
    for char in msg:
        try:
            # ALPHABET.index(char.lower()) raises a ValueError if there is no such item in the list.
            new_index = ALPHABET.index(char.lower())
            if operation_code:
                new_index += shift
            else:
                new_index -= shift

            new_index %= len(ALPHABET)
            final_msg += ALPHABET[new_index].upper() if char.isupper() else ALPHABET[new_index]
        except ValueError: 
            final_msg += char

    return final_msg


def main():
    option = choose_option(OPTIONS)
    if len(option) > 2:
        user_msg = input("Type your message: ")
        while not user_msg:
            print("Empty message. Try again:\n")
            user_msg = input("Type your message: ")

        
        print(option[2](user_msg, SHIFT))
       

if __name__ == "__main__":
    main()
