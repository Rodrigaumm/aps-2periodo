alphabet = list('abcdefghijklmnopqrstuvwxyz')
SHIFT = 21


def caesar_algorithm(msg, shift, operation_code):
    # Cria uma string vazia que será preenchida
    # com cada letra da mensagem original porém encriptada/desencriptada
    final_msg = ""
    for char in msg:
        # Verifica se a letra atual convertida pra minúscula
        # está contida no alfabeto
        if char.lower() in alphabet:
            
            # Atribui à variável new_index a posição
            # da letra atual no alfabeto. Ex: a - 0, b - 1, etc...
            new_index = alphabet.index(char.lower())

            # A função recebe operation_code == "e" para encriptar
            # e operation_code == "d" para decriptar
            if operation_code == "e":
                new_index += shift
            elif operation_code == "d":
                new_index -= shift

            new_index = new_index % len(alphabet)

            # Caso a letra original da mensagem seja maíscula
            # a letra encriptada/decriptada também será maíscula
            # no texto de final_msg
            if char.isupper():
                final_msg += alphabet[new_index].upper()
            else:
                final_msg += alphabet[new_index]
        
        # Caso a letra atual não esteja no alfabeto
        # não efetua nenhuma encriptação/decriptação.
        # Apenas repete o caractere no texto final
        else: 
            final_msg += char

    # Após o loop percorrer todas as letras da mensagem original,
    # encriptar/decriptar cada uma, a função retorna o texto final, que foi
    # gerado letra a letra a partir da mensagem do usuário (mensagem original)
    return final_msg



# Printa as opções para o usuário
print("1 - Encriptar")
print("2 - Decriptar")

# Define a variável valid_option pra false. Essa é usada na condicional
# do loop 
should_continue = True
while should_continue:
    user_option = input("\nEscolha: ")

    if user_option == "1":
        should_continue = False

        msg = input("Mensagem: ")
        print(caesar_algorithm(msg, SHIFT, "e"))
    elif user_option == "2":
        should_continue = False

        msg = input("Mensagem: ")
        print(caesar_algorithm(msg, SHIFT, "d"))
    else:
        print("Opção inválida, tente novamente")
        

