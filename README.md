# Análise da Qualidade dos Vinhos 🍇🍷

Este projeto tem como objetivo explorar o conjunto de dados de qualidade dos vinhos tintos, analisando suas características químicas e sua relação com a pontuação de qualidade atribuída. A ideia principal é identificar padrões e correlações que possam ajudar a entender quais fatores impactam positivamente ou negativamente a qualidade da bebida.

## Como funciona o projeto?

1. **Coleta de Dados**:
   - Utilizamos o conjunto de dados disponível na UCI Machine Learning Repository, que contém informações sobre diversos vinhos tintos, incluindo suas propriedades químicas e uma nota de qualidade variando de 0 a 10.

2. **Exploração Inicial**:
   - Verificação de estrutura, distribuição dos dados e presença de valores nulos.
   - Geração de histogramas e boxplots para entender melhor a distribuição das variáveis.

3. **Análise Estatística e Visualização**:
   - Criação de heatmaps para visualizar correlações entre as variáveis.
   - Gráficos de dispersão para examinar relações individuais entre os atributos químicos e a qualidade.
   - Agrupamento dos vinhos com base na qualidade para comparação dos atributos.

4. **Descobertas Preliminares**:
   - O teor alcoólico e os sulfatos apresentam correlação positiva com a qualidade.
   - A acidez volátil e a densidade possuem impacto negativo na avaliação do vinho.
   - A maioria dos vinhos analisados apresenta qualidade entre 5 e 6.

## Versão 2.0

- Adição de Análise Estatística: Adicionei uma análise estatística utilizando o teste t de Student para comparar as médias de diferentes grupos de qualidade de vinho, confirmando a influência do teor alcoólico na qualidade.

- Análise de Outliers: Implementei uma análise detalhada de outliers usando o método IQR, identificando as variáveis mais impactadas e comparando as médias com e sem outliers.

- Melhoria na Visualização: Aprimorei a visualização de dados com gráficos de barras e boxplots, facilitando a identificação de padrões e outliers.

- Documentação e Clareza: Adicionei comentários e explicações detalhadas ao longo do código para melhorar a clareza e a documentação.

## Como executar o projeto?

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/wine-quality-analysis.git
   ```
2. Instale as dependências necessárias:
   ```bash
   pip install pandas numpy matplotlib seaborn
   ```
3. Execute o script no ambiente de sua preferência (Google Colab, Jupyter Notebook ou Python puro).


---

### 📚 Fonte dos Dados
Os dados foram obtidos do repositório da UCI Machine Learning:  
[Wine Quality Dataset](https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv)

---

Fique à vontade para contribuir com ideias, dúvidas ou melhorias! 🚀

