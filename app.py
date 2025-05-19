import streamlit as st

st.title("Imersão 360 - Taxa Sala")

st.subheader("A seguir, faremos algumas perguntas para definir a Taxa Sala da sua clínica.")

st.header("Custos Fixos:")

# Inputs
aluguel = st.number_input("Qual o valor do seu aluguel? (R$)", min_value=0.0, step=0.01)
funcionarios = st.number_input("Qual o gasto total com funcionarios? (R$)", min_value=0.0, step=0.01)
demais = st.number_input("Qual o valor total com demais gastos? (R$)", min_value=0.0, step=0.01)

# Cálculo do total de despesas
total_despesas = aluguel + funcionarios + demais

st.markdown(
    "<h2 style='font-size:48px;'>Total de Despesas: R$ {valor}</h2>".format(
        valor=f"{total_despesas:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    ),
    unsafe_allow_html=True
)
st.write("")  # Quebra de linha para separar visualmente

st.header("Informações sobre Funcionamento:")
# Demais inputs
dias_uteis = st.number_input("Quantos dias úteis funciona por mês?", min_value=1, step=1)
horas_dia = st.number_input("Quantas horas por dia?", min_value=1, step=1)
salas = st.number_input("Quantas salas de procedimento?", min_value=1, step=1)


# Evitar divisão por zero
if dias_uteis > 0:
    taxa_sala = total_despesas /dias_uteis/horas_dia/salas

    st.markdown(
        "<h2 style='font-size:48px;'>Taxa Sala: R$ {valor}</h2>".format(
            valor=f"{taxa_sala:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
        ),
        unsafe_allow_html=True
    )
else:
    st.write("Por favor, insira valores válidos para dias úteis, horas por dia e salas.")

st.header("Procedimento:")

procedimnto = st.text_input("Qual o nome do Procedimento?")
preco_venda = st.number_input("Qual o preço de venda? (R$)", min_value=1, step=1)
tempo = st.number_input("Quanto tempo leva fazendo? (em minutos)", min_value=1, step=1)
consumivel = st.number_input("Qual o gasto com consumivel? (R$)", min_value=1, step=1)
aliquota = st.number_input("Qual a aliquota de imposto? (%)", min_value=0.01, step=0.01) / 100
cartao = st.number_input("Qual a taxa de cartão de crédito? (%)", min_value=0.01, step=0.01) / 100
comissao = st.number_input("Qual o comissionamento de venda? (%)", min_value=0.01, step=0.01) / 100
mod = st.number_input("Qual valor pago ao profissinal pela execucao? (R$)", min_value=1, step=1)

margem_rs = preco_venda-(tempo/60*taxa_sala)-consumivel-(aliquota*preco_venda)-(cartao*preco_venda)-(comissao*preco_venda)-mod
margem_porcento = (margem_rs/preco_venda)*100
margem_formatada = f"{margem_porcento:.2f}".replace('.', ',')
margem_reais_formatada = f"{margem_rs:,.2f}".replace('.', ',')  # coloca vírgula como decimal e separa milhar

proced_pe = total_despesas/(margem_rs+(tempo/60*taxa_sala))
format_proced_pe = f"{proced_pe:.2f}"
fat_pe = proced_pe*preco_venda
mod_pe = proced_pe*mod
ocupacao_pe = (proced_pe*tempo)/(60*salas*horas_dia*dias_uteis)*100
format_ocupacao_pe = f"{ocupacao_pe:.2f}"
fat_max = fat_pe/ocupacao_pe
num_prced_max = fat_max/preco_venda
lucro_max = (num_prced_max*(margem_rs+(tempo/60*taxa_sala)))-total_despesas
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
    "<h3 style='font-size:30px;'>Margem (R$) {}</h3>".format(margem_reais_formatada),
    unsafe_allow_html=True
)
    st.markdown(
    "<h3 style='font-size:30px;'>Procedimento (PE) {}</h3>".format(format_proced_pe),
    unsafe_allow_html=True
)
    st.markdown(
    "<h3 style='font-size:30px;'>MOD (PE) R$ {}</h3>".format(variaveis_formatadas["mod_pe"]),
    unsafe_allow_html=True
)
with col2:
    st.markdown(
    "<h3 style='font-size:30px;'>Margem (%) {}</h3>".format(margem_formatada),
    unsafe_allow_html=True
)
    st.markdown(
    "<h3 style='font-size:30px;'>Faturamento (PE) R$ {}</h3>".format(variaveis_formatadas["fat_pe"]),
    unsafe_allow_html=True
)
    st.markdown(
    "<h3 style='font-size:30px;'>Ocupação (PE) % {}</h3>".format(format_ocupacao_pe),
    unsafe_allow_html=True)