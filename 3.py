d = {"a": 1, "b": 2, "c": 3}

def inv_dict(d):
    inverted = {}
    for alphabet,num in d.items():
        inverted[num] = alphabet
    return inverted

print(inv_dict(d))