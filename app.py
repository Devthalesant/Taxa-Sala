import streamlit as st

# Verifica se o estado da página está definido; se não, inicia na página 1
if 'page' not in st.session_state:
    st.session_state['page'] = 1

# Função para avançar a página
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
    
    if st.button("Salvar Despesas", on_click=next_page):
        pass

        # Armazena na sessão
        st.session_state['total_despesas'] = total_despesas
        st.session_state['aluguel'] = aluguel
        st.session_state['funcionarios'] = funcionarios
        st.session_state['demais'] = demais

# Página 2 - Informações sobre funcionamento
elif st.session_state['page'] == 2:
    st.title("Imersão 360 - Taxa Sala")
    st.header("Informações sobre Funcionamento:")

    # Recupera o valor de despesas
    total_despesas = st.session_state.get('total_despesas', 0)

    dias_uteis = st.number_input("Quantos dias úteis funciona por mês?", min_value=1, step=1)
    horas_dia = st.number_input("Quantas horas por dia?", min_value=1, step=1)
    salas = st.number_input("Quantas salas de procedimento?", min_value=1, step=1)
    
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

    if st.button("Salvar Informações de Funcionamento", on_click=next_page):
        pass
    
        st.session_state['dias_uteis'] = dias_uteis
        st.session_state['horas_dia'] = horas_dia
        st.session_state['salas'] = salas
        st.session_state['taxa_sala'] = taxa_sala

elif st.session_state['page'] == 3:
    st.title("Imersão 360 - Taxa Sala")
    st.header("Outras Informações:")

    procedimnto = st.text_input("Qual o nome do Procedimento?")
    preco_venda = st.number_input("Qual o preço de venda? (R$)", min_value=0.00, step=1.00)
    tempo = st.number_input("Quanto tempo leva fazendo? (em minutos)", min_value=0.00, step=1.00)
    consumivel = st.number_input("Qual o gasto com consumivel? (R$)", min_value=0.00, step=1.00)
    aliquota = st.number_input("Qual a aliquota de imposto? (%)", min_value=0.00, step=0.01) / 100
    cartao = st.number_input("Qual a taxa de cartão de crédito? (%)", min_value=0.00, step=0.00) / 100
    comissao = st.number_input("Qual o comissionamento de venda? (%)", min_value=0.00, step=0.00) / 100
    mod = st.number_input("Qual valor pago ao profissinal pela execucao? (R$)", min_value=0.00, step=1.00)

    if st.button("Salvar Outras Informaçõs e Calcular", on_click=next_page):
        pass
    
        st.session_state['procedimnto'] = procedimnto
        st.session_state['preco_venda'] = preco_venda
        st.session_state['tempo'] = tempo
        st.session_state['consumivel'] = consumivel
        st.session_state['aliquota'] = aliquota
        st.session_state['cartao'] = cartao
        st.session_state['comissao'] = comissao
        st.session_state['mod'] = mod

