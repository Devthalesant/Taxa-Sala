import streamlit as st

st.title("Imersão 360 - Taxa Sala")

import streamlit as st

st.subheader("A seguir, faremos algumas perguntas para definir a Taxa Sala da sua clínica.")

# Inputs
aluguel = st.number_input("Qual o valor do seu aluguel?", min_value=0.0, step=0.01)
funcionarios = st.number_input("Qual o gasto total com funcionarios?", min_value=0.0, step=0.01)
demais = st.number_input("Qual o valor total com demais gastos?", min_value=0.0, step=0.01)

# Cálculo do total de despesas
total_despesas = aluguel + funcionarios + demais

st.markdown(
    "<h2 style='font-size:48px;'>Total de Despesas: R$ {valor}</h2>".format(
        valor=f"{total_despesas:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    ),
    unsafe_allow_html=True
)
st.write("")  # Quebra de linha para separar visualmente

# Demais inputs
dias_uteis = st.number_input("Quantos dias úteis funciona por mês?", min_value=1, step=1)
horas_dia = st.number_input("Quantas horas por dia?", min_value=1, step=1)
salas = st.number_input("Quantas salas de procedimento?", min_value=1, step=1)

# Calculando a base de cálculo
base_calculo = dias_uteis / horas_dia / salas

# Evitar divisão por zero
if base_calculo > 0:
    taxa_sala = total_despesas / base_calculo

    st.markdown(
        "<h2 style='font-size:48px;'>Taxa Sala: R$ {valor}</h2>".format(
            valor=f"{taxa_sala:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
        ),
        unsafe_allow_html=True
    )
else:
    st.write("Por favor, insira valores válidos para dias úteis, horas por dia e salas.")