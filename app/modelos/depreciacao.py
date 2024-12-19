from datetime import datetime
import random

def calculo_depreciacao(
        valor_veiculo,
        ano_veiculo
        ):
    
    ano_atual = datetime.now().year
    idade_veiculo = ano_atual - int(ano_veiculo)
    
    resultados = []
    valor_atual = valor_veiculo
    mes_atual = 1
    depreciacao_acumulada = 0
    
    while valor_atual > 0:
        resultados.append((mes_atual, round(valor_atual, 2)))
        
        taxa_anual = random.uniform(17.33, 21.33)
        taxa_mensal = taxa_anual / 12
            
        depreciacao_acumulada += taxa_mensal
        
        valor_atual = valor_veiculo * (1 - depreciacao_acumulada/100)
        
        if valor_atual < 1:
            valor_atual = 0
            resultados.append((mes_atual + 1, 0))
            break
            
        mes_atual += 1
        if mes_atual % 12 == 1:
            idade_veiculo += 1
    
    return tuple(resultados)