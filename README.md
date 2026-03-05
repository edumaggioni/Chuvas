Site: https://cemcchuvas.netlify.app/

# 🌧️ Sistema Impacto Climático

<<<<<<< HEAD
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-dashboard-red)
![Plotly](https://img.shields.io/badge/plotly-visualization-blue)
![Status](https://img.shields.io/badge/status-active-success)
![License](https://img.shields.io/badge/license-MIT-green)

Dashboard analítico interativo para **monitoramento de precipitação e análise de desastres naturais no Brasil (2010–2025)**.

O sistema coleta, processa e visualiza dados climáticos utilizando **Python**, **Streamlit** e **Plotly**, permitindo análise estatística, exploração visual e identificação de eventos extremos.

---

# 📊 Visão Geral

O **Sistema Impacto Climático** foi desenvolvido para análise integrada entre **dados de precipitação** e **eventos de desastres naturais**, permitindo identificar padrões, tendências e impactos humanos ao longo do tempo.

### Principais características

* Dashboard interativo em navegador
* Visualização geográfica das estações
* Correlação entre chuva e desastres
* Rankings climáticos por município
* Análise de eventos extremos
* Estatísticas históricas
* Integração com APIs meteorológicas públicas

---

# 🖥️ Interface do Dashboard

O sistema apresenta:

* Indicadores climáticos em tempo real
* Mapa interativo com estações meteorológicas
* Análise temporal de precipitação
* Correlação entre eventos climáticos e desastres
* Rankings municipais
* Impacto humano anual

---

# 📈 Indicadores Principais

O dashboard apresenta **KPIs atualizados dinamicamente** conforme os filtros aplicados.

| Indicador       | Descrição                               |
| --------------- | --------------------------------------- |
| Chuva acumulada | Volume total de precipitação no período |
| Desastres       | Número de eventos registrados           |
| Óbitos          | Mortes confirmadas                      |
| Feridos         | Pessoas feridas                         |
| Desabrigados    | Pessoas que perderam moradia            |
| Desalojados     | Pessoas deslocadas temporariamente      |
| Afetados        | Total de pessoas impactadas             |

---

# 📊 Visualizações Analíticas

O sistema inclui múltiplos tipos de análise:

| Visualização                 | Tipo               |
| ---------------------------- | ------------------ |
| Top Municípios por Chuva     | Barras horizontais |
| Evolução Temporal            | Linha com área     |
| Correlação Chuva × Desastres | Scatter            |
| Distribuição de Desastres    | Donut              |
| Heatmap Sazonal              | Mapa de calor      |
| Tendência Histórica          | Barras + linha     |
| Impacto Humano               | Gráfico multilinha |
| Eventos Extremos             | Tabela interativa  |

---

# 🗺️ Cobertura Geográfica

O sistema monitora **30 cidades distribuídas nas cinco regiões do Brasil**.

### Regiões monitoradas

**Norte**

* Manaus
* Belém
* Macapá
* Porto Velho
* Rio Branco
* Boa Vista

**Nordeste**

* Salvador
* Recife
* Fortaleza
* Natal
* Teresina
* São Luís
* Maceió

**Centro-Oeste**

* Goiânia
* Brasília
* Campo Grande
* Cuiabá

**Sudeste**

* São Paulo
* Rio de Janeiro
* Belo Horizonte
* Vitória
* Petrópolis
* Angra dos Reis
* Nova Friburgo
* Teresópolis

**Sul**

* Curitiba
* Florianópolis
* Joinville
* Blumenau
* Porto Alegre

---

# ⚙️ Tecnologias Utilizadas

| Tecnologia | Uso                     |
| ---------- | ----------------------- |
| Python     | Linguagem principal     |
| Streamlit  | Interface web           |
| Plotly     | Visualização interativa |
| Pandas     | Manipulação de dados    |
| NumPy      | Cálculos numéricos      |
| SciPy      | Estatística             |
| Requests   | Integração com APIs     |
| Folium     | Mapas geográficos       |
=======
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
>>>>>>> 63316643db8d0466212af000352573f4946392d5

---

# 📂 Estrutura do Projeto

```
impacto_climatico/

<<<<<<< HEAD
main.py
dashboard.py
gerar_dados.py
coletor_dados.py
processamento_dados.py

requirements.txt
iniciar.bat

data/
    chuva.csv
    desastres.csv
    eventos_combinados.csv
```

### Descrição dos módulos

| Arquivo                | Função                           |
| ---------------------- | -------------------------------- |
| main.py                | Inicialização do sistema         |
| dashboard.py           | Interface Streamlit              |
| gerar_dados.py         | Geração de dados de demonstração |
| coletor_dados.py       | Integração com APIs externas     |
| processamento_dados.py | Análises estatísticas            |

---

# 🚀 Instalação

## Pré-requisitos

* Python **3.10 ou superior**
* pip

Download:

[https://www.python.org/downloads/](https://www.python.org/downloads/)

---

# ▶️ Execução

### Instalar dependências

```bash
pip install -r requirements.txt
```

### Gerar base de dados

```bash
python gerar_dados.py
```

### Iniciar o dashboard

```bash
python main.py
```

Acesse no navegador:

```
http://localhost:8501
=======
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
>>>>>>> 63316643db8d0466212af000352573f4946392d5
```

---

<<<<<<< HEAD
# 🔌 Integração com APIs Públicas

O sistema suporta integração com fontes oficiais.

### INMET

Instituto Nacional de Meteorologia
Dados meteorológicos de estações automáticas.

[https://apitempo.inmet.gov.br/](https://apitempo.inmet.gov.br/)

---

=======
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

>>>>>>> 63316643db8d0466212af000352573f4946392d5
### S2ID

Sistema Integrado de Informações sobre Desastres.

[https://s2id.mi.gov.br/](https://s2id.mi.gov.br/)

<<<<<<< HEAD
---

=======
>>>>>>> 63316643db8d0466212af000352573f4946392d5
### CEMADEN

Centro Nacional de Monitoramento e Alertas de Desastres Naturais.

---

<<<<<<< HEAD
# 📊 Análises Estatísticas Disponíveis
=======
# 📊 Análises Estatísticas
>>>>>>> 63316643db8d0466212af000352573f4946392d5

O módulo `processamento_dados.py` inclui:

* Correlação de **Pearson**
<<<<<<< HEAD
* Identificação de eventos extremos
* Ranking de anos mais chuvosos
* Análise de tendência climática
* Relatórios personalizados por período

Exemplo de uso:

```python
from processamento_dados import *

df_chuva, df_desastres = carregar_dados()

corr = calcular_correlacao(df_chuva, df_desastres)

print(corr)
```
=======
* Ranking de anos mais chuvosos
* Identificação de eventos extremos
* Análise de tendência climática
* Relatórios por período
>>>>>>> 63316643db8d0466212af000352573f4946392d5

---

# 📦 Dependências

<<<<<<< HEAD
Instalação automática:

```bash
pip install -r requirements.txt
```

Principais bibliotecas:
=======
Principais bibliotecas utilizadas:
>>>>>>> 63316643db8d0466212af000352573f4946392d5

```
streamlit
plotly
pandas
numpy
scipy
requests
folium
```

<<<<<<< HEAD
---

# 🛠️ Troubleshooting

| Problema                 | Solução                   |
| ------------------------ | ------------------------- |
| ModuleNotFoundError      | instalar dependências     |
| chuva.csv não encontrado | executar gerar_dados.py   |
| mapa não aparece         | verificar conexão         |
=======
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
>>>>>>> 63316643db8d0466212af000352573f4946392d5
| porta 8501 ocupada       | fechar instância anterior |

---

# 📚 Fontes de Dados

<<<<<<< HEAD
Dados climáticos e históricos baseados em:

* Instituto Nacional de Meteorologia
* Sistema Integrado de Informações sobre Desastres
* Centro Nacional de Monitoramento de Desastres Naturais
=======
* INMET – Instituto Nacional de Meteorologia
* S2ID – Ministério da Integração Nacional
* CEMADEN – Monitoramento de desastres naturais
>>>>>>> 63316643db8d0466212af000352573f4946392d5

---

# 📄 Licença

<<<<<<< HEAD
Este projeto está licenciado sob a licença **MIT**.

---

# 👨‍💻 Autor

**Eduardo Maggioni**



que deixa seu projeto **bem mais forte para portfólio ou apresentação técnica**.
=======
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
>>>>>>> 63316643db8d0466212af000352573f4946392d5
