import json as js

ARQUIVO = "historico.json"

def salvar(lista):
    with open(ARQUIVO, 'w', encoding='utf-8') as arq:
        js.dump(lista, arq, indent=4, ensure_ascii=False)

def carregar():
    try:
        with open(ARQUIVO, 'r', encoding='utf-8') as arq:
            return js.load(arq)
            
    except (js.JSONDecodeError, FileNotFoundError):
        return []
    