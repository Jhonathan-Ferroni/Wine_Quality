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

## O que ainda falta implementar?

- Melhorar a análise de outliers e verificar se há necessidade de tratamento.
- Aplicar métodos estatísticos mais avançados para confirmar padrões identificados.
- Documentar melhor os códigos e criar um fluxo mais organizado para reprodutibilidade.

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

## Status do Projeto

Este projeto ainda está **em desenvolvimento**, e novas melhorias serão adicionadas conforme avanço na análise. Feedbacks e sugestões são sempre bem-vindos!

---

### 📚 Fonte dos Dados
Os dados foram obtidos do repositório da UCI Machine Learning:  
[Wine Quality Dataset](https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv)

---

Fique à vontade para contribuir com ideias, dúvidas ou melhorias! 🚀

