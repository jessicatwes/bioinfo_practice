def DNAtoRNA(DNAstring):
    '''Given a DNA string, returns the RNA string transcribed from the DNA string by replacing T with U
    DNAstring - str input of DNA
    rStr - str output of RNA where T have been replaced with U
    '''
    RNAstring = DNAstring.replace('T', 'U')
    return RNAstring
