from controle import depreciacao, financiamento, get_dados_db

dados_depreciacao = depreciacao(
    #Tipo
    "carro", 
    # Marca
    "toyota",
    # Modelo
    "corolla",
    # Ano de fabricação
    "2020",
    # Tipo de consumo
    "gasolina"
)

# Printing data
print("Depreciação de um toyota corolla 2020: ")
for mes, valor in dados_depreciacao:
    print(f"{mes}º mes: R${valor}")
print("")

dados_depreciacao = depreciacao(
    #Tipo
    "carro", 
    # Marca
    "toyota",
    # Modelo
    "corolla",
    # Ano de fabricação
    "2024",
    # Tipo de consumo
    "gasolina"
)

# Printing data
print("Depreciação de um toyota corolla 2024: ")
for mes, valor in dados_depreciacao:
    print(f"{mes}º mes: R${valor}")
print("")

# Testes financiamento
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
print("Financiamento pela PRICE: ")
for parcela, valor in dados_do_financiamento:
    print(f"{parcela}º parcela: R${valor}")
print("")

dados_do_financiamento = financiamento(
    #Tipo
    "carro", 
    # Marca
    "toyota",
    # Modelo
    "corolla",
    # Ano de fabricação
    "2024",
    # Tipo de consumo
    "gasolina",
    # 5%
    5,
    # 12 parcelas
    12,
    # Modalidade de parcelamento: mensal
    "mensal",
    # Tabela aplicada no cálculo de financiamento
    "SAC",
    # Entrada
    12000, 
)

# Printing data
print("Financiamento pela SAC: ")
for parcela, valor in dados_do_financiamento:
    print(f"{parcela}º parcela: R${valor}")
print("")

# testes dados_db
tipos_de_veiculos = get_dados_db("tipos")
print(f"Todos os tipos de veículos cadastrados no db: {tipos_de_veiculos}")

for tipo in tipos_de_veiculos:
    marcas_de_um_tipo_de_veiculo = get_dados_db("marcas", tipo)
    print(f"Todas as marcas de {tipo} cadastrados no db: {marcas_de_um_tipo_de_veiculo}")

    for marca in marcas_de_um_tipo_de_veiculo:
        modelos_de_uma_marca = get_dados_db("modelos", tipo, marca)
        print(f"Todas os modelos de {tipo} da marca {marca} cadastrados no db: {modelos_de_uma_marca}")
print("")