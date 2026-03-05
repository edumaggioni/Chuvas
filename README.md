Site: https://cemcchuvas.netlify.app/

# 🌧️ Sistema Impacto Climático

Dashboard analítico interativo para análise de **chuvas e desastres naturais no Brasil (2010–2025)**.

O sistema foi desenvolvido em **Python**, utilizando **Streamlit** para interface web e **Plotly** para visualizações analíticas. Ele permite explorar dados de precipitação, eventos extremos e impactos humanos em diferentes regiões do país.

---

## 📊 Visão Geral

| Atributo                | Descrição              |
| ----------------------- | ---------------------- |
| Linguagem               | Python 3.10+           |
| Interface               | Streamlit              |
| Visualização            | Plotly                 |
| Período de dados        | 2010 – 2025            |
| Estações meteorológicas | 30 cidades brasileiras |
| Eventos de desastres    | 825+ registros         |
| Registros de chuva      | 175.000+ medições      |

---

## 🖥️ Demonstração

O dashboard permite visualizar:

* Ranking de cidades com **maior volume de chuva**
* Evolução temporal da precipitação
* Correlação entre **chuva e desastres naturais**
* Mapa interativo com estações meteorológicas
* Impacto humano de eventos extremos

---

## 🚀 Instalação

### Pré-requisitos

* Python **3.10 ou superior**
* pip instalado

Download do Python:

[https://www.python.org/downloads/](https://www.python.org/downloads/)

---

## ⚙️ Execução Rápida

### Windows

Basta executar:

```
iniciar.bat
```

O script instalará as dependências e abrirá o dashboard automaticamente no navegador.

---

### Execução Manual

1️⃣ Instalar dependências

```
pip install -r requirements.txt
```

2️⃣ Gerar dados de demonstração (primeira execução)

```
python gerar_dados.py
```

3️⃣ Iniciar o sistema

```
python main.py
```

O dashboard abrirá em:

```
http://localhost:8501
```

---

# 📂 Estrutura do Projeto

```
impacto_climatico/

├── main.py
├── dashboard.py
├── gerar_dados.py
├── coletor_dados.py
├── processamento_dados.py
├── iniciar.bat
├── requirements.txt
└── data/
    ├── chuva.csv
    ├── desastres.csv
    └── eventos_combinados.csv
```

---

# 📈 Funcionalidades do Dashboard

## Filtros

* Ano (2010 – 2025)
* Mês
* Quantidade de cidades exibidas
* Exibição do mapa interativo

---

## Indicadores Principais

O sistema apresenta **KPIs em tempo real**:

* Chuva acumulada
* Número de desastres
* Óbitos
* Feridos
* Desabrigados
* Desalojados
* Pessoas afetadas

---

## Visualizações

O dashboard inclui:

* 📊 **Top Municípios por Chuva**
* 📈 **Evolução Temporal**
* 🔵 **Correlação Chuva × Desastres**
* 🥧 **Tipos de Desastre**
* 🔥 **Heatmap Sazonal**
* 📉 **Tendência Histórica**
* 👥 **Impacto Humano**
* 📋 **Eventos Extremos**

---

# 🗺️ Cobertura Geográfica

O sistema monitora **30 cidades brasileiras**, distribuídas nas cinco regiões:

* Norte
* Nordeste
* Centro-Oeste
* Sudeste
* Sul

Incluindo cidades como:

* São Paulo
* Rio de Janeiro
* Belo Horizonte
* Porto Alegre
* Recife
* Manaus
* Curitiba

---

# 🌎 Integração com APIs

O sistema permite integração com dados públicos.

### INMET

Instituto Nacional de Meteorologia.

[https://apitempo.inmet.gov.br/](https://apitempo.inmet.gov.br/)

### S2ID

Sistema Integrado de Informações sobre Desastres.

[https://s2id.mi.gov.br/](https://s2id.mi.gov.br/)

### CEMADEN

Centro Nacional de Monitoramento e Alertas de Desastres Naturais.

---

# 📊 Análises Estatísticas

O módulo `processamento_dados.py` inclui:

* Correlação de **Pearson**
* Ranking de anos mais chuvosos
* Identificação de eventos extremos
* Análise de tendência climática
* Relatórios por período

---

# 📦 Dependências

Principais bibliotecas utilizadas:

```
streamlit
plotly
pandas
numpy
scipy
requests
folium
```

Instalar tudo com:

```
pip install -r requirements.txt
```

---

# 🛠️ Problemas Comuns

| Erro                     | Solução                   |
| ------------------------ | ------------------------- |
| ModuleNotFoundError      | instalar dependências     |
| chuva.csv não encontrado | rodar gerar_dados.py      |
| mapa não aparece         | verificar internet        |
| porta 8501 ocupada       | fechar instância anterior |

---

# 📚 Fontes de Dados

* INMET – Instituto Nacional de Meteorologia
* S2ID – Ministério da Integração Nacional
* CEMADEN – Monitoramento de desastres naturais

---

# 📄 Licença

Este projeto é destinado para **uso educacional, pesquisa e demonstração de análise climática**.

---

💻 Projeto desenvolvido em **Python + Streamlit + Plotly**

---

Se quiser, também posso te entregar:

* **README nível profissional (padrão projetos grandes de GitHub)**
* **README com imagens do dashboard**
* **README com GIF do sistema rodando**
* **README com badges automáticas (Python, licença, build, etc.)**

que deixa o repositório **bem mais bonito e profissional**.
