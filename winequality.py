# -*- coding: utf-8 -*-
"""WineQuality.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1esLamY1OvIlhuzw7g-yFji93hYz9zBC3

#Análise Exploratória de Dados - Qualidade do Vinho Tinto

Este script realiza uma análise exploratória de dados (EDA) sobre um conjunto de dados de vinhos tintos.
O objetivo é explorar as relações entre as características químicas dos vinhos e sua qualidade.

Autor: Jhonathan Ferroni

# Bibliotecas e dados utilizados
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from scipy.stats import ttest_ind

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
df = pd.read_csv(url, sep=';')
#O conjunto de dados contém informações sobre vinhos tintos, incluindo características químicas e uma pontuação de qualidade (de 0 a 10)

"""# Exploração Inicial

<p>Nesta primeira sessão de exploração, podemos verificar todas as colunas do nosso conjunto de dados. Todas elas são compostas por números do tipo float, com exceção a coluna 'quality', que é um número inteiro. Utilizei a função isnull para verificar a ocorrência de células vazias, porém nenhuma foi encontrada, não necessitando de uma limpeza de dados nesse início.</p>
"""

df.head()

df.info()

df.describe()

df.isnull().sum()

"""# Análise Explorátoria
<p>Neste trecho iniciei as exploração das características químicas dos vinhos de fato, e como elas estavam se relacionando com a qualidade deles.</p>

<p>Com um heat map, notei algumas correlações fortes com a coluna 'quality'</p>


Positivas:  
- Alcool 0,48 </p>
- Sulfatos 0,25 </p>
- Ácido cítrico 0,23 </p>

Negativas:
- Acidez volátil - 0,39 </p>
- Dióxido de enxofre total - 0,19</p>
- Densidade - 0,17 </p>

