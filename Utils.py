class Utils:
    @staticmethod
    def list_options(options_list):
        print("\n\n")
        for option_element in options_list:
            print(f"{option_element[0]}: {option_element[1]}\n\n")


    @staticmethod
    def choose_option(options_list):
        Utils.list_options(options_list)
        
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


    @staticmethod   
    def read_multiline_message():
        print(
            "\nType your message (to finish the message, break a line and CTRL+Z on Windows "
            "and CTRL+D on Unix): "
        )
        msg = []
        while True:
            try:
                line = input()
            except EOFError:
                break
            msg.append(line)

        return "\n".join(msg)
