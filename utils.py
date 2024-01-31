import numpy as np

def similarity(a:str, b:str):
    assert len(a) == len(b)
    return len([True for i in range(len(a)) if a[i] == b[i]])

def idxsimilarity(base:str, data:list, cid:int):
    return np.argsort([similarity(base, data[i]) for i in range(len(data))])[cid]

def idxsimilarityskipsample(base:str, data:list, sample:str):
    return np.argsort([similarity(base, data[i])*(sample!=data[i]) for i in range(len(data))])[-1]

def idxsimilarityskipsamplelist(base:str, data:list, samples:list):
    return np.argsort([similarity(base, data[i])*(not (data[i] in samples)) for i in range(len(data))])[-1]

def binstr2keystr(string):
    return ''.join([(chr(97+i) if string[i] == '0' else chr(65+i))  for i in range(len(string))])

def notkeystr(string):
    return ''.join([(c.lower() if c.isupper() else c.upper()) for c in string])

def simplify(a:str, b:str):
    fa = ""
    fb = ""

    for i in range(len(a)):
        if a[i] == b[i]:
            fa = fa + a[i]
        else:
            fb = fb + a[i]
        # if len(fb) == 2 y es not mutuamente entonces seaplica xor

    return [fa] if len(fb) == 1 else [a, b]
