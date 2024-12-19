from modelos.depreciacao import calculo_depreciacao
from modelos.financiamento import calculo_financiamento

def depreciacao(
        tipo_veiculo, 
        marca_veiculo, 
        modelo_veiculo, 
        ano_veiculo,
        consumo_veiculo,
    ):
    
    valor_veiculo = get_dados_db(
        "valor",
        tipo_veiculo, 
        marca_veiculo, 
        modelo_veiculo, 
        ano_veiculo,
        consumo_veiculo,
    )
    
    dados_depreciacao = calculo_depreciacao(valor_veiculo, ano_veiculo)
    
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
    
    valor_veiculo_financiado = get_dados_db(
        "valor",
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
    
def get_dados_db(dado, tipo=None, marca=None, modelo=None, ano=None, consumo=None):
    import rotas
    match dado:
        case "tipos":
            return rotas.get_tipos()        
        case "marcas":
            return rotas.get_marcas(tipo)
        case "modelos":            
            return rotas.get_modelos(tipo, marca)        
        case "anos":
            return rotas.get_anos(tipo, marca, modelo)
        case "consumos":
            return rotas.get_consumos(tipo, marca, modelo, ano)
        case "valor":
            return rotas.get_valor_veiculo(tipo, marca, modelo, ano, consumo)
    
    return dados_financiamento