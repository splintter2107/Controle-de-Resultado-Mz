"""
Funções auxiliares gerais
"""

import pandas as pd
from datetime import datetime
from config.settings import CURRENCY_SYMBOL, DEFAULT_DECIMAL_PLACES


def formatar_moeda(valor):
    """
    Formata valor para moeda brasileira
    
    Args:
        valor: Valor numérico
    
    Returns:
        String formatada
    """
    try:
        return f"{CURRENCY_SYMBOL} {valor:,.{DEFAULT_DECIMAL_PLACES}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except:
        return f"{CURRENCY_SYMBOL} 0,00"


def formatar_percentual(valor):
    """
    Formata valor como percentual
    
    Args:
        valor: Valor numérico
    
    Returns:
        String formatada
    """
    try:
        return f"{valor:.{DEFAULT_DECIMAL_PLACES}f}%"
    except:
        return "0,00%"


def formatar_data(data):
    """
    Formata data para formato brasileiro
    
    Args:
        data: Data (datetime ou string)
    
    Returns:
        String formatada
    """
    try:
        if isinstance(data, str):
            data = pd.to_datetime(data)
        return data.strftime("%d/%m/%Y")
    except:
        return "-"


def formatar_numero(valor, casas_decimais=2):
    """
    Formata número com casas decimais
    
    Args:
        valor: Valor numérico
        casas_decimais: Número de casas decimais
    
    Returns:
        String formatada
    """
    try:
        return f"{valor:,.{casas_decimais}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except:
        return "0,00"


def calcular_variacao(valor_anterior, valor_atual):
    """
    Calcula variação percentual entre dois valores
    
    Args:
        valor_anterior: Valor anterior
        valor_atual: Valor atual
    
    Returns:
        Valor de variação percentual
    """
    try:
        if valor_anterior == 0:
            return 0
        return ((valor_atual - valor_anterior) / valor_anterior) * 100
    except:
        return 0


def obter_mes_nome(numero_mes):
    """
    Obtém nome do mês pelo número
    
    Args:
        numero_mes: Número do mês (1-12)
    
    Returns:
        Nome do mês
    """
    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril",
        "Maio", "Junho", "Julho", "Agosto",
        "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    try:
        return meses[int(numero_mes) - 1]
    except:
        return "-"


def gerar_timestamp():
    """
    Gera timestamp atual
    
    Returns:
        String com timestamp
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
