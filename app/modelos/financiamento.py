'''Model responsavel pelo cálculo de um determinado financiamento.'''

# Biblioteca para a leitura do db
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
        case _:
            raise ValueError("Tipo de parcelas inválido.")
    
    # Calculo das parcelas
    match tipo_de_tabela:
        # PRICE - Valores fixos, conta simples
        case "PRICE":
            # Se a taxa de juros for 0, só divide o valor financiado pelo numero de tabelas
            if taxa_de_juros_aa_d_por_parcela == 0:
                valor_parcela = valor_financiado / numero_de_parcelas
                # Cria uma lista de tuplas onde cada tupla deve indicar um período do parcelamento e uma parcela
                # TODO: Deve retornar a variação em meses, não em parcelas
                parcelas = [(parcela + 1, valor_parcela) for parcela in range(numero_de_parcelas)]
            else:
                # Calculo do valor da parcela
                valor_parcela = (
                    # Aqui é só formula, ignore
                    valor_financiado * 
                    (taxa_de_juros_aa_d_por_parcela * (1 + taxa_de_juros_aa_d_por_parcela) ** numero_de_parcelas) / 
                    ((1 + taxa_de_juros_aa_d_por_parcela) ** numero_de_parcelas - 1)
                    )
                # Cria uma lista de tuplas onde cada tupla deve indicar um período do parcelamento e uma parcela
                # TODO: Deve retornar a variação em meses, não em parcelas
                parcelas = [(parcela + 1, round(valor_parcela, 2)) for parcela in range(numero_de_parcelas)]
            # Transforma a lista em uma tupla e a retorna
            return tuple(parcelas)
        # SAC - Parcelas constantemente amortizadas
        case "SAC":
            # Se a taxa de juros for 0, só divide o valor financiado pelo numero de tabelas
            if taxa_de_juros_aa_d_por_parcela == 0:
                valor_amortizacao = valor_financiado / numero_de_parcelas
                # TODO: Deve retornar a variação em meses, não em parcelas
                parcelas = [(parcela + 1, valor_amortizacao) for parcela in range(numero_de_parcelas)]

            else:
                # Calcula o valor padrão da amortização
                valor_amortizacao = valor_financiado / numero_de_parcelas
                
                # Define o saldo necessário para quitar o financiamento (no momento igual ao valor financiado)
                saldo_devedor = valor_financiado
                
                parcelas = []
                
                # Fórmula - ignore
                for parcela in range(numero_de_parcelas):
                    juros = saldo_devedor * taxa_de_juros_aa_d_por_parcela
                    valor_parcela = valor_amortizacao + juros
                    # TODO: Deve retornar a variação em meses, não em parcelas
                    parcelas.append((parcela + 1, round(valor_parcela, 2)))
                    saldo_devedor -= valor_amortizacao
            # Transforma a lista em uma tupla e a retorna
            return tuple(parcelas)
        case _:
            raise ValueError("Tipo de tabela inválido.")