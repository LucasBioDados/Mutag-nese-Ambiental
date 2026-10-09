import streamlit as st
import pandas as pd

st.title("Cálculo de Composto para Animais")

# Entradas principais
concentracao = st.number_input(
    "Digite a concentração do composto em mg/kg:",
    min_value=0.0,
    step=0.1,
    value=0.0,
)

num_animais = st.number_input(
    "Digite a quantidade de animais do seu grupo experimental:",
    min_value=1,
    step=1,
    value=1,
)
margem = st.number_input(
    "Digite a porcentagem extra desejada (ex: 10 para 10%):",
    min_value=0.0,
    step=1.0,
    value=10.0,
)

# Entrada do peso de cada animal
pesos = []
st.subheader("Peso dos Animais (em gramas)")
for i in range(int(num_animais)):
    valor_peso = st.number_input(
        f"Digite o peso do animal {i+1} (g):",
        min_value=0.0,
        step=0.1,
        key=f"peso_{i}",
    )
    pesos.append(valor_peso)



# Cálculos
soma = sum(pesos)
media = soma / num_animais if num_animais > 0 else 0

acrescimo = margem / 100
fator = 1 + acrescimo

quantidade_composto = (concentracao * media) / 1000  # mg por animal
quantidade_total = quantidade_composto * num_animais  # mg para o grupo
quantidade_final = quantidade_total * fator  # mg com margem de segurança

# Proteção contra divisão por zero para cálculo da solução
if quantidade_composto > 0:
    concentracao_solucao = quantidade_composto / 0.2
    volume_final = quantidade_final / concentracao_solucao
else:
    volume_final = 0.0

# Exibição dos resultados
st.divider()
st.subheader("Resultados:")

st.write(f"**Quantidade por animal (média):** {quantidade_composto:.2f} mg")
st.write(f"**Quantidade total para {int(num_animais)} animais:** {quantidade_total:.2f} mg")
st.write(f"**Quantidade final com acréscimo de {margem:.0f}%:** {quantidade_final:.2f} mg")
st.success(f"**Volume final necessário para diluição:** {volume_final:.2f} mL")

# --- RECURSO DE REGISTRO E VALIDAÇÃO DE DADOS ---
st.divider()
st.subheader(" Registro de Conferência")

if st.button("Gerar Relatório de Dados Inseridos"):
    # Montagem do resumo de dados
    dados_gerais = {
        "Parâmetro": [
            "Concentração do Composto (mg/kg)",
            "Nº de Animais no Grupo",
            "Média dos Pesos (g)",
            "Margem Extra (%)",
            "Dose por Animal (mg)",
            "Volume Final Diluição (mL)",
        ],
        "Valor Inserido / Calculado": [
            f"{concentracao:.2f}",
            f"{int(num_animais)}",
            f"{media:.2f}",
            f"{margem:.0f}%",
            f"{quantidade_composto:.2f}",
            f"{volume_final:.2f}",
        ],
    }

    # Tabela com o peso individual de cada animal
    df_pesos = pd.DataFrame(
        {"Animal ID": [f"Animal {i+1}" for i in range(len(pesos))], "Peso (g)": pesos}
    )

    st.markdown("### 1. Parâmetros Configurados")
    st.table(pd.DataFrame(dados_gerais))

    st.markdown("### 2. Pesos Individuais Registrados")
    st.dataframe(df_pesos, use_container_width=True)

    # Criação de um arquivo CSV para download (para ata de laboratório/auditoria)
    csv_geral = df_pesos.to_csv(index=False).encode("utf-8")
    st.download_button(
        label=" Baixar Relatório de Pesos em CSV",
        data=csv_geral,
        file_name="registro_pesos_experimento.csv",
        mime="text/csv",
    )
