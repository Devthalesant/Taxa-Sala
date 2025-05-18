import streamlit as st

st.title("Imersão 360 - Taxa Sala")

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

dias_uteis = st.number_input("Quantos dias uteis funciona?")
horas_dia = st.number_input("Quantas horas por dia?")
salas = st.number_input("Quantas salas de procedimento?")

base_calculo = dias_uteis/horas_dia/salas

taxa_sala = total_despesas/base_calculo

st.markdown(
    "<h2 style='font-size:48px;'>Taxa Sala: R$ {valor}</h2>".format(
        valor=f"{taxa_sala:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    ),
    unsafe_allow_html=True)