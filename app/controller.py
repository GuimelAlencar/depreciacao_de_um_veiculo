'''
# Controle
Arquivo responsável por gerenciar o relacionamento e o fluxo de informações entre a visualização, o processamento de dados, e a API da FIPE.
'''
import json
from models.depreciacao import calculo_depreciacao
from models.financiamento import calculo_financiamento

with open("preco_final_de_um_veiculo/db/db.json", "r", encoding="utf-8") as db_file:
    db = json.load(db_file)

def depreciacao(
        tipo_veiculo, 
        marca_veiculo, 
        modelo_veiculo, 
        ano_veiculo,
        consumo_veiculo,
    ):
    
    dados_depreciacao = calculo_depreciacao(
        tipo_veiculo, 
        marca_veiculo, 
        modelo_veiculo, 
        ano_veiculo,
        consumo_veiculo,
    )
    
    return dados_depreciacao 

def financiamento(
        tipo_veiculo, 
        marca_veiculo, 
        modelo_veiculo, 
        ano_veiculo,
        consumo_veiculo,
        taxa_de_juros_ao_ano, 
        numero_de_parcelas,
        tipo_de_parcela="mensal",
        tipo_de_tabela="PRICE",
        entrada=None, 
    ):
    
    valor_veiculo_financiado = get_valor_veiculo(
        tipo_veiculo, 
        marca_veiculo, 
        modelo_veiculo, 
        ano_veiculo,
        consumo_veiculo,
    )
    
    dados_financiamento = calculo_financiamento(
        valor_veiculo_financiado, 
        taxa_de_juros_ao_ano, 
        numero_de_parcelas,
        tipo_de_parcela,
        tipo_de_tabela,
        entrada,
    )
    
    return dados_financiamento

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
    set_de_consumos = set(veiculo["modelo"] for veiculo in veiculos if veiculo["tipo"] == tipo and veiculo["marca"] == marca and veiculo["modelo"] == modelo and veiculo["ano"] == ano)
    return list(set_de_consumos)

def get_valor_veiculo(tipo, marca, modelo, ano, consumo):
    for veiculo in veiculos:
        if (veiculo["tipo"] == tipo and
            veiculo["marca"] == marca and 
            veiculo["modelo"] == modelo and 
            veiculo["ano"] == ano and 
            veiculo["consumo"] == consumo):
            return veiculo["valor"]
    raise ValueError("Dados inválidos.")