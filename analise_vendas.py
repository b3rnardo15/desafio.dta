import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import pearsonr, f_oneway
import pandas as pd

# Configuração do estilo dos gráficos
sns.set_style("whitegrid")
plt.style.use('ggplot')

# 1. Medidas de Tendência Central com gráfico - CORREÇÃO AQUI
dados = [5, 7, 8, 8, 10]
media = np.mean(dados)
mediana = np.median(dados)
moda_result = stats.mode(dados)
moda = float(moda_result.mode)  # Convertendo para float simples

print(f"Média: {media}, Mediana: {mediana}, Moda: {moda}")

# Gráfico de pontos com as medidas
plt.figure(figsize=(10, 5))
sns.stripplot(x=dados, jitter=0.05, size=10)
plt.axhline(media, color='r', linestyle='--', label=f'Média: {media:.1f}')
plt.axhline(mediana, color='g', linestyle='-.', label=f'Mediana: {mediana:.1f}')
plt.axhline(moda, color='b', linestyle=':', label=f'Moda: {moda:.0f}')
plt.title('Medidas de Tendência Central')
plt.legend()
plt.savefig('medidas_tendencia_central.png', dpi=600, bbox_inches='tight')
plt.show()

# 2. Medidas de Dispersão com gráfico
amplitude = np.ptp(dados)
variancia = np.var(dados, ddof=1)
desvio_padrao = np.std(dados, ddof=1)
q1 = np.percentile(dados, 25)
q3 = np.percentile(dados, 75)
iqr = q3 - q1

print(f"Amplitude: {amplitude}, Variância: {variancia}, Desvio: {desvio_padrao}, IQR: {iqr}")

# Boxplot mostrando as medidas de dispersão
plt.figure(figsize=(8, 6))
sns.boxplot(x=dados, width=0.3)
plt.title('Boxplot - Medidas de Dispersão')
plt.savefig('medidas_dispersao.png', dpi=600, bbox_inches='tight')
plt.show()

# 3. Teste de Normalidade com gráfico Q-Q
stat, p = stats.shapiro(dados)
print(f"Estatística W: {stat}, p-valor: {p}")

# Gráfico Q-Q para normalidade
plt.figure(figsize=(8, 6))
stats.probplot(dados, plot=plt)
plt.title('Gráfico Q-Q - Teste de Normalidade')
plt.savefig('qqplot_normalidade.png', dpi=600, bbox_inches='tight')
plt.show()

# 4. Teste t com gráfico comparativo
grupoA = [3, 5, 7]
grupoB = [4, 6, 8]
t_stat, p_valor = stats.ttest_ind(grupoA, grupoB)
print(f"t = {t_stat}, p = {p_valor}")

# Gráfico de barras com intervalos de confiança
df_grupos = pd.DataFrame({
    'Grupo': ['A'] * len(grupoA) + ['B'] * len(grupoB),
    'Valores': grupoA + grupoB
})

plt.figure(figsize=(8, 6))
sns.barplot(x='Grupo', y='Valores', data=df_grupos, errorbar=('ci', 95))
plt.title('Comparação entre Grupos (Teste t)')
plt.savefig('comparacao_grupos_t.png', dpi=600, bbox_inches='tight')
plt.show()

# 5. Correlação de Pearson com gráfico de dispersão
x = [1, 2, 3]
y = [2, 4, 6]
r, p = pearsonr(x, y)
print(f"Pearson r: {r}, valor-p:{p:.4f}")

# Gráfico de dispersão com linha de regressão
plt.figure(figsize=(8, 6))
sns.regplot(x=x, y=y)
plt.title(f'Correlação de Pearson (r = {r:.2f})')
plt.savefig('correlacao_pearson.png', dpi=600, bbox_inches='tight')
plt.show()

# 6. ANOVA com gráfico
grupo1 = [3, 5, 7]
grupo2 = [4, 6, 8]
grupo3 = [2, 4, 6]
f_stat, p_valor = f_oneway(grupo1, grupo2, grupo3)
print(f"F = {f_stat}, p = {p_valor}")

# Gráfico de caixas para ANOVA
df_anova = pd.DataFrame({
    'Valores': grupo1 + grupo2 + grupo3,
    'Grupo': ['Grupo1']*3 + ['Grupo2']*3 + ['Grupo3']*3
})

plt.figure(figsize=(10, 6))
sns.boxplot(x='Grupo', y='Valores', data=df_anova)
sns.swarmplot(x='Grupo', y='Valores', data=df_anova, color='black', alpha=0.5)
plt.title('Comparação Múltipla (ANOVA)')
plt.savefig('anova_grupos.png', dpi=600, bbox_inches='tight')
plt.show()

print("Análise concluída com sucesso! Todos os gráficos foram salvos.")
