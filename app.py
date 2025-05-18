import streamlit as st

st.title("Imersão 360- Taxa Sala")

st.subheader("A seguir, faremos algumas perguntas para definir a Taxa Sala da sua clínica.")


#nome = st.text_input("Digite seu nome")
aluguel = st.number_input("Qual o valor do seu aluguel?")
funcionarios = st.number_input("Qual o gasto total com funcionarios?")
demais = st.number_input("Qual o valor total com demais gastos?")

total_despesas  = aluguel + funcionarios + demais

st.markdown(
    "<h2 style='font-size:48px;'>Total de Despesas: R$ {valor}</h2>".format(
        valor=f"{total_despesas:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    ),
    unsafe_allow_html=True)
