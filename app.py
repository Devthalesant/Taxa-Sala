import streamlit as st

# Verifica se o estado da página está definido; se não, inicia na página 1
if 'page' not in st.session_state:
    st.session_state['page'] = 1

# Função para mudar para a próxima página
def next_page():
    st.session_state['page'] += 1

# Página 1 - Custos Fixos
if st.session_state['page'] == 1:
    st.title("Imersão 360 - Taxa Sala")
    st.subheader("A seguir, faremos algumas perguntas para definir a Taxa Sala da sua clínica.")
    st.header("Custos Fixos:")

    # Inputs
    aluguel = st.number_input("Qual o valor do seu aluguel? (R$)", min_value=1, step=1, key='aluguel')
    funcionarios = st.number_input("Qual o gasto total com funcionarios? (R$)", min_value=1, step=1, key='funcionarios')
    demais = st.number_input("Qual o valor total com demais gastos? (R$)", min_value=1, step=1, key='demais')

    total_despesas = aluguel + funcionarios + demais

    st.markdown(
        "<h2 style='font-size:48px;'>Total de Despesas: R$ {valor}</h2>".format(
            valor=f"{total_despesas:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
        ),
        unsafe_allow_html=True
    )
    
    # Botão para avançar para a próxima sessão
    if st.button("Próxima seção", on_click=next_page):
        pass

# Página 2 - Informações sobre funcionamento
elif st.session_state['page'] == 2:
    st.title("Imersão 360 - Taxa Sala")
    st.header("Informações sobre Funcionamento:")

    # Para manter o valor de total_despesas acessível aqui, você pode aproveitar o session_state
    # Porém, como ele foi calculado na página 1, é importante armazená-lo também no session_state
    # Então aqui, vamos usar `st.session_state` para garantir persistência
    total_despesas = st.session_state.get('total_despesas', 0)
    
    dias_uteis = st.number_input("Quantos dias úteis funciona por mês?", min_value=0, step=1)
    horas_dia = st.number_input("Quantas horas por dia?", min_value=0, step=1)
    salas = st.number_input("Quantas salas de procedimento?", min_value=0, step=1)
    
    # Evitar divisão por zero
    if dias_uteis > 0 and horas_dia > 0 and salas > 0:
        taxa_sala = total_despesas / dias_uteis / horas_dia / salas
        st.markdown(
            "<h2 style='font-size:48px;'>Taxa Sala: R$ {valor}</h2>".format(
                valor=f"{taxa_sala:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
            ),
            unsafe_allow_html=True
        )
    else:
        st.write("Por favor, insira valores válidos para dias úteis, horas por dia e salas.")


    
