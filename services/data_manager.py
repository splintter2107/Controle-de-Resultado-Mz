"""
Gerenciador de dados e operações com arquivos
"""

import pandas as pd
from pathlib import Path
from config.settings import UPLOADS_DIR, EXPORTS_DIR, ALLOWED_EXTENSIONS
from datetime import datetime


class DataManager:
    """Classe para gerenciar dados da aplicação"""

    @staticmethod
    def carregar_arquivo(caminho_arquivo):
        """
        Carrega dados de arquivo Excel ou CSV
        
        Args:
            caminho_arquivo: Path para o arquivo
        
        Returns:
            DataFrame ou None se houver erro
        """
        try:
            extensao = Path(caminho_arquivo).suffix.lower()
            
            if extensao in [".xlsx", ".xls"]:
                return pd.read_excel(caminho_arquivo)
            elif extensao == ".csv":
                return pd.read_csv(caminho_arquivo, encoding="utf-8")
            
            return None
        except Exception as e:
            print(f"Erro ao carregar arquivo: {e}")
            return None

    @staticmethod
    def salvar_arquivo(df, nome_arquivo, tipo="xlsx"):
        """
        Salva DataFrame em arquivo
        
        Args:
            df: DataFrame a salvar
            nome_arquivo: Nome do arquivo
            tipo: Tipo de arquivo (xlsx, csv)
        
        Returns:
            Path do arquivo salvo ou None
        """
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            nome_base = Path(nome_arquivo).stem
            
            if tipo == "xlsx":
                nome_final = f"{nome_base}_{timestamp}.xlsx"
                caminho = EXPORTS_DIR / nome_final
                df.to_excel(caminho, index=False)
            elif tipo == "csv":
                nome_final = f"{nome_base}_{timestamp}.csv"
                caminho = EXPORTS_DIR / nome_final
                df.to_csv(caminho, index=False, encoding="utf-8")
            
            return caminho
        except Exception as e:
            print(f"Erro ao salvar arquivo: {e}")
            return None

    @staticmethod
    def validar_arquivo(arquivo):
        """
        Valida se o arquivo é aceito
        
        Args:
            arquivo: Arquivo do Streamlit
        
        Returns:
            True se válido, False caso contrário
        """
        extensao = Path(arquivo.name).suffix.lower()
        return extensao in ALLOWED_EXTENSIONS

    @staticmethod
    def listar_arquivos_upload():
        """
        Lista arquivos da pasta de upload
        
        Returns:
            Lista de caminhos dos arquivos
        """
        return sorted(UPLOADS_DIR.glob("*.*"))

    @staticmethod
    def listar_arquivos_export():
        """
        Lista arquivos da pasta de exportação
        
        Returns:
            Lista de caminhos dos arquivos
        """
        return sorted(EXPORTS_DIR.glob("*.*"))

    @staticmethod
    def filtrar_dados(df, filtros):
        """
        Aplica filtros a um DataFrame
        
        Args:
            df: DataFrame
            filtros: Dicionário com filtros {coluna: valor}
        
        Returns:
            DataFrame filtrado
        """
        resultado = df.copy()
        
        for coluna, valor in filtros.items():
            if coluna in resultado.columns and valor is not None:
                if isinstance(valor, list):
                    resultado = resultado[resultado[coluna].isin(valor)]
                else:
                    resultado = resultado[resultado[coluna] == valor]
        
        return resultado

    @staticmethod
    def gerar_resumo_dados(df):
        """
        Gera resumo estatístico dos dados
        
        Args:
            df: DataFrame
        
        Returns:
            Dicionário com resumo
        """
        return {
            "total_linhas": len(df),
            "total_colunas": len(df.columns),
            "colunas": list(df.columns),
            "tipos": dict(df.dtypes),
            "valores_faltantes": dict(df.isnull().sum())
        }
