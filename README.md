# 📊 Análise de Dados de Vendas – Desafio Obrigatório (Estatística para Data Science)

Este repositório contém a resolução completa do **Desafio Obrigatório** proposto na disciplina de Estatística para Data Science (Curso ADS – 60h), ministrada pelo Prof. Dr. Welton Dionísio.

---

## 👨‍💻 Autor

**Bernardo Simões**  
📅 Data de execução: 17 de abril de 2025

---

## 🧠 Objetivo

Analisar dados hipotéticos de vendas e despesas mensais de uma empresa, tratando valores ausentes e gerando estatísticas descritivas com base em agrupamentos por região e mês.

---

## 🛠️ Tecnologias Utilizadas

- Python 3.12
- pandas
- numpy
- openpyxl

---

## 📂 Conteúdo

### 📁 Arquivos

- `desafio_obrigatorio_vendas.ipynb`: Notebook com todo o código Python, comentários e análises.
- `vendas.xlsx`: Arquivo Excel gerado com os dados originais.

### 🧪 Etapas Realizadas

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

---

## 📈 Exemplos de Saída

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
- openpyxl – https://openpyxl.readthedocs.io

---

## ✅ Status

✔️ Projeto finalizado e pronto para avaliação acadêmica.
