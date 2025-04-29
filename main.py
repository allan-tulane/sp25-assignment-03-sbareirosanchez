import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))


def fast_MED(S, T, MED={}):
    if (S, T) in MED:
        return MED[(S, T)]
    if not S:
        return len(T)
    elif not T:
        return len(S)
    elif S[0] == T[0]:
        MED[(S, T)] = fast_MED(S[1:], T[1:], MED)
    else:
        MED[(S, T)] = 1 + min(fast_MED(S, T[1:], MED), fast_MED(S[1:], T, MED), fast_MED(S[1:], T[1:], MED))
    return MED[(S, T)]

def fast_align_MED(S, T, memo={}):
    if (S, T) in memo:
        return memo[(S, T)]
    
    if not S:
        memo[(S, T)] = ('-' * len(T), T)
    elif not T:
        memo[(S, T)] = (S, '-' * len(S))
    elif S[0] == T[0]:
        aligned_S, aligned_T = fast_align_MED(S[1:], T[1:], memo)
        memo[(S, T)] = (S[0] + aligned_S, T[0] + aligned_T)
    else:
        ins_S, ins_T = fast_align_MED(S, T[1:], memo)
        insert = (1 + fast_MED(S, T[1:], memo), '-' + ins_S, T[0] + ins_T)
        
        del_S, del_T = fast_align_MED(S[1:], T, memo)
        delete = (1 + fast_MED(S[1:], T, memo), S[0] + del_S, '-' + del_T)
        
        sub_S, sub_T = fast_align_MED(S[1:], T[1:], memo)
        substitute = (1 + fast_MED(S[1:], T[1:], memo), S[0] + sub_S, T[0] + sub_T)

        best = min([insert, delete, substitute], key=lambda x: x[0])
        memo[(S, T)] = (best[1], best[2])
    return memo[(S, T)]

