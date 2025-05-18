import streamlit as st

st.title("Imersão 360 Estética - Taxa Sala")

st.subheader("A seguir, faremos algumas perguntas para definir a Taxa Sala da sua clínica.")


nome = st.text_input("Digite seu nome")
idade = st.number_input("Digite sua idade", min_value=0, max_value=120, step=1)

st.write(f"Nome : {nome}")
