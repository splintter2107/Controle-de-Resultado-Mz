"""
Funções para criar gráficos e visualizações
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from config.settings import ORDEM_MESES, COLORS


def criar_grafico_linha_evolucao(df, x_col, y_col, titulo_x="", titulo_y=""):
    """
    Cria gráfico de linha com evolução
    
    Args:
        df: DataFrame com os dados
        x_col: Coluna para eixo X
        y_col: Coluna para eixo Y
        titulo_x: Título eixo X
        titulo_y: Título eixo Y
    
    Returns:
        Figure Plotly
    """
    fig = px.line(
        df,
        x=x_col,
        y=y_col,
        markers=True,
        text=y_col
    )

    fig.update_traces(
        line=dict(color=COLORS["primary"], width=3),
        marker=dict(size=8),
        textposition="top center"
    )

    fig.update_layout(
        height=330,
        margin=dict(l=10, r=10, t=25, b=10),
        xaxis_title=titulo_x,
        yaxis_title=titulo_y,
        showlegend=False,
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    return fig


def criar_grafico_barras_horizontal(df, x_col, y_col, text_col=None, titulo=""):
    """
    Cria gráfico de barras horizontal
    
    Args:
        df: DataFrame com os dados
        x_col: Coluna para eixo X (valor)
        y_col: Coluna para eixo Y (categoria)
        text_col: Coluna para texto dentro da barra (opcional)
        titulo: Título do gráfico
    
    Returns:
        Figure Plotly
    """
    fig = px.bar(
        df,
        x=x_col,
        y=y_col,
        orientation="h",
        text=text_col or x_col
    )

    fig.update_traces(
        marker_color=COLORS["primary"],
        texttemplate="%{text}%",
        textposition="inside",
        textfont=dict(color="#FFFFFF", size=13)
    )

    fig.update_layout(
        height=350,
        margin=dict(l=10, r=40, t=20, b=10),
        xaxis_visible=False,
        yaxis_title="",
        yaxis=dict(
            autorange="reversed",
            tickfont=dict(size=13, color=COLORS["text_dark"])
        ),
        plot_bgcolor="white",
        paper_bgcolor="white",
        showlegend=False
    )

    return fig


def criar_grafico_dupla_linha(df, x_col, y_col1, y_col2, nome1="", nome2=""):
    """
    Cria gráfico com duas linhas
    
    Args:
        df: DataFrame
        x_col: Coluna eixo X
        y_col1: Primeira coluna Y
        y_col2: Segunda coluna Y
        nome1: Nome série 1
        nome2: Nome série 2
    
    Returns:
        Figure Plotly
    """
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df[x_col],
            y=df[y_col1],
            mode="lines+markers+text",
            text=df[y_col1],
            textposition="top center",
            name=nome1,
            line=dict(color=COLORS["primary"], width=3)
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df[x_col],
            y=df[y_col2],
            mode="lines+markers+text",
            text=df[y_col2],
            textposition="bottom center",
            name=nome2,
            line=dict(color=COLORS["blue"], width=3)
        )
    )

    fig.update_layout(
        height=320,
        margin=dict(l=10, r=10, t=25, b=10),
        xaxis=dict(
            title=None,
            showgrid=False
        ),
        yaxis=dict(
            title=None,
            showgrid=False
        ),
        legend=dict(
            orientation="h",
            y=1.05,
            x=0
        ),
        plot_bgcolor="white",
        paper_bgcolor="white",
        showlegend=True
    )

    return fig
