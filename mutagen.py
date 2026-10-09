import pandas as pd
import streamlit as st

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

margem = st.number_input(
    "Digite a porcentagem extra desejada (ex: 10 para 10%):",
    min_value=0.0,
    step=1.0,
    value=10.0,
)

# Cálculos
soma = sum(pesos)
media = soma / num_animais if num_animais > 0 else 0

acrescimo = margem / 100
fator = 1 + acrescimo

quantidade_composto = (concentracao * media) / 1000  # mg por animal
quantidade_total = quantidade_composto * num_animais  # mg para o grupo
quantidade_final = quantidade_total * fator  # mg com margem de segurança

if quantidade_composto > 0:
    concentracao_solucao = quantidade_composto / 0.2
    volume_final = quantidade_final / concentracao_solucao
else:
    volume_final = 0.0

# Exibição dos resultados na tela
st.divider()
st.subheader("Resultados:")

st.write(f"**Quantidade por animal (média):** {quantidade_composto:.2f} mg")
st.write(
    f"**Quantidade total para {int(num_animais)} animais:** {quantidade_total:.2f} mg"
)
st.swrite(
    f"**Quantidade final com acréscimo de {margem:.0f}%:** {quantidade_final:.2f} mg"
)
st.suces(
    f"**Volume final necessário para diluição:** {volume_final:.2f} mL"
)

# --- REGISTRO E VALIDAÇÃO DE DADOS ---
st.divider()
st.subheader("Registro de Conferência")

if st.button("Gerar Relatório de Dados Inseridos"):
    # 1. Resumo na tela do Streamlit
    dados_gerais = {
        "Parâmetro": [
            "Concentração do Composto (mg/kg)",
            "Nº de Animais no Grupo",
            "Média dos Pesos (g)",
            "Margem Extra (%)",
            "Dose por Animal (mg)",
            "Quantidade Total para o Grupo (mg)",
            "Quantidade Final com Margem (mg)",
            "Volume Final para Diluição (mL)",
        ],
        "Valor": [
            f"{concentracao:.2f}",
            f"{int(num_animais)}",
            f"{media:.2f}",
            f"{margem:.0f}%",
            f"{quantidade_composto:.2f}",
            f"{quantidade_total:.2f}",
            f"{quantidade_final:.2f}",
            f"{volume_final:.2f}",
        ],
    }

    df_pesos = pd.DataFrame(
        {
            "Animal ID": [f"Animal {i+1}" for i in range(len(pesos))],
            "Peso (g)": pesos,
        }
    )

    st.markdown("### 1. Parâmetros Configurados")
    st.table(pd.DataFrame(dados_gerais))

    st.markdown("### 2. Pesos Individuais Registrados")
    st.dataframe(df_pesos, use_container_width=True)

    # 2. Montagem do CSV completo com separador ';'
    # substituido o ponto '.' por vírgula ',' para ser 100% compatível com o Excel em português
    linhas_csv = [
        "PARAMETROS E CONFIGURACOES DO EXPERIMENTO;",
        f"Concentração do Composto (mg/kg);{concentracao:.2f}".replace(".", ","),
        f"Quantidade de Animais;{int(num_animais)}",
        f"Média dos Pesos (g);{media:.2f}".replace(".", ","),
        f"Margem Extra (%);{margem:.0f}%",
        f"Dose por Animal (mg);{quantidade_composto:.2f}".replace(".", ","),
        f"Quantidade Total do Grupo (mg);{quantidade_total:.2f}".replace(
            ".", ","
        ),
        f"Quantidade Final com Margem (mg);{quantidade_final:.2f}".replace(
            ".", ","
        ),
        f"Volume Final para Diluição (mL);{volume_final:.2f}".replace(".", ","),
        ";",
        "--- PESOS INDIVIDUAIS DOS ANIMAIS ---;",
        "Animal ID;Peso (g)",
    ]

    for i, peso in enumerate(pesos):
        peso_str = f"{peso:.2f}".replace(".", ",")
        linhas_csv.append(f"Animal {i+1};{peso_str}")

    conteudo_csv = "\n".join(linhas_csv)

    # Botão para baixar o arquivo CSV completo
    st.download_button(
        label=" Baixar Relatório Completo em CSV",
        data=conteudo_csv.encode("utf-8-sig"),
        file_name="registro_completo_experimento.csv",
        mime="text/csv",
    )
