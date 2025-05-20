

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