"""

#Histograma para cada coluna
for coluna in df.columns:
    plt.figure(figsize=(8, 4))
    plt.hist(df[coluna].dropna(), bins=30, color='blue', edgecolor='black')
    plt.title(f'Histograma de {coluna}')
    plt.xlabel(coluna)
    plt.ylabel('Frequência')
    plt.show()

# Calcular a matriz de correlação
correlation_matrix = df.corr()

# Criar o heatmap
plt.figure(figsize=(10, 8))  # Ajustar o tamanho do gráfico
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)

# Exibir o gráfico
plt.show()

plt.figure(figsize=(8, 6))
sns.countplot(x='quality', data=df)
plt.title('Distribuição dos Vinhos por Nível de Qualidade')
plt.xlabel('Qualidade')
plt.ylabel('Contagem')
plt.show()
qualidade_contagem = df['quality'].value_counts().sort_index()
print(qualidade_contagem)

#agrupamento de dados

medias_por_qualidade = df.groupby('quality').mean()
print(medias_por_qualidade)

# Relação positiva: Álcool vs Qualidade
plt.figure(figsize=(10, 4))
sns.scatterplot(x=df['quality'], y=df['alcohol'], color='blue')
plt.title('Relação entre Qualidade e Álcool (Positiva)')
plt.xlabel('Qualidade')
plt.ylabel('Álcool')
plt.show()

# Relação positiva: Sulfatos vs Qualidade
plt.figure(figsize=(10, 4))
sns.scatterplot(x=df['quality'], y=df['sulphates'], color='blue')
plt.title('Relação entre Qualidade e Sulfatos (Positiva)')
plt.xlabel('Qualidade')
plt.ylabel('Sulfatos')
plt.show()

# Relação positiva: Ácido Cítrico vs Qualidade
plt.figure(figsize=(10, 4))
sns.scatterplot(x=df['quality'], y=df['citric acid'], color='blue')
plt.title('Relação entre Qualidade e Ácido Cítrico (Positiva)')
plt.xlabel('Qualidade')
plt.ylabel('Ácido Cítrico')
plt.show()

# Relação negativa: Acidez Volátil vs Qualidade
plt.figure(figsize=(10, 4))
sns.scatterplot(x=df['quality'], y=df['volatile acidity'], color='red')
plt.title('Relação entre Qualidade e Acidez Volátil (Negativa)')
plt.xlabel('Qualidade')
plt.ylabel('Acidez Volátil')
plt.show()

# Relação negativa: Dióxido de Enxofre Total vs Qualidade
plt.figure(figsize=(10, 4))
sns.scatterplot(x=df['quality'], y=df['total sulfur dioxide'], color='red')
plt.title('Relação entre Qualidade e Dióxido de Enxofre Total (Negativa)')
plt.xlabel('Qualidade')
plt.ylabel('Dióxido de Enxofre Total')
plt.show()

# Relação negativa: Densidade vs Qualidade
plt.figure(figsize=(10, 4))
sns.scatterplot(x=df['quality'], y=df['density'], color='red')
plt.title('Relação entre Qualidade e Densidade (Negativa)')
plt.xlabel('Qualidade')
plt.ylabel('Densidade')
plt.show()

variaveis_quimicas = ['alcohol', 'citric acid', 'sulphates', 'density', 'volatile acidity', 'total sulfur dioxide']

# Criar um gráfico separado para cada variável
for coluna in variaveis_quimicas:
    plt.figure(figsize=(8, 4))  # Tamanho do gráfico
    sns.lineplot(
        x=medias_por_qualidade.index,
        y=medias_por_qualidade[coluna],
        marker='o',  # Marcadores nos pontos
        color='blue'  # Cor da linha
    )
    plt.title(f'Média de {coluna} por Qualidade')
    plt.xlabel('Qualidade')
    plt.ylabel('Média')
    plt.grid(True)  # Adiciona uma grade para melhorar a visualização
    plt.show()

"""#Vinhos por qualidade
<p>Não notei a necessidade de retirada de outliers, porém, notei que vinhos de qualidade extrema (perfeitos=8 ou péssimos=3) fugiam muito de regra, portanto decidi separa-los dos vinhos medianos (qualidade entre 4 até 7).</p>
"""

vinhos_perfeitos = df[df['quality'] == 8]
vinhos_pessimos = df[df['quality'] == 3]

medias_perfeitos = vinhos_perfeitos.mean()
print("Médias para vinhos de qualidade perfeita = 8:")
print(medias_perfeitos)

medias_pessimos = vinhos_pessimos.mean()
print("Médias para vinhos de qualidade pessima = 3:")
print(medias_pessimos)



# Calcular as médias gerais
medias_gerais = df.mean()
print("\nMédias gerais:")
print(medias_gerais)

# Filtrar vinhos bons (qualidade entre 6 e 7)
vinhos_bons = df[(df['quality'] >= 6) & (df['quality'] <= 7)]

# Filtrar vinhos ruins (qualidade entre 4 e 5)
vinhos_ruins = df[(df['quality'] >= 4) & (df['quality'] <= 5)]

# Calcular as médias das variáveis para vinhos bons
medias_bons = vinhos_bons.mean()
print("Médias para vinhos bons (qualidade entre 6 e 7):")
print(medias_bons)

# Calcular as médias das variáveis para vinhos ruins
medias_ruins = vinhos_ruins.mean()
print("\nMédias para vinhos ruins (qualidade entre 4 e 5):")
print(medias_ruins)

"""#Enxofre
<p>Neste gráfico podemos descobrir aonde os vinhos de extrema qualidade se diferenciam dos medianos.</p>
<p>Enquanto na maioria das características vimos uma espécie de "escada", em 'total sulfur dioxide' e 'free sulfur dioxide' vimos que as maiores doses de enxofre estão relacionadas com vinhos medianos, portanto, evitando que um vinho seja péssimo mas também não permitindo que ele seja perfeito.</p>
"""

# Selecionar as variáveis de interesse (excluindo 'quality')
variaveis = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides',
             'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']

# Preparar os dados para o gráfico de barras
categorias = variaveis
x = np.arange(len(categorias))  # Posições no eixo x
largura = 0.2  # Largura das barras

# Criar o gráfico de barras
plt.figure(figsize=(14, 8))

# Barras para cada grupo
plt.bar(x - 1.5*largura, medias_perfeitos[variaveis], width=largura, label='Perfeitos (8)', color='gold')
plt.bar(x - 0.5*largura, medias_bons[variaveis], width=largura, label='Bons (6-7)', color='green')
plt.bar(x + 0.5*largura, medias_ruins[variaveis], width=largura, label='Ruins (4-5)', color='orange')
plt.bar(x + 1.5*largura, medias_pessimos[variaveis], width=largura, label='Péssimos (3)', color='red')

# Ajustar o gráfico
plt.xlabel('Variáveis')
plt.ylabel('Média')
plt.title('Comparação das Médias das Variáveis por Grupo de Qualidade')
plt.xticks(x, categorias, rotation=45, ha='right')  # Rotacionar rótulos do eixo x
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()  # Ajustar layout para evitar cortes
plt.show()

"""#Análise Estatística

<p>O t-statistic comprova a análise anterior de que o teor alcoólico influencia fortemente na qualidade do vinho. </p>

