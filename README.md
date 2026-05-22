# Controle de Resultado MZ

Aplicação web para controle e análise de resultados desenvolvida com **Streamlit**.

## 🚀 Quick Start

### Pré-requisitos
- Python 3.8+
- pip

### Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/splintter2107/Controle-de-Resultado-Mz.git
cd Controle-de-Resultado-Mz
```

2. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

3. **Execute a aplicação:**
```bash
streamlit run app.py
```

A aplicação estará disponível em `http://localhost:8501`

## 📁 Estrutura do Projeto

```
Controle-de-Resultado-Mz/
├── app.py                 # Aplicação principal
├── requirements.txt       # Dependências Python
├── README.md             # Este arquivo
├── .gitignore            # Arquivo de exclusão Git
├── config/
│   ├── __init__.py
│   └── settings.py       # Configurações globais
├── services/
│   ├── __init__.py
│   └── data_manager.py   # Gerenciador de dados
├── components/
│   ├── __init__.py
│   └── charts.py         # Componentes de gráficos
├── utils/
│   ├── __init__.py
│   └── helpers.py        # Funções auxiliares
└── data/
    ├── uploads/          # Arquivos importados
    └── exports/          # Arquivos exportados
```

## 📊 Funcionalidades

### 📈 Dashboard
- Visão geral dos dados
- Métricas principais
- Visualização de dados

### 📥 Importar Dados
- Suporte a arquivos Excel (.xlsx, .xls)
- Suporte a arquivos CSV
- Validação automática
- Preview dos dados

### 📉 Análises
- Estatísticas descritivas
- Gráficos interativos
- Comparações de períodos

### ⚙️ Configurações
- Informações da aplicação
- Ajustes de visualização

## 🎨 Configurações

Todas as configurações centralizadas em `config/settings.py`:
- Cores da aplicação
- Diretórios de dados
- Limites de upload
- Formatos de exibição

## 📦 Dependências Principais

- **streamlit** - Framework web
- **pandas** - Manipulação de dados
- **plotly** - Gráficos interativos
- **openpyxl** - Suporte Excel

## 🤝 Como Publicar para seu Chefe

### ✅ OPÇÃO 1: STREAMLIT CLOUD (Recomendado - GRÁTIS)

**Melhor opção:** Fácil, grátis, automático!

1. **Prepare o repositório:**
   ```bash
   git add .
   git commit -m "Project restructure complete"
   git push origin project-restructure
   ```

2. **Faça Pull Request e Merge:**
   - Vá ao GitHub
   - Crie PR de `project-restructure` → `main`
   - Merge quando aprovado

3. **Deploy:**
   - Acesse https://share.streamlit.io
   - Clique "New app"
   - Selecione: `splintter2107/Controle-de-Resultado-Mz`
   - Branch: `main`, Main file: `app.py`
   - Deploy!

4. **Compartilhe:**
   ```
   https://seu-app-name.streamlit.app
   ```

✅ **Seu chefe acessa em qualquer navegador!**

---

### 🚀 OPÇÃO 2: RAILWAY (Moderno, Fácil)

1. Vá a https://railway.app
2. Clique "New Project" → "Deploy from GitHub"
3. Selecione seu repositório
4. Railway detecta automaticamente
5. Compartilhe o link público

✅ **Interface mais moderna que Streamlit Cloud**

---

### 💻 OPÇÃO 3: SERVIDOR DA EMPRESA

Se tiver servidor próprio:

```bash
# No servidor
git clone https://github.com/splintter2107/Controle-de-Resultado-Mz.git
cd Controle-de-Resultado-Mz
pip install -r requirements.txt
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

URL para seu chefe: `http://seu-servidor:8501`

✅ **Máxima segurança, dados internos**

---

## 🔒 Segurança

Antes de compartilhar com seu chefe:

1. Configure `.streamlit/config.toml`:
```toml
[browser]
serverAddress = "seu-dominio.com"
serverPort = 8501

[server]
runOnSave = true
maxUploadSize = 10
```

2. Adicione autenticação em `app.py` (se necessário)

3. Use variáveis de ambiente para senhas

## 📞 Suporte

Para dúvidas, abra uma issue no repositório.

---

**Desenvolvido com ❤️ usando Streamlit**
