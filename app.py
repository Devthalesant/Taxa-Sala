import streamlit as st

st.title("Imersão 360 Estética - Taxa Sala")

st.subheader("A seguir, faremos algumas perguntas para definir a Taxa Sala da sua clínica.")


#nome = st.text_input("Digite seu nome")
aluguel = st.number_input("Qual o valor do seu aluguel?")
funcionarios = st.number_input("Qual o gasto total com funcionarios?")
demais = st.number_input("Qual o valor total com demais gastos?")

total_despesas  = aluguel + funcionarios + demais

st.write(f"Total de Despeas: R$ {total_despesas:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))

