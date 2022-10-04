import inspect
from . import Caesar, Utils


def main():
    should_terminate = False
    caesar = Caesar(0)
    while not should_terminate:
            action_option = Utils.choose_option(caesar.OPTIONS)

            if action_option and len(action_option) > 2:
                action_parameters_list = [parameter for parameter in inspect.signature(action_option[2]).parameters]
                if "msg" in action_parameters_list:
                    msg_option = Utils.choose_option(caesar.MSG_OPTIONS)

                    if msg_option:
                        user_msg = msg_option[2]()

                        if "shift" in action_parameters_list:
                            shift = int(input("What's the shift? "))
                            result = action_option[2](user_msg, shift)
                        else:
                            result = action_option[2](user_msg)

                        print("\n-------Result-------")
                        if inspect.isgenerator(result):
                            for i in result:
                                print(i)
                        else:
                            print(result)
                        print("--------------------")
                else:
                    alphabet_option = Utils.choose_option(caesar.ALPHABET_OPTIONS)
                    caesar.change_alphabet(alphabet_option[0])
                    print("Changed alphabet successfully")
                    
            elif action_option:
                should_terminate = True
        

if __name__ == "__main__":
    main()
