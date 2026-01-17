def to_rna(dna_strand):
    dna_upper = dna_strand.upper()
    if dna_upper:
        rna_strand = ''
        for nucleotide in dna_upper:
            if nucleotide == 'G':
                rna_strand += 'C'
            elif nucleotide == 'C':
                rna_strand += 'G'
            elif nucleotide == 'T':
                rna_strand += 'A'
            elif nucleotide == 'A':
                rna_strand += 'U'
            else:
                rna_strand = 'Invalid DNA strand!'
                break
    return rna_strand
