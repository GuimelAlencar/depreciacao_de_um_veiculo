from controller import get_valor_veiculo

def calculo_depreciacao(
        tipo_veiculo, 
        marca_veiculo, 
        modelo_veiculo, 
        ano_veiculo,
        consumo_veiculo,
    ):
    
    valor_veiculo = get_valor_veiculo(tipo_veiculo, marca_veiculo, modelo_veiculo, ano_veiculo, consumo_veiculo)
    
    
'''
1 - Um carro perde cerca de 63% do seu valor original nos seus 5 primeiros anos de atividade.
    1.1 - cerca de 18.33% a.a
    1.2 - cerca de 1.52% a.m
2 - Os 3 primeiros anos são marcados por taxas que variam de 15% a 20% a.a
    2.1 - cerca de 17.5% a.a
    2.2 - cerca de 1.45% a.m
3 - Os 2 anos seguintes se estabilizam entre 6% e 10% a.a
    3.1 - cerca de 8% a.a
    3.2 - cerca de 0.66% a.m
'''