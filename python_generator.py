i_list = [
    
    "4123456789123456",
    "5123-4567-8912-3456",
    "61234-567-8912-3456",
    "4123356789123456",
    "5133-3367-8912-3456",
    "5123 - 3567 - 8912 - 3456"
]

for credit_number in i_list:
    # Remover espacios y guiones para la validacion
    clean_number = credit_number.replace(' ', '').replace('-', '')

    # Contador de digitos
    contador_numeros = 0
    contador_repeticiones = 1  
    caracter_anterior = clean_number[0] 

    for caracter in clean_number:
        if caracter.isdigit():
            contador_numeros += 1        

    if contador_numeros != 16:
        print('Invalid')
    elif clean_number[0] not in ('4', '5', '6'):
        print("Invalid")
    elif not all(caracter.isdigit() for caracter in clean_number):
        print("Invalid")
    else:
        # Validar el formato con guiones o espacios si existen
        if '-' in credit_number:
            if not (credit_number[4] == '-' and credit_number[9] == '-' and credit_number[14] == '-'):
                print("Invalid")
                continue
        elif ' ' in credit_number:
            if not (credit_number[4] == ' ' and credit_number[9] == ' ' and credit_number[14] == ' '):
                print("Invalid")
                continue

        # Validar repeticiones consecutivas
        for caracter in clean_number[1:]:
            if caracter == caracter_anterior:
                contador_repeticiones += 1
                if contador_repeticiones >= 4:
                    print("Invalid")
                    break  
            else:
                contador_repeticiones = 1  
            caracter_anterior = caracter
        else:
            print("Valid")

