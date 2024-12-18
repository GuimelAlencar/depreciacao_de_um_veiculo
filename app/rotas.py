import json

with open("db\db.json", "r", encoding="utf-8") as db_file:
    db = json.load(db_file)

veiculos = db["veiculos"]


def get_tipos():
    tipos_vistos = set()
    lista_de_tipos = []
    for veiculo in veiculos:
        if veiculo["tipo"] not in tipos_vistos:
            tipos_vistos.add(veiculo["tipo"])
            lista_de_tipos.append(veiculo["tipo"])
    return tuple(lista_de_tipos)

def get_marcas(tipo):
    marcas_vistas = set()
    lista_de_marcas = []
    for veiculo in veiculos:
        if (veiculo["tipo"] == tipo and 
            veiculo["marca"] not in marcas_vistas):
            marcas_vistas.add(veiculo["marca"])
            lista_de_marcas.append(veiculo["marca"])
    return tuple(lista_de_marcas)


def get_modelos(tipo, marca):
    modelos_vistos = set()
    lista_de_modelos = []
    for veiculo in veiculos:
        if (veiculo["tipo"] == tipo and 
            veiculo["marca"] == marca and 
            veiculo["modelo"] not in modelos_vistos):
            modelos_vistos.add(veiculo["modelo"])
            lista_de_modelos.append(veiculo["modelo"])
    return tuple(lista_de_modelos)

def get_anos(tipo, marca, modelo):
    anos_vistos = set()
    lista_de_anos = []
    for veiculo in veiculos:
        if (veiculo["tipo"] == tipo and 
            veiculo["marca"] == marca and 
            veiculo["modelo"] == modelo and 
            veiculo["ano_de_fabricacao"] not in anos_vistos):
            anos_vistos.add(veiculo["ano_de_fabricacao"])
            lista_de_anos.append(veiculo["ano_de_fabricacao"])
    return tuple(lista_de_anos)

def get_consumos(tipo, marca, modelo, ano):
    consumos_vistos = set()
    lista_de_consumos = []
    for veiculo in veiculos:
        if (veiculo["tipo"] == tipo and 
            veiculo["marca"] == marca and 
            veiculo["modelo"] == modelo and 
            veiculo["ano_de_fabricacao"] == ano and 
            veiculo["consumo"] not in consumos_vistos):
            consumos_vistos.add(veiculo["consumo"])
            lista_de_consumos.append(veiculo["consumo"])
    return tuple(lista_de_consumos)

def get_valor_veiculo(tipo, marca, modelo, ano, consumo):
    for veiculo in veiculos:
        if (veiculo["tipo"] == tipo and
            veiculo["marca"] == marca and 
            veiculo["modelo"] == modelo and 
            veiculo["ano_de_fabricacao"] == ano and 
            veiculo["tipo_combustivel"] == consumo):
            return veiculo["valor"]
    raise ValueError("Dados inválidos.")