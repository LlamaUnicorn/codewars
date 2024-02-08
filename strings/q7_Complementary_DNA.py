# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).
# Example: (input --> output)

# "ATTGC" --> "TAACG"
# "GTAT" --> "CATA"

cases = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C',
}


def dna_strand(dna):
    result = ''.join(cases[letter] for letter in dna)
    return result


print(dna_strand('ATTGC'))
