import streamlit as st

# Verifica se o estado da página está definido; se não, inicia na página 1
st.set_page_config(
    page_title="Taxa Sala ",
    layout="wide",
    initial_sidebar_state="auto"
)

if 'page' not in st.session_state:
    st.session_state['page'] = 1

# Função para avançar a página
def next_page():
    st.session_state['page'] += 1
    st.rerun()

# Página 1 - Custos Fixos
if st.session_state['page'] == 1:
    st.image("images/Logo-Imersão-horizontal-fundoclaro-png.png", use_container_width=True)
    st.markdown('<h1 style="font-size:30px; color:purple; text-decoration:underline;">Taxa Sala</h1>', unsafe_allow_html=True)
    st.markdown('<h3 style="font-size:20px;">A seguir, faremos algumas perguntas para definir a Taxa Sala da sua clínica.</h3>', unsafe_allow_html=True)
    st.markdown('<h2 style="font-size:20px; color:purple; text-decoration:underline;">Despesas Fixas:</h2>', unsafe_allow_html=True)

    # Inputs
    aluguel = st.number_input("Qual o valor do seu aluguel? (R$)", min_value=1, step=1, key='aluguel')
    funcionarios = st.number_input("Qual o gasto total com salário de funcionários? (R$)", min_value=1, step=1, key='funcionarios')
    demais = st.number_input("Qual o valor total com demais Depesas Fixas? (R$)", min_value=1, step=1, key='demais')
    funcionarios = funcionarios * 1.8  # Considerando 80% de encargos sociais

    total_despesas = aluguel + funcionarios + demais

    st.markdown(
        "<h2 style='font-size:30px; color:purple;'>Despesa fixa: R$ {valor}</h2>".format(
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
    st.markdown('<h1 style="font-size:30px;color:purple; text-decoration:underline;">Taxa Sala</h1>', unsafe_allow_html=True)
    st.markdown('<h2 style="font-size:20px;color:purple; text-decoration:underline;">Informações sobre Funcionamento:</h2>', unsafe_allow_html=True)

    total_despesas = st.session_state.get('total_despesas', 0)

    dias_uteis = st.number_input("Quantos dias úteis funciona por mês?", min_value=1, step=1)
    horas_dia = st.number_input("Quantas horas por dia?", min_value=1, step=1)
    salas = st.number_input("Quantas salas de procedimento?", min_value=1, step=1)

    # Calcule quando tiver valores válidos
    if dias_uteis > 0 and horas_dia > 0 and salas > 0:
        taxa_sala = total_despesas / dias_uteis / horas_dia / salas
        Custo_dia = total_despesas / dias_uteis
        custo_hora = Custo_dia / horas_dia
        st.session_state['taxa_sala'] = taxa_sala

        # Exibir o resultado
        st.markdown(
            "<h2 style='font-size:30px; color:purple;'>Custo dia: R$ {valor}</h2>".format(
                valor=f"{Custo_dia:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
            ),
            unsafe_allow_html=True
        )

        st.markdown(
            "<h2 style='font-size:30px; color:purple;'>Custo Hora: R$ {valor}</h2>".format(
                valor=f"{custo_hora:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
            ),
            unsafe_allow_html=True
        )

        st.markdown(
            "<h2 style='font-size:30px; color:purple;'>Taxa Sala: R$ {valor}</h2>".format(
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
    st.image("images/Icone Horizontal.png")

    st.markdown(
    '<h1 style="font-size:30px; color:purple; text-decoration:underline;">Taxa Sala</h1>',unsafe_allow_html=True)
    st.markdown(
            """
            <div style='text-align:center;'>
                <h2 style='color:purple;'>Agora, como fazemos para pagar essa Conta?</h2>
            </div>
            """, unsafe_allow_html=True
     )
    
    st.markdown('<h2 style="font-size:20px;color:purple; text-decoration:underline;">Outras Informações:</h2>', unsafe_allow_html=True)

    procedimnto = st.text_input("Qual o nome do Procedimento?")
    preco_venda = st.number_input("Qual o preço de venda? (R$)", min_value=0.00, step=1.00)
    tempo = st.number_input("Quanto tempo leva fazendo? (em minutos)", min_value=0.00, step=1.00)
    consumivel = st.number_input("Qual o gasto com consumivel? (R$)", min_value=0.00, step=1.00)
    aliquota = st.number_input("Qual a aliquota de imposto? (%)", min_value=0.00, step=0.01) / 100
    cartao = st.number_input("Qual a taxa de cartão de crédito? (%)", min_value=0.00, step=0.00) / 100
    comissao = st.number_input("Qual o comissionamento de venda? (%)", min_value=0.00, step=0.00) / 100
    mod = st.number_input("Qual valor pago ao profissinal pela execução? (R$)", min_value=0.00, step=1.00)

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
    st.image("images/Icone Horizontal.png")

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

    margem_rs = preco_venda-(tempo/60*taxa_sala)-consumivel-(aliquota*preco_venda)-(cartao*preco_venda)-(comissao*preco_venda)-mod
    margem_porcento = (margem_rs/preco_venda)*100
    proced_pe = total_despesas/(margem_rs+(tempo/60*taxa_sala))
    fat_pe = proced_pe*preco_venda
    mod_pe = proced_pe*mod
    ocupacao_pe = (proced_pe*tempo)/(60*salas*horas_dia*dias_uteis)*100
    fat_max = (fat_pe/ocupacao_pe)*100
    num_prced_max = fat_max/preco_venda
    lucro_max = (num_prced_max*(margem_rs+((tempo/60)*taxa_sala)))-total_despesas
    fat_hora = preco_venda/(tempo/60)
    mod_hora = mod/(tempo/60)
    lucro_hora= (margem_rs+(tempo/60*taxa_sala))/(tempo/60)

    margem_porcento = f"{margem_porcento:.2f}".replace('.', ',')
    margem_rs = "R$ " + f"{margem_rs:,.2f}".replace('.', ',')  # coloca vírgula como decimal e separa milhar
    ocupacao_pe = f"{ocupacao_pe:.2f}"
    proced_pe = f"{proced_pe:.0f}".replace('.', ',')
    fat_pe = "R$ " + f"{fat_pe:,.2f}".replace('.', ',')
    mod_pe = "R$ " + f"{mod_pe:,.2f}".replace('.', ',')
    fat_max = "R$ " + f"{fat_max:,.2f}".replace('.', ',')
    num_prced_max = f"{num_prced_max:.0f}".replace('.', ',')
    lucro_max = "R$ " + f"{lucro_max:,.2f}".replace('.', ',')
    fat_hora = "R$ " + f"{fat_hora:,.2f}".replace('.', ',')
    mod_hora = "R$ " + f"{mod_hora:,.2f}".replace('.', ',')
    lucro_hora = "R$ " + f"{lucro_hora:,.2f}".replace('.', ',')




    with st.container():
        # Linha 1 - cabeçalhos

        st.markdown(
            """
            <div style='text-align:center;'>
                <h2 style='color:#673AB7;'>KPIs da Taxa Sala</h2>
            </div>
            """, unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div style='text-align:center;'>
                <h2 style='color:#37474F;'>Procedimento : <strong>{procedimnto}</h2>
            </div>
            """, unsafe_allow_html=True
        )

        # Linha 2 - caixas
        col1, col2, col3, col4 = st.columns(4)

        # Adiciona espaçamento entre todas as colunas em mobile usando CSS customizado
        st.markdown("""
            <style>
            @media (max-width: 768px) {
                .custom-kpi > div {
                margin-bottom: 20px !important;
                }
            }
            </style>
        """, unsafe_allow_html=True)

        # Linha 2 - caixas
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown(
            f"<div class='custom-kpi' style='background-color:#B39DDB; padding:15px; border-radius:10px; text-align:center;'>"
            f"<strong style='font-size:20px; color:#6A1B9A;'>Margem(R$)</strong><br>"
            f"<span style='font-size:24px;'><strong>{margem_rs}</span>"
            f"</div>", unsafe_allow_html=True
            )
        with col2:
            st.markdown(
            f"<div class='custom-kpi' style='background-color:#B39DDB; padding:15px; border-radius:10px; text-align:center;'>"
            f"<strong style='font-size:20px; color:#6A1B9A;'>Margem(%)</strong><br>"
            f"<span style='font-size:24px;'><strong>{margem_porcento}</span>"
            "</div>", unsafe_allow_html=True
            )
        with col3:
            st.markdown(
            f"<div class='custom-kpi' style='background-color:#B39DDB; padding:15px; border-radius:10px; text-align:center;'>"
            f"<strong style='font-size:20px; color:#6A1B9A;'>Quantidade(Pe)</strong><br>"
            f"<span style='font-size:24px;'><strong>{proced_pe}</span>"
            f"</div>", unsafe_allow_html=True
            )
        with col4:
            st.markdown(
            f"<div class='custom-kpi' style='background-color:#B39DDB; padding:15px; border-radius:10px; text-align:center;'>"
            f"<strong style='font-size:20px; color:#6A1B9A;'>Faturamento(Pe)</strong><br>"
            f"<span style='font-size:24px;'><strong>{fat_pe}</span>"
            "</div>", unsafe_allow_html=True
            )

        # Espaçamento entre linhas
        st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

        # Linha 3 - segunda linha de KPIs
        col5, col6, col7, col8 = st.columns(4)
        with col5:
            st.markdown(
            f"<div class='custom-kpi' style='background-color:#B39DDB; padding:15px; border-radius:10px; text-align:center;'>"
            f"<strong style='font-size:20px; color:#6A1B9A;'>Mão de Obra(Pe)</strong><br>"
            f"<span style='font-size:24px;'><strong>{mod_pe}</span>"
            "</div>", unsafe_allow_html=True
            )
        with col6:
            st.markdown(
            f"<div class='custom-kpi' style='background-color:#B39DDB; padding:15px; border-radius:10px; text-align:center;'>"
            f"<strong style='font-size:20px; color:#6A1B9A;'>Ocupação(%)</strong><br>"
            f"<span style='font-size:24px;'><strong>{ocupacao_pe}</span>"
            "</div>", unsafe_allow_html=True
            )
        with col7:
            st.markdown(
            f"<div class='custom-kpi' style='background-color:#B39DDB; padding:15px; border-radius:10px; text-align:center;'>"
            f"<strong style='font-size:20px; color:#6A1B9A;'>Faturamento(Max)</strong><br>"
            f"<span style='font-size:20px;'><strong>{fat_max}</span>"
            "</div>", unsafe_allow_html=True
            )
        with col8:
            st.markdown(
            f"<div class='custom-kpi' style='background-color:#B39DDB; padding:15px; border-radius:10px; text-align:center;'>"
            f"<strong style='font-size:20px; color:#6A1B9A;'>Quantidade(Max)</strong><br>"
            f"<span style='font-size:24px;'><strong>{num_prced_max}</span>"
            "</div>", unsafe_allow_html=True
            )

        # Espaçamento entre linhas
        st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

        col9, col10, col11, col12 = st.columns(4)
        with col9:
            st.markdown(
            f"<div class='custom-kpi' style='background-color:#B39DDB; padding:15px; border-radius:10px; text-align:center;'>"
            f"<strong style='font-size:20px; color:#6A1B9A;'>Lucro(Max)</strong><br>"
            f"<span style='font-size:22px;'><strong>{lucro_max}</span>"
            "</div>", unsafe_allow_html=True
            )
        with col10:
            st.markdown(
            f"<div class='custom-kpi' style='background-color:#B39DDB; padding:15px; border-radius:10px; text-align:center;'>"
            f"<strong style='font-size:20px; color:#6A1B9A;'>Faturamento(Hora)</strong><br>"
            f"<span style='font-size:24px;'><strong>{fat_hora}</span>"
            "</div>", unsafe_allow_html=True
            )
        with col11:
            st.markdown(
            f"<div class='custom-kpi' style='background-color:#B39DDB; padding:15px; border-radius:10px; text-align:center;'>"
            f"<strong style='font-size:20px; color:#6A1B9A;'>Mão de Obra(Hora)</strong><br>"
            f"<span style='font-size:24px;'><strong>{mod_hora}</span>"
            "</div>", unsafe_allow_html=True
            )
        with col12:
            st.markdown(
            f"<div class='custom-kpi' style='background-color:#B39DDB; padding:15px; border-radius:10px; text-align:center;'>"
            f"<strong style='font-size:20px; color:#6A1B9A;'>Lucro(Hora)</strong><br>"
            f"<span style='font-size:24px;'><strong>{lucro_hora}</span>"
            "</div>", unsafe_allow_html=True
            )