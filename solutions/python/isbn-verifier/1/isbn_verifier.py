# O Algoritmo do ISBN-10

def is_valid(isbn):
    # Limpar a string: Remover hifens e garantir que tudo esteja em um padrão (como tudo maiúsculo ou minúsculo).
    isbn = list(isbn.lower().replace('-',''))
    multipliers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    numbers = []
    # Validar o tamanho: Se após a limpeza não houver exatamente 10 caracteres, retorne False.
    if len(isbn) != 10:
        return False
    # Processar e Validar os Caracteres:
    # Percorrer os caracteres um por um.
    # Regra 1: Os primeiros 9 caracteres devem ser dígitos (0-9). Se aparecer uma letra aqui, retorne False.
    for i, char in enumerate(isbn):
        if i < 9 and not char.isdigit():
            return False
        elif i < 9 and char.isdigit():
            numbers.append(int(char))
    # Regra 2: O 10º caractere pode ser um dígito ou a letra 'X'. Se for 'X', ele vale 10. Se for qualquer outra letra, retorne False.
        elif i == 9 and (char.isdigit() or char == 'x'):
            if char =='x':
                numbers.append(10)
            else:
                numbers.append(int(char))
        else:
            return False
    # Calcular a Soma Ponderada:
    # Multiplicar o primeiro valor por 10, o segundo por 9... até o último por 1.
    # Somar todos esses resultados.
    # Verificar o Módulo:
    # Se a soma final dividida por 11 tiver resto zero, o ISBN é válido (True).
    # Caso contrário, é inválido (False).
    operation = list(zip(numbers, multipliers))
    return sum(a * b for a, b in operation) % 11 == 0

print(is_valid("3-598-21508-8"))