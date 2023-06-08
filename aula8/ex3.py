def format_string(string):

    if len(string) != 9:
        return "A string deve conter nove caracteres numéricos."

    parte_inteira = string[:7]
    parte_decimal = string[7:]

    parte_inteira_formatada = '.'.join(parte_inteira[i:i+3] for i in range(1, len(parte_inteira), 3))

    parte_decimal_formatada = ',' + parte_decimal


    return parte_inteira[0] + '.' + parte_inteira_formatada + parte_decimal_formatada


entrada = input("Digite os nove caracteres numéricos: ")


resultado = format_string(entrada)
print("Formatado:", resultado)
