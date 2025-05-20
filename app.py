import streamlit as st

# Verifica se o estado da página está definido; se não, inicia na página 1
if 'page' not in st.session_state:
    st.session_state['page'] = 1

# Função para avançar a página
def next_page():
    st.session_state['page'] += 1

# Página 1 - Custos Fixos
if st.session_state['page'] == 1:
    st.image("images/Logo-Imersão-horizontal-fundoclaro-png.png",use_container_width=False)
    st.title("Taxa Sala")
    st.header("A seguir, faremos algumas perguntas para definir a Taxa Sala da sua clínica.")
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
    
    if st.button("Salvar Despesas"):
        st.session_state['total_despesas'] = total_despesas
        next_page()

# Página 2 - Informações sobre funcionamento
elif st.session_state['page'] == 2:
    st.image("images/Icone Horizontal.png")
    st.title("Taxa Sala")
    st.header("Informações sobre Funcionamento:")

    total_despesas = st.session_state.get('total_despesas', 0)

    dias_uteis = st.number_input("Quantos dias úteis funciona por mês?", min_value=1, step=1)
    horas_dia = st.number_input("Quantas horas por dia?", min_value=1, step=1)
    salas = st.number_input("Quantas salas de procedimento?", min_value=1, step=1)

    # Calcule quando tiver valores válidos
    if dias_uteis > 0 and horas_dia > 0 and salas > 0:
        taxa_sala = total_despesas / dias_uteis / horas_dia / salas
        st.session_state['taxa_sala'] = taxa_sala

        # Exibir o resultado
        st.markdown(
            "<h2 style='font-size:48px;'>Taxa Sala: R$ {valor}</h2>".format(
                valor=f"{taxa_sala:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
            ),
            unsafe_allow_html=True
        )
    else:
        st.write("Por favor, insira valores válidos para dias úteis, horas por dia e salas.")

    if st.button("Salvar Informações de Funcionamento"):

        st.session_state['dias_uteis'] = dias_uteis
        st.session_state['horas_dia'] = horas_dia
        st.session_state['salas'] = salas
        st.session_state['taxa_sala'] = taxa_sala
        next_page()

elif st.session_state['page'] == 3:
    st.write(f"PáginaAtual: {st.session_state['page']}")
    st.title("Taxa Sala")
    st.header("Outras Informações:")

    procedimnto = st.text_input("Qual o nome do Procedimento?")
    preco_venda = st.number_input("Qual o preço de venda? (R$)", min_value=0.00, step=1.00)
    tempo = st.number_input("Quanto tempo leva fazendo? (em minutos)", min_value=0.00, step=1.00)
    consumivel = st.number_input("Qual o gasto com consumivel? (R$)", min_value=0.00, step=1.00)
    aliquota = st.number_input("Qual a aliquota de imposto? (%)", min_value=0.00, step=0.01) / 100
    cartao = st.number_input("Qual a taxa de cartão de crédito? (%)", min_value=0.00, step=0.00) / 100
    comissao = st.number_input("Qual o comissionamento de venda? (%)", min_value=0.00, step=0.00) / 100
    mod = st.number_input("Qual valor pago ao profissinal pela execucao? (R$)", min_value=0.00, step=1.00)

    if st.button("Salvar Outras Informaçõs e Calcular"):
    
        st.session_state['procedimnto'] = procedimnto
        st.session_state['preco_venda'] = preco_venda
        st.session_state['tempo'] = tempo
        st.session_state['consumivel'] = consumivel
        st.session_state['aliquota'] = aliquota
        st.session_state['cartao'] = cartao
        st.session_state['comissao'] = comissao
        st.session_state['mod'] = mod
        next_page()

