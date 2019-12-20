__author__ = 'darakna'
def one_dna_to_rna(c):
    if c == 'A':
        return 'U'
    elif c == 'C':
        return 'G'
    elif c == 'G':
        return 'C'
    elif c == 'T':
        return 'A'
    else:
        return ''

def transcribe(S):
    if S == '':
        return ''
    else:
        return one_dna_to_rna(S[0])+transcribe(S[1:])
#
# Tests
#
print("transcribe('ACGT TGCA'):  'UGCAACGU' ==", transcribe('ACGT TGCA'))
print("transcribe('GATTACA'):     'CUAAUGU' ==", transcribe('GATTACA'))
print("transcribe('cs5') :               '' ==", transcribe('cs5'))
print("transcribe('') :                  '' ==", transcribe(''))
