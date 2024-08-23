# Importando as bibliotecas necessárias
import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 

# Carregando a base de dados
dados = pd.read_csv("slr12.csv", sep=";")

# Separando os dados de treinamento e de texte
X = dados[['FrqAnual']]
y = dados['CusInic']

# Criando e treinando o modelo de Regressão Linear
modelo = LinearRegression().fit(X, y)

# Construindo a aplicação com Streamlit
st.title("Previsão Inicial de Custo para Franquia")

# Separando a aplicação em colunas
col1, col2 = st.columns(2)

with col1:
    st.header("Dados")
    st.table(dados.head(10))
    
with col2:
    st.header("Gráfico de Dispersão")
    fig, ax = plt.subplots()
    ax.scatter(X, y, color='blue')
    ax.plot(X, modelo.predict(X), color='red')
    st.pyplot(fig)
    
st.header("Valor Anual da Franquia: ")
novo_valor = st.number_input("Informe Novo Valor", min_value=1.0, max_value=999999.0, value=1500.0, step=0.01)
processar = st.button("Processar")

if processar:
    dados_novo_valor = pd.DataFrame([[novo_valor]], columns=['FrqAnual'])
    prev = modelo.predict(dados_novo_valor)
    st.header(f"A Previsão de Custo Inicial é de R$ {prev[0]:.2f}")
