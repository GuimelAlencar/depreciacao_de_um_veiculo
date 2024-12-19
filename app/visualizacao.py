'''
# Visualização
Arquivo responsável por gerar a interação entre o usuário e o programa por meio de alguma 
biblioteca como StreamLit, Python kivy ou Plotly Dash
'''
# depreciação - Cálculo da depreciação de um veículo de valor x
# financiamento - Cálculo de um financiamento de um veículo de valor x

#3 get_tipos,marcas,modelos,consumos e anos são ferramentas que retornam todos os tipos, marcas, modelos, anos e consumos dos veículos do db veículos

# Eles serão os únicos meios de comunicação com o back do qual vocês terão que se preocupar.

import streamlit as st
import plotly.graph_objects as go
from controle import depreciacao, financiamento, get_dados_db

# Título da aplicação
st.title("Simulação de Depreciação e Financiamento de Veículos")

# Seleção do tipo de veículo
tipos = get_dados_db("tipos")
tipo_selecionado = st.selectbox("Selecione o tipo de veículo", tipos)

# Seleção da marca do veículo
if tipo_selecionado:
    marcas = get_dados_db("marcas", tipo_selecionado)
    marca_selecionada = st.selectbox("Selecione a marca do veículo", marcas)

# Seleção do modelo do veículo
if marca_selecionada:
    modelos = get_dados_db("modelos", tipo_selecionado, marca_selecionada)
    modelo_selecionado = st.selectbox("Selecione o modelo do veículo", modelos)

# Seleção do ano de fabricação do veículo
if modelo_selecionado:
    anos = get_dados_db("anos", tipo_selecionado, marca_selecionada, modelo_selecionado)
    ano_selecionado = st.selectbox("Selecione o ano de fabricação do veículo", anos)

# Seleção do tipo de combustível do veículo
if ano_selecionado:
    consumos = get_dados_db("consumos", tipo_selecionado, marca_selecionada, modelo_selecionado, ano_selecionado)
    consumo_selecionado = st.selectbox("Selecione o tipo de combustível do veículo", consumos)

# Parâmetros do financiamento
taxa_juros = st.number_input("Taxa de juros ao ano (%)", min_value=0.0, value=5.0)
numero_parcelas = st.number_input("Número de parcelas", min_value=1, value=12)
tipo_parcela = st.selectbox("Modalidade de parcelamento", ["mensal", "trimestral", "semestral", "anual"])
tipo_tabela = st.selectbox("Tabela aplicada no cálculo de financiamento", ["PRICE", "SAC"])
entrada = st.number_input("Valor da entrada", min_value=0.0, value=12000.0)

# Botão para continuar
if st.button("Calcular"):
    # Cálculo da depreciação
    dados_depreciacao = depreciacao(tipo_selecionado, marca_selecionada, modelo_selecionado, ano_selecionado, consumo_selecionado)
    
    # Cálculo do financiamento
    dados_financiamento = financiamento(tipo_selecionado, marca_selecionada, modelo_selecionado, ano_selecionado, consumo_selecionado, taxa_juros, numero_parcelas, tipo_parcela, tipo_tabela, entrada)
    
    # Preparação dos dados para o gráfico
    meses_depreciacao, valores_depreciacao = zip(*dados_depreciacao)
    meses_financiamento, valores_financiamento = zip(*dados_financiamento)
    
    # Criação do gráfico
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=meses_depreciacao, y=valores_depreciacao, mode='lines', name='Depreciação'))
    fig.add_trace(go.Scatter(x=meses_financiamento, y=valores_financiamento, mode='lines', name='Financiamento'))
    
    # Configuração do layout do gráfico
    fig.update_layout(title='Depreciação e Financiamento do Veículo',
                      xaxis_title='Meses',
                      yaxis_title='Valores (R$)',
                      legend_title='Linhas')
    
    # Exibição do gráfico
    st.plotly_chart(fig)