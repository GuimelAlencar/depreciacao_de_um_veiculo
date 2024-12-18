import json

with open("db\db.json", "r", encoding="utf-8") as db_file:
    db = json.load(db_file)

veiculos = db["veiculos"]


def get_tipos():
    set_de_tipos = set(veiculo["tipo"] for veiculo in veiculos)
    return list(set_de_tipos)

def get_marcas(tipo):
    set_de_marcas = set(veiculo["marca"] for veiculo in veiculos if veiculo["tipo"] == tipo)
    return list(set_de_marcas)

def get_modelos(tipo, marca):
    set_de_modelos = set(veiculo["modelo"] for veiculo in veiculos if veiculo["tipo"] == tipo and veiculo["marca"] == marca)
    return list(set_de_modelos)

def get_anos(tipo, marca, modelo):
    set_de_anos = set(veiculo["modelo"] for veiculo in veiculos if veiculo["tipo"] == tipo and veiculo["marca"] == marca and veiculo["modelo"] == modelo)
    return list(set_de_anos)

def get_consumos(tipo, marca, modelo, ano):
    set_de_consumos = set(veiculo["modelo"] for veiculo in veiculos if veiculo["tipo"] == tipo and veiculo["marca"] == marca and veiculo["modelo"] == modelo and veiculo["ano_de_fabricacao"] == ano)
    return list(set_de_consumos)

def get_valor_veiculo(tipo, marca, modelo, ano, consumo):
    for veiculo in veiculos:
        if (veiculo["tipo"] == tipo and
            veiculo["marca"] == marca and 
            veiculo["modelo"] == modelo and 
            veiculo["ano_de_fabricacao"] == ano and 
            veiculo["tipo_combustivel"] == consumo):
            return veiculo["valor"]
    raise ValueError("Dados inválidos.")