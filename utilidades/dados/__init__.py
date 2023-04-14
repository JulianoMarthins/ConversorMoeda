def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').replace(' ', '')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[0;31mERRO:\033[m \033[0:35m\"{entrada}\" é um preço inválido!\033[m\n')
        else:
            valido = True
            return float(entrada)