elif st.session_state['page'] == 4:
    st.write(f"PáginaAtual: {st.session_state['page']}")

    total_despesas = st.session_state.get('total_despesas', 0)
    procedimnto = st.session_state.get('procedimnto',0)
    preco_venda = st.session_state.get('preco_venda',0)
    tempo = st.session_state.get('tempo',0)
    consumivel = st.session_state.get('consumivel',0)
    aliquota = st.session_state.get('aliquota',0)
    cartao = st.session_state.get('cartao',0)
    comissao = st.session_state.get('comissao',0)
    mod = st.session_state.get('mod',0)
    dias_uteis = st.session_state.get('dias_uteis',0)
    horas_dia = st.session_state.get('horas_dia',0)
    salas = st.session_state.get('salas',0)
    taxa_sala = st.session_state.get('taxa_sala',0)


    st.title("Taxa Sala")
    st.header("KPI´s Taxa Sala:")
    margem_rs = preco_venda-(tempo/60*taxa_sala)-consumivel-(aliquota*preco_venda)-(cartao*preco_venda)-(comissao*preco_venda)-mod
    margem_porcento = (margem_rs/preco_venda)*100
    margem_formatada = f"{margem_porcento:.2f}".replace('.', ',')
    margem_reais_formatada = f"{margem_rs:,.2f}".replace('.', ',')  # coloca vírgula como decimal e separa milhar

    proced_pe = total_despesas/(margem_rs+(tempo/60*taxa_sala))
    format_proced_pe = f"{proced_pe:.0f}"
    fat_pe = proced_pe*preco_venda
    mod_pe = proced_pe*mod
    ocupacao_pe = (proced_pe*tempo)/(60*salas*horas_dia*dias_uteis)*100
    format_ocupacao_pe = f"{ocupacao_pe:.2f}"
    fat_max = (fat_pe/ocupacao_pe)*100
    num_prced_max = fat_max/preco_venda
    lucro_max = (num_prced_max*(margem_rs+((tempo/60)*taxa_sala)))-total_despesas
    fat_hora = preco_venda/(tempo/60)
    mod_hora = mod/(tempo/60)
    lucro_hora= (margem_rs+(tempo/60*taxa_sala))/(tempo/60)

    nomes = ['fat_pe', 'mod_pe', 'fat_max', 'lucro_max', 'fat_hora', 'mod_hora', 'lucro_hora']
    variaveis_para_formatar_rs = [fat_pe,mod_pe,fat_max,lucro_max,fat_hora,mod_hora,lucro_hora]

    variaveis_formatadas = {}

    for nome, valor in zip(nomes, variaveis_para_formatar_rs):
        variavel_formatada = f"{valor:,.2f}".replace('.', 'X').replace(',', '.').replace('X', ',')
        variaveis_formatadas[nome] = variavel_formatada


    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
        "<h3 style='font-size:30px;'>Margem(R$) {}</h3>".format(margem_reais_formatada),
        unsafe_allow_html=True
    )
        st.markdown(
        "<h3 style='font-size:30px;'>Procedimento(PE) {}</h3>".format(format_proced_pe),
        unsafe_allow_html=True
    )
        st.markdown(
        "<h3 style='font-size:30px;'>MOD(PE) R$ {}</h3>".format(variaveis_formatadas["mod_pe"]),
        unsafe_allow_html=True
    )
        st.markdown(
        "<h3 style='font-size:30px;'>FAT(MAX) R$ {}</h3>".format(variaveis_formatadas["fat_max"]),
        unsafe_allow_html=True
    )

    with col2:
        st.markdown(
        "<h3 style='font-size:30px;'>Margem(%) {}</h3>".format(margem_formatada),
        unsafe_allow_html=True
    )
        st.markdown(
        "<h3 style='font-size:30px;'>FAT(PE) R$ {}</h3>".format(variaveis_formatadas["fat_pe"]),
        unsafe_allow_html=True
    )
        st.markdown(
        "<h3 style='font-size:30px;'>Ocupação(PE) % {}</h3>".format(format_ocupacao_pe),
        unsafe_allow_html=True)

        st.markdown(
        "<h3 style='font-size:30px;'>Lucro(Max) R$ {}</h3>".format(variaveis_formatadas["lucro_max"]),
        unsafe_allow_html=True
    )
