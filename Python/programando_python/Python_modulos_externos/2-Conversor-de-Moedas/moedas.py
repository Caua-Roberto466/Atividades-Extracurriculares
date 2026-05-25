taxas = {
    'BRL': 1.0,
    'USD': 0.2,
    'EUR': 0.17,
    'GBP': 0.15
}

def converter(moeda, convertida, quantidade):
    brl = quantidade / taxas[moeda]
    res = brl * taxas[convertida]
    return res
