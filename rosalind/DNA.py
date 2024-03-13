def count_nt(DNAstring):
    '''Given a DNA string, returns the number of A, C, G, and T nucleotides in the string.
    DNAstring - str input eg., "GACACTAACTTAGGCAAGGACCTGAGTGCCAGACCCAATCTACATAAATAGTAG"
    rInt - int output
    '''
    A = DNAstring.count('A')
    C = DNAstring.count('C')
    G = DNAstring.count('G')
    T = DNAstring.count('T')
    return A, C, G, T
