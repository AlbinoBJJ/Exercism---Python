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
    # lista vazia
    strands = [] 

    # loop que itera usando um range de len(strand), 
    # ou seja, do tamanho do argumento strand da função, 
    # o passo está de 3 em 3, ou seja, codon é uma variável de número 0, 3, 6, 9...
    for codon in range(0, len(strand), 3):
        # faz o append do codon usando o slice do strand, onde
        # codon é 0 para o início e codon + 3 é o fim
        strands.append(strand[codon : codon + 3]) 
    
    # lista vazia para armazenar as proteínas
    proteins = [] 

    # loop que procura o codon na lista strands
    for codon in strands:
        # acessa o valor específico associado àquela chave única. 
        # é como olhar uma palavra específica em um dicionário físico. 
        # no caso, é o dicionário codons
        protein = codons[codon] 
                                                            
        # verifica se 'Stop' é um value da protein
        if protein == 'Stop':
            # para o loop se encontrar um 'Stop'
            break 

        # como a sequência de 3 letras contida em strands existe 
        # como uma chave no dicionário fazemos o append da protein na lista proteins
        proteins.append(protein) 
        
    # retorna a lista proteins
    return proteins