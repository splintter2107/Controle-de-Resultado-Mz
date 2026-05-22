"""
Configurações gerais da aplicação
"""

import os
from pathlib import Path

# Diretórios
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
UPLOADS_DIR = DATA_DIR / "uploads"
EXPORTS_DIR = DATA_DIR / "exports"

# Criar diretórios se não existirem
DATA_DIR.mkdir(exist_ok=True)
UPLOADS_DIR.mkdir(exist_ok=True)
EXPORTS_DIR.mkdir(exist_ok=True)

# Cores da aplicação
COLORS = {
    "primary": "#1f77b4",
    "secondary": "#ff7f0e",
    "success": "#2ca02c",
    "danger": "#d62728",
    "warning": "#ff9800",
    "info": "#17a2b8",
    "light": "#f8f9fa",
    "dark": "#343a40",
    "white": "#ffffff",
    "text_dark": "#212529",
    "text_muted": "#6c757d",
    "blue": "#0066cc",
    "green": "#28a745",
    "red": "#dc3545"
}

# Ordem dos meses
ORDEM_MESES = [
    "Janeiro", "Fevereiro", "Março", "Abril",
    "Maio", "Junho", "Julho", "Agosto",
    "Setembro", "Outubro", "Novembro", "Dezembro"
]

# Configurações de upload
MAX_UPLOAD_SIZE = 10 * 1024 * 1024  # 10 MB
ALLOWED_EXTENSIONS = {".xlsx", ".xls", ".csv"}

# Configurações de página Streamlit
PAGE_CONFIG = {
    "page_title": "Controle de Resultado MZ",
    "page_icon": "📊",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# Configurações de dados
DEFAULT_DECIMAL_PLACES = 2
CURRENCY_SYMBOL = "R$"