O que isso quer dizer?:

- O t = 18,81 indica que as médias dos grupos são muito diferentes.</p>
- O p-value igual ou próximo zero significa que a probabilidade dessa diferença ocorrer por acaso é praticamente inexistente.</p>
- Ou seja, os vinhos bons e ruins têm teores alcoólicos significativamente diferentes.</p>
"""

# Comparando álcool entre vinhos bons e ruins
t_stat, p_value = ttest_ind(vinhos_bons['alcohol'], vinhos_ruins['alcohol'])
print(f"Teste t para Álcool (Bons vs Ruins): t-statistic = {t_stat:.2f}, p-value = {p_value:.4f}")

#outros exemplos


t_stat, p_value = ttest_ind(vinhos_perfeitos['alcohol'], vinhos_pessimos['alcohol'])
print(f"Teste t para Álcool (perfeitos vs pessimos): t-statistic = {t_stat:.2f}, p-value = {p_value:.4f}")


t_stat, p_value = ttest_ind(vinhos_perfeitos['alcohol'], vinhos_bons['alcohol'])
print(f"Teste t para Álcool (Perfeitos vs bons): t-statistic = {t_stat:.2f}, p-value = {p_value:.4f}")


t_stat, p_value = ttest_ind(vinhos_bons['alcohol'], vinhos_pessimos['alcohol'])
print(f"Teste t para Álcool (Bons vs pessimos): t-statistic = {t_stat:.2f}, p-value = {p_value:.4f}")

"""#Outliers
<p>Explorar outliers é uma etapa importante na análise de dados, pois eles podem distorcer os resultados e afetar a performance de modelos preditivos. Vamos explorar os outliers no conjunto de dados de qualidade do vinho, focando nas variáveis que parecem ter uma relação não linear com a qualidade, como 'total sulfur dioxide' e 'free sulfur dioxide'.</p>

<p> As colunas mais impactadas com os outliers são 'residual sugar', 'chlorides' e 'total sulfur dioxide', chegando a variações de 10 a 20% em suas médias. Entretanto, analisando os dados é possível notar que essas características são comuns aos vinhos, não indicando serem erros de medição.</p>


"""

# Selecionar as variáveis de interesse
variaveis_foco = ['total sulfur dioxide', 'free sulfur dioxide', 'sulphates', 'fixed acidity',	'volatile acidity',
                  'citric acid',	'residual sugar'	,'chlorides',	'density',	'pH',	'alcohol',	'quality']


# Boxplots para visualizar outliers
plt.figure(figsize=(20, 10))  # Tamanho da figura
for i, coluna in enumerate(variaveis_foco):
    plt.subplot(2,12, i+1)  # Criar subplots (1 linha, 3 colunas)
    sns.boxplot(y=df[coluna])  # Boxplot para cada variável
    plt.title(coluna)  # Título do gráfico
plt.tight_layout()  # Ajustar layout para evitar sobreposição
plt.show()  # Mostrar os gráficos

# Função para detectar outliers usando IQR
def detectar_outliers(coluna):
    Q1 = coluna.quantile(0.25)  # Primeiro quartil (25%)
    Q3 = coluna.quantile(0.75)  # Terceiro quartil (75%)
    IQR = Q3 - Q1  # Intervalo Interquartil
    limite_inferior = Q1 - 1.5 * IQR  # Limite inferior
    limite_superior = Q3 + 1.5 * IQR  # Limite superior
    outliers = coluna[(coluna < limite_inferior) | (coluna > limite_superior)]  # Valores fora dos limites
    return outliers

# Detectar outliers para as variáveis de foco
outliers_dict = {}
for coluna in variaveis_foco:
    outliers = detectar_outliers(df[coluna])
    outliers_dict[coluna] = outliers
    print(f"Outliers em {coluna}: {len(outliers)}")

  # Calcular as médias sem outliers
medias_sem_outliers = df[variaveis_foco].apply(lambda x: x[~x.isin(outliers_dict[x.name])]).mean()

# Exibir as médias originais e sem outliers
print("\nMédias originais:")
print(df[variaveis_foco].mean())

print("\nMédias sem outliers:")
print(medias_sem_outliers)

# Comparação visual das médias
comparacao_medias = pd.DataFrame({'Original': df[variaveis_foco].mean(), 'Sem Outliers': medias_sem_outliers})
comparacao_medias.plot(kind='bar', figsize=(10, 5))
plt.title('Comparação das Médias com e sem Outliers')
plt.ylabel('Média')
plt.show()