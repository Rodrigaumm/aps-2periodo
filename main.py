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

# Define a variável should_continue pra True. Essa é usada na condicional
# do loop
should_continue = True
while should_continue:
    # Pede uma opção ao usuário
    user_option = input("\nEscolha: ")

    # Caso o usuário tenha digitado 1,
    # troca o valor da variável should_continue para False
    # para que o loop pare de repetir e chama a função caesar_algorithm
    # passando para ela a mensagem do usuário, o shift que é uma
    # constante e o parâmetro que indica para a função que a mensagem
    # deve ser encriptada.
    if user_option == "1":
        should_continue = False

        msg = input("Mensagem: ")
        print(caesar_algorithm(msg, SHIFT, "e"))

    # Caso o usuário tenha digitado 2,
    # troca o valor da variável should_continue para False
    # para que o loop pare de repetir e chama a função caesar_algorithm
    # passando para ela a mensagem pedida ao usuário, o shift que é uma constante
    # e o parâmetro que indica para a função que a mensagem deve ser decriptada.
    elif user_option == "2":
        should_continue = False

        msg = input("Mensagem: ")
        print(caesar_algorithm(msg, SHIFT, "d"))

    # Caso o usuário não tenha digitado nem 1 nem 2,
    # mostre uma mensagem de erro e não altere o valor da variável de controle do loop
    # para que ela continue True e o loop continue repetindo
    else:
        print("Opção inválida, tente novamente")
        

