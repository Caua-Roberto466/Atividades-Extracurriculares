import json

ARQUIVO = "1-frutas.json"

dados = {
    'frutas': [
        {
            "nome": "Banana",
            "preço": 2.45
        },
        {
            "nome": "Maçã",
            "preço": 1.23
        }
    ]
}

with open(ARQUIVO, "w", encoding="utf-8") as arq:
    json.dump(dados, arq, indent=4, ensure_ascii=False)

frutas = {}

with open(ARQUIVO, "r", encoding='utf-8') as arq:
    frutas = json.load(arq)

print(frutas)