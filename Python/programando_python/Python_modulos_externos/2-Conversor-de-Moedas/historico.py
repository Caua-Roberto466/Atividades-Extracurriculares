import json

ARQUIVO = "historico.json"

def carregar():
    try:
        with open(ARQUIVO, 'r', encoding='utf-8') as arq:
            return json.load(arq)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    
def salvar(lista):
    with open(ARQUIVO, "w", encoding='utf-8') as arq:
        json.dump(lista, arq, indent=4, ensure_ascii=False)