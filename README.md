# 📊 Análise Estatística para Data Science

Este repositório contém implementações práticas de conceitos estatísticos fundamentais para Data Science, incluindo a resolução do **Desafio Obrigatório** proposto na disciplina de Estatística para Data Science (Curso ADS – 60h), ministrada pelo Prof. Dr. Welton Dionísio.

---

## 👨‍💻 Autor

**Bernardo Simões**  
📅 Data de execução: 17 de abril de 2025

---

## 🧠 Objetivos

1. **Análise de Vendas (Desafio Obrigatório)**: Analisar dados hipotéticos de vendas e despesas mensais de uma empresa, tratando valores ausentes e gerando estatísticas descritivas.

2. **Implementação de Conceitos Estatísticos**: Desenvolver scripts para cálculo e visualização de medidas estatísticas essenciais, testes de hipóteses e análises comparativas.

---

## 🛠️ Tecnologias Utilizadas

- Python 3.12
- pandas
- numpy
- matplotlib
- seaborn
- scipy
- openpyxl

---

## 📂 Conteúdo do Projeto

### 📁 Arquivos Principais

- `desafio_obrigatorio_vendas.ipynb`: Notebook com resolução do desafio de dados de vendas.
- `analise_vendas.py`: Script Python com implementações de conceitos estatísticos e visualizações.
- `vendas.xlsx`: Arquivo Excel com dados de vendas e despesas.

### 🧪 Funcionalidades Implementadas

#### 📊 Análise de Vendas (Desafio Obrigatório)
1. **Criação e carregamento** do arquivo Excel com dados de vendas e despesas.
2. **Tratamento de dados ausentes**:
   - Mediana para "Vendas"
   - Média para "Despesas"
3. **Agrupamento por Região e Mês**:
   - Soma total de vendas
   - Média das despesas
4. **Combinação de colunas** ("Vendas" e "Despesas")
5. **Geração de sumário estatístico**:
   - Média, Mediana, Desvio Padrão

#### 📈 Implementações Estatísticas
1. **Medidas de Tendência Central**:
   - Média, Mediana e Moda com visualização
   
2. **Medidas de Dispersão**:
   - Amplitude, Variância, Desvio Padrão e IQR
   - Visualização via Boxplot
   
3. **Testes de Normalidade**:
   - Teste Shapiro-Wilk
   - Visualização com Gráfico Q-Q
   
4. **Teste t para Amostras Independentes**:
   - Comparação estatística entre grupos
   - Visualização com gráficos de barras e intervalos de confiança
   
5. **Correlação de Pearson**:
   - Cálculo do coeficiente de correlação
   - Visualização com gráfico de dispersão e linha de regressão
   
6. **Análise de Variância (ANOVA)**:
   - Comparação entre múltiplos grupos
   - Visualização com boxplots e swarmplots

---

## 📊 Exemplos de Visualizações

O projeto gera diversas visualizações estatísticas de alta qualidade (600 DPI):

- `medidas_tendencia_central.png`: Visualização de média, mediana e moda
- `medidas_dispersao.png`: Boxplot ilustrando medidas de dispersão
- `qqplot_normalidade.png`: Gráfico Q-Q para teste de normalidade
- `comparacao_grupos_t.png`: Comparação estatística entre dois grupos
- `correlacao_pearson.png`: Correlação de Pearson com linha de regressão
- `anova_grupos.png`: Comparação múltipla usando ANOVA

---

## 🚀 Como Executar

1. Clone este repositório:
```
git clone https://github.com/seu-usuario/estatistica-datascience.git
```

2. Instale as dependências necessárias:
```
pip install pandas numpy matplotlib seaborn scipy openpyxl
```

3. Execute os scripts:
```
# Para análise estatística
python analise_vendas.py

# Para o notebook do desafio de vendas
jupyter notebook desafio_obrigatorio_vendas.ipynb
```

---

## 📈 Exemplos de Saída (Desafio de Vendas)

```
Soma total de vendas por região e mês:
Região  Mês
Norte   Fev    2000.0
        Jan    1500.0
        Mar    2000.0
Sul     Fev    1800.0
        Jan    2200.0
```

```
Sumário estatístico:
Média das Vendas: 1900.0
Mediana das Vendas: 2000.0
Desvio padrão: 273.86
```

---

## 📚 Referências

- Python Software Foundation – https://www.python.org  
- pandas documentation – https://pandas.pydata.org  
- NumPy – https://numpy.org  
- Matplotlib – https://matplotlib.org
- Seaborn – https://seaborn.pydata.org
- SciPy – https://scipy.org
- openpyxl – https://openpyxl.readthedocs.io

---

## ✅ Status

✔️ Projeto finalizado e pronto para avaliação acadêmica.