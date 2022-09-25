import numpy as np;
from math import cos, pi;

_j_facts = np.empty(2, dtype=object);
_j_facts[0] = 1;
_j_facts[1] = 1;
_j_maxfact = 1;

""" Fatorial otimizado"""
def _j_fact(val) -> int:
    global _j_facts;
    global _j_maxfact;
    if (val <= _j_maxfact):
        return _j_facts[val];
    
    else:
        for i in range(_j_maxfact+1, val+1):
            mult = i*_j_facts[i-1];
            _j_facts = np.append(_j_facts, mult);
        _j_maxfact = val;
        return _j_facts[val];


""" Combinação simples (N P)"""
def comb(N, P) -> int:
    return _j_fact(N) // (_j_fact(P)*_j_fact(N - P)); # comb sempre retorna um inteiro


""" Números de euler"""
def euler(val) -> int:
    # tratar erro
    if val == 0: return 1;
    elif (val%2) != 0: return 0;

    N = val;
    mult = (N + 1);
    soma = 0;
    for l in range(1, N+1):
        itema = ((-1)**l);
        itemb = (1/((2**l)*(l+1)));
        itemc = comb(N, l);
        itemd = 0;
        for q in range(0, l+1):            
            itemd += comb(l, q)* ((2*q -  l))**N;
        
        soma += itema*itemb*itemc*itemd;    

    return round(mult*soma);


#pares = 0
def secant(val):
    return 1/cos(val);

__secant_table = {
    0: 1,
    
    np.pi/6: 2/np.sqrt(3),
    np.pi/4: 2/np.sqrt(2),
    np.pi/3: 2,
    
    np.pi/2: None,
    
    2*np.pi/3: -2,
    3*np.pi/4: -2/np.sqrt(2),
    5*np.pi/6: -2/np.sqrt(3),
    
    np.pi: -1,
    
    7*np.pi/6: -2/np.sqrt(3),
    5*np.pi/4: -2/np.sqrt(2),
    4*np.pi/3: -2,

    3*np.pi/2: None,

    5*np.pi/3: 2,
    7*np.pi/4: 2/np.sqrt(2),
    11*np.pi/6: 2/np.sqrt(3),
}

def taylor_secante(val, inf) -> float:
    if val in __secant_table:
        return __secant_table[val];
    
    retorno = 0;
    for i in range(0, inf+1):
        retorno += (max(euler(i), -euler(i))/_j_fact(2*i)) * val**(2*i);
    return retorno; 

print(taylor_secante(np.pi/6, 100));
print(secant(np.pi/6));
print(2/np.sqrt(3));

# é pra dar o mesmo
print((pi/6)%(2*pi));
print((13*pi/6)%(2*pi));