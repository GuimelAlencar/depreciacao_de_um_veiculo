'''
# Visualização
Arquivo responsável por gerar a interação entre o usuário e o programa por meio de alguma 
biblioteca como StreamLit, Python kivy ou Plotly Dash
'''
# depreciação - Cálculo da depreciação de um veículo de valor x
# financiamento - Cálculo de um financiamento de um veículo de valor x

#3 get_tipos,marcas,modelos,consumos e anos são ferramentas que retornam todos os tipos, marcas, modelos, anos e consumos dos veículos do db veículos

# Eles serão os únicos meios de comunicação com o back do qual vocês terão que se preocupar.
from controller import depreciacao, financiamento, get_tipos, get_marcas, get_modelos, get_anos, get_consumos