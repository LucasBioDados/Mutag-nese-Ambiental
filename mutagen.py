import streamlit as st

st.title("Cálculo de Composto para Animais")

concentração = st.number_input(
    "Digite a concentração do composto em mg/kg:", step=0.1
)
num_animais = int(
    st.number_input(
        "Digite a quantidade de animais do seu grupo experimental:",
        step=1,
        min_value=1,
        value=1,
    )
)

pesos = []

# Loop usando key única para cada input
for i in range(num_animais):
  valor_peso = st.number_input(
      f"Digite o peso do animal {i+1} em gramas:", step=0.1, key=f"peso_{i}"
  )
  pesos.append(valor_peso)

soma = sum(pesos)
media = soma / num_animais if num_animais > 0 else 0

margem = st.number_input(
    "Digite a porcentagem extra desejada (ex: 10 para 10%): ",
    step=1.0,
    min_value=0.0,
)

# Cálculos
acrescimo = margem / 100
fator = 1 + acrescimo

quantidade_composto = (concentração * media) / 1000  # Quantidade por animal
quantidade_total = quantidade_composto * num_animais  # Quantidade para o grupo
quantidade_final = quantidade_total * fator  # Total com margem de segurança

# Exibição dos resultados na interface do Streamlit
st.divider()
st.subheader("Resultados:")
st.write(
    f"**Quantidade por animal (média):** {quantidade_composto:.2f} mg"
)
st.write(
    f"**Quantidade total para {num_animais} animais:** {quantidade_total:.2f}"
    " mg"
)
st.success(
    f"**Quantidade final com acréscimo de {margem:.0f}%:**"
    f" {quantidade_final:.2f} mg"
)