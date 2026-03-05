Abaixo está um **README.md em nível profissional**, no padrão usado em projetos grandes do GitHub, com **badges, estrutura clara, seções técnicas, arquitetura e exemplos de uso**. Basta criar o arquivo **`README.md`** na raiz do repositório e colar.

---

# 🌧️ Sistema Impacto Climático

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

---

# 📂 Estrutura do Projeto

```
impacto_climatico/

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
```

---

# 🔌 Integração com APIs Públicas

O sistema suporta integração com fontes oficiais.

### INMET

Instituto Nacional de Meteorologia
Dados meteorológicos de estações automáticas.

[https://apitempo.inmet.gov.br/](https://apitempo.inmet.gov.br/)

---

### S2ID

Sistema Integrado de Informações sobre Desastres.

[https://s2id.mi.gov.br/](https://s2id.mi.gov.br/)

---

### CEMADEN

Centro Nacional de Monitoramento e Alertas de Desastres Naturais.

---

# 📊 Análises Estatísticas Disponíveis

O módulo `processamento_dados.py` inclui:

* Correlação de **Pearson**
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

---

# 📦 Dependências

Instalação automática:

```bash
pip install -r requirements.txt
```

Principais bibliotecas:

```
streamlit
plotly
pandas
numpy
scipy
requests
folium
```

---

# 🛠️ Troubleshooting

| Problema                 | Solução                   |
| ------------------------ | ------------------------- |
| ModuleNotFoundError      | instalar dependências     |
| chuva.csv não encontrado | executar gerar_dados.py   |
| mapa não aparece         | verificar conexão         |
| porta 8501 ocupada       | fechar instância anterior |

---

# 📚 Fontes de Dados

Dados climáticos e históricos baseados em:

* Instituto Nacional de Meteorologia
* Sistema Integrado de Informações sobre Desastres
* Centro Nacional de Monitoramento de Desastres Naturais

---

# 📄 Licença

Este projeto está licenciado sob a licença **MIT**.

---

# 👨‍💻 Autor

**Eduardo Maggioni**



que deixa seu projeto **bem mais forte para portfólio ou apresentação técnica**.
