import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 

def load_data(file_path):
    return pd.read_csv(file_path, sep=";")

def train_model(data):
    X = data[['FrqAnual']]
    y = data['CusInic']
    model = LinearRegression().fit(X, y)
    return model, X, y

def display_data(data):
    st.header("Base de Dados")
    st.table(data.head(10))

def display_scatter_plot(X, y, model):
    st.header("Gráfico de dispersão")
    fig, ax = plt.subplots()
    ax.scatter(X, y, color='blue')
    ax.plot(X, model.predict(X), color='red')
    st.pyplot(fig)

def predict_cost(model, new_value):
    new_data = pd.DataFrame([[new_value]], columns=['FrqAnual'])
    return model.predict(new_data)[0]

def main():
    st.title("Previsão de custo inicial para franquia")

    data = load_data("slr12.csv")
    model, X, y = train_model(data)

    col1, col2 = st.columns(2)
    with col1:
        display_data(data)
    with col2:
        display_scatter_plot(X, y, model)

    st.header("Valor anual da franquia: ")
    new_value = st.number_input("Insira um novo valor", min_value=1.0, max_value=999999.0, value=1500.0, step=0.01)
    process = st.button("Processar")

    if process:
        prediction = predict_cost(model, new_value)
        st.header(f"A previsão de custo inicial é R$ {prediction:.2f}")

if __name__ == "__main__":
    main()
