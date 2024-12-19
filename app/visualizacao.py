import streamlit as st
import plotly.graph_objects as go

from controle import depreciacao, financiamento, get_dados_db
st.title("Simulação de Depreciação e Financiamento de Veículos")

col1,col2 = st.columns(2)
with col1:
    tipo = st.selectbox("Tipo", get_dados_db("tipos"))
    marca = st.selectbox("Marca", get_dados_db("marcas", tipo) if tipo else [])
    modelo = st.selectbox("Modelo", get_dados_db("modelos", tipo, marca) if marca else [])
    ano = st.selectbox("Ano", get_dados_db("anos", tipo, marca, modelo) if modelo else [])
    consumo = st.selectbox("Combustível", get_dados_db("consumos", tipo, marca, modelo, ano) if ano else [])
with col2:
    taxa_juros = st.number_input("Taxa de juros (%)", min_value=0.0, value=5.0)
    numero_parcelas = st.number_input("Parcelas", min_value=1, value=12)
    tipo_parcela = st.selectbox("Modalidade", ["mensal", "trimestral", "semestral", "anual"])
    tipo_tabela = st.selectbox("Sistema", ["PRICE", "SAC"])
    entrada = st.number_input("Entrada (R$)", min_value=0.0, value=12000.0)
if st.button("Calcular"):

    dados_depreciacao = depreciacao(tipo, marca, modelo, ano, consumo)
    dados_financiamento = financiamento(tipo, marca, modelo, ano, consumo, taxa_juros, numero_parcelas, tipo_parcela, tipo_tabela, entrada)
    
    meses_depreciacao, valores_depreciacao = zip(*dados_depreciacao)
    meses_financiamento, valores_financiamento = zip(*dados_financiamento)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=meses_depreciacao, y=valores_depreciacao, mode='lines', name='Depreciação'))
    fig.add_trace(go.Scatter(x=meses_financiamento, y=valores_financiamento, mode='lines', name='Financiamento'))
    
    fig.update_layout(title='Depreciação e Financiamento do Veículo',
                      xaxis_title='Meses',
                      yaxis_title='Valores (R$)',
                      legend_title='Linhas')
    
    st.plotly_chart(fig)