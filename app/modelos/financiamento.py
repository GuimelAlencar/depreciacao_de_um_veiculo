import json

def calculo_financiamento(
        valor_financiado, 
        taxa_de_juros_ao_ano, 
        numero_de_parcelas,
        tipo_de_parcela="mensal",
        tipo_de_tabela="PRICE",
        entrada=None,
    ):
    
    # Abatimento do valor de entrada
    if entrada is not None:
        valor_financiado -= entrada
    
    # Calculo da taxa de juros anual
    taxa_de_juros_aa_decimal = taxa_de_juros_ao_ano / 100
    
    # Define o intervalo em meses entre parcelas
    meses_por_parcela = {
        "anual": 12,
        "semestral": 6,
        "trimestral": 3,
        "mensal": 1
    }
    
    # Verifica se o tipo de parcela é válido
    if tipo_de_parcela.lower() not in meses_por_parcela:
        raise ValueError("Tipo de parcelas inválido.")
        
    intervalo_meses = meses_por_parcela[tipo_de_parcela.lower()]
    
    # Calculo da taxa de juros em relação à modalidade de parcelamento
    match tipo_de_parcela.lower():
        case "anual":
            taxa_de_juros_aa_d_por_parcela = taxa_de_juros_aa_decimal
        case "semestral":
            taxa_de_juros_aa_d_por_parcela = taxa_de_juros_aa_decimal / 2 
        case "trimestral":
            taxa_de_juros_aa_d_por_parcela = taxa_de_juros_aa_decimal / 4
        case "mensal":
            taxa_de_juros_aa_d_por_parcela = taxa_de_juros_aa_decimal / 12
    
    # Calculo das parcelas
    match tipo_de_tabela:
        # PRICE - Valores fixos, conta simples
        case "PRICE":
            # Se a taxa de juros for 0, só divide o valor financiado pelo numero de tabelas
            if taxa_de_juros_aa_d_por_parcela == 0:
                valor_parcela = valor_financiado / numero_de_parcelas
                # Cria uma lista com todos os meses, preenchendo com 0 os meses sem parcela
                parcelas = []
                for mes in range(1, (numero_de_parcelas * intervalo_meses) + 1):
                    if mes % intervalo_meses == 0:  # Se é mês de pagamento
                        parcelas.append((mes, valor_parcela))
                    else:  # Se não é mês de pagamento
                        parcelas.append((mes, 0))
            else:
                # Calculo do valor da parcela
                valor_parcela = (
                    valor_financiado * 
                    (taxa_de_juros_aa_d_por_parcela * (1 + taxa_de_juros_aa_d_por_parcela) ** numero_de_parcelas) / 
                    ((1 + taxa_de_juros_aa_d_por_parcela) ** numero_de_parcelas - 1)
                    )
                # Cria uma lista com todos os meses, preenchendo com 0 os meses sem parcela
                parcelas = []
                for mes in range(1, (numero_de_parcelas * intervalo_meses) + 1):
                    if mes % intervalo_meses == 0:  # Se é mês de pagamento
                        parcelas.append((mes, round(valor_parcela, 2)))
                    else:  # Se não é mês de pagamento
                        parcelas.append((mes, 0))
            
            return tuple(parcelas)
            
        # SAC - Parcelas constantemente amortizadas
        case "SAC":
            # Se a taxa de juros for 0, só divide o valor financiado pelo numero de tabelas
            if taxa_de_juros_aa_d_por_parcela == 0:
                valor_amortizacao = valor_financiado / numero_de_parcelas
                parcelas = []
                for mes in range(1, (numero_de_parcelas * intervalo_meses) + 1):
                    if mes % intervalo_meses == 0:  # Se é mês de pagamento
                        parcelas.append((mes, valor_amortizacao))
                    else:  # Se não é mês de pagamento
                        parcelas.append((mes, 0))

            else:
                # Calcula o valor padrão da amortização
                valor_amortizacao = valor_financiado / numero_de_parcelas
                
                # Define o saldo necessário para quitar o financiamento
                saldo_devedor = valor_financiado
                
                parcelas = []
                parcela_atual = 0
                
                for mes in range(1, (numero_de_parcelas * intervalo_meses) + 1):
                    if mes % intervalo_meses == 0:  # Se é mês de pagamento
                        juros = saldo_devedor * taxa_de_juros_aa_d_por_parcela
                        valor_parcela = valor_amortizacao + juros
                        parcelas.append((mes, round(valor_parcela, 2)))
                        saldo_devedor -= valor_amortizacao
                        parcela_atual += 1
                    else:  # Se não é mês de pagamento
                        parcelas.append((mes, 0))
                        
            return tuple(parcelas)
            
        case _:
            raise ValueError("Tipo de tabela inválido.")