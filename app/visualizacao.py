'''
# Visualização
Arquivo responsável por gerar a interação entre o usuário e o programa por meio de alguma 
biblioteca como StreamLit, Python kivy ou Plotly Dash
'''
# depreciação - Cálculo da depreciação de um veículo de valor x
# financiamento - Cálculo de um financiamento de um veículo de valor x

#3 get_tipos,marcas,modelos,consumos e anos são ferramentas que retornam todos os tipos, marcas, modelos, anos e consumos dos veículos do db veículos

# Eles serão os únicos meios de comunicação com o back do qual vocês terão que se preocupar.
from controle import depreciacao, financiamento, get_dados_db

dados_do_financiamento = financiamento(
    #Tipo
    "carro", 
    # Marca
    "toyota",
    # Modelo
    "corolla",
    # Ano de fabricação
    "2020",
    # Tipo de consumo
    "gasolina",
    # 5%
    5,
    # 12 parcelas
    12,
    # Modalidade de parcelamento: mensal
    "mensal",
    # Tabela aplicada no cálculo de financiamento
    "PRICE",
    # Entrada
    12000, 
)
# Printing data
for parcela, valor in dados_do_financiamento:
    print(f"{parcela}º parcela: R${valor}")