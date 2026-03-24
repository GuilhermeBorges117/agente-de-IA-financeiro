import csv
import json

def carregar_transacoes(caminho):
    with open(caminho, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def carregar_json(caminho):
    with open(caminho, encoding='utf-8') as f:
        return json.load(f)
