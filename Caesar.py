import string


class Caesar:
    def __init__(self, alphabet_option_index):
        self.OPTIONS = [
            (0, "encrypt text", self.encrypt), 
            (1, "decrypt text", self.decrypt), 
            (2, "bruteforce decryption", self.bruteforce_decrypt), 
            (3, "change alphabet", self.change_alphabet), 
            (4, "exit program"),
        ]
        self.MSG_OPTIONS = [
            (0, "single line message", lambda: input("\nType your message (Enter to finish): ")),
            (1, "multiline message", Utils.read_multiline_message)
        ]
        self.ALPHABET_OPTIONS = [
            (0, "[a, b, c ... x, y, z]", string.ascii_lowercase),
            (1, 
             "[a, b, c ... !, @, # ... 1, 2, 3] (WARNING: In this option you'll " \
                "lose case sensitiveness)", 
             string.ascii_lowercase + string.punctuation + string.digits
            ),
        ]

        self.__alphabet = list(self.ALPHABET_OPTIONS[alphabet_option_index])[2]
        self.__is_alphabet_only_letters = True
        for char in self.__alphabet:
            if not char.isalpha():
                self.__is_alphabet_only_letters = False

    
    def __set_alphabet(self, new_alphabet):
        self.__alphabet = list(new_alphabet)


    def change_alphabet(self, new_alphabet_opt_index):
        self.__set_alphabet(self.ALPHABET_OPTIONS[new_alphabet_opt_index][2])


    def __caesar_algorithm(self, msg, shift, operation):
        final_txt = ""
        for char in msg:
            if char.lower() in self.__alphabet:
                if operation == "e":
                    new_index = (self.__alphabet.index(char.lower()) + shift)
                elif operation == "d":
                    new_index = (self.__alphabet.index(char.lower()) - shift)
                else:
                    raise ValueError("Invalid operation")

                new_index %= len(self.__alphabet)
                
                if self.__is_alphabet_only_letters:
                    final_txt += self.__alphabet[new_index].upper() if char.isupper() \
                                else self.__alphabet[new_index]
                else:
                    final_txt += self.__alphabet[new_index]
            else:
                final_txt += char
        
        return final_txt


    def encrypt(self, msg, shift):
        return self.__caesar_algorithm(msg, shift, "e")
    

    def decrypt(self, msg, shift):
        return self.__caesar_algorithm(msg, shift, "d")


    def bruteforce_decrypt(self, msg):
        for i in range(1, len(self.__alphabet)):
            yield f"{i:0>{len(str(len(self.__alphabet)))}} shift:\n{self.decrypt(msg, i)}\n\n"
