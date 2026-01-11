codons = {
        'AUG': 'Methionine',
        'UUU': 'Phenylalanine',
        'UUC': 'Phenylalanine',
        'UUA': 'Leucine',
        'UUG': 'Leucine',
        'UCU': 'Serine',
        'UCC': 'Serine', 
        'UCA': 'Serine', 
        'UCG': 'Serine',
        'UAU': 'Tyrosine',
        'UAC': 'Tyrosine',
        'UGU': 'Cysteine', 
        'UGC': 'Cysteine',
        'UGG': 'Tryptophan',
        'UAA': 'Stop',
        'UAG': 'Stop',
        'UGA': 'Stop'
    }

def proteins(strand):
    # slice
    strands = [] # lista vazia

    for codon in range(0, len(strand), 3):              # loop que itera usando um range de len(strand), 
                                                        # ou seja, do tamanho do argumento strand da função, 
                                                        # o passo está de 3 em 3, ou seja, codon é uma variável 
                                                        # de número 0, 3, 6 , 9...
        
        strands. append(strand[codon : codon + 3])      # faz o append do codon usando o slice do strand, onde
                                                        # codon é 0 para o início e codon + 3 é o fim
    
    proteins = []                                       # lista vazia para armazenar as proteínas

    for codon in strands:                               # loop que procura o codon na lista strands
                                                        #
        protein = codons[codon]                         # protein é uma variável que armazena os values do 
                                                        # dicionário codons
                                                    
        if protein == 'Stop':                           # verifica se 'Stop' é um value da protein
            break                                       # para o loop se encontrar um 'Stop'
        elif codon in codons:                           # verifica se o codon é uma protein em codons
            proteins.append(protein)                    # faz o append da protein na lista proteins

    return proteins                                     # retorna a lista proteins
    
print(proteins("UAA"))