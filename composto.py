{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "50b92dec",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "e51478c4",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026-10-05 22:28:51.070 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.071 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.072 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.073 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.073 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.074 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.075 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.075 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.075 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.076 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.077 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.077 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.078 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.079 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.079 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.080 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.081 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.081 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.082 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.082 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.083 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.083 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.084 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.085 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.086 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.086 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.087 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.087 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.088 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.088 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.089 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.089 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.090 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.091 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.092 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.093 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.093 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.094 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.095 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.167 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.168 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-05 22:28:51.168 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import streamlit as st\n",
    "\n",
    "st.title(\"Cálculo de Composto para Animaes\")\n",
    "\n",
    "concentração = st.number_input(\n",
    "    \"Digite a concentração do composto em mg/kg (ou mg por g):\", step=0.1\n",
    ")\n",
    "num_animais = int(\n",
    "    st.number_input(\n",
    "        \"Digite a quantidade de animais do seu grupo experimental:\",\n",
    "        step=1,\n",
    "        min_value=1,\n",
    "        value=1,\n",
    "    )\n",
    ")\n",
    "\n",
    "pesos = []\n",
    "\n",
    "# Loop usando key única para cada input\n",
    "for i in range(num_animais):\n",
    "  valor_peso = st.number_input(\n",
    "      f\"Digite o peso do animal {i+1} em gramas:\", step=0.1, key=f\"peso_{i}\"\n",
    "  )\n",
    "  pesos.append(valor_peso)\n",
    "\n",
    "soma = sum(pesos)\n",
    "media = soma / num_animais if num_animais > 0 else 0\n",
    "\n",
    "margem = st.number_input(\n",
    "    \"Digite a porcentagem extra desejada (ex: 10 para 10%): \",\n",
    "    step=1.0,\n",
    "    min_value=0.0,\n",
    ")\n",
    "\n",
    "# Cálculos\n",
    "acrescimo = margem / 100\n",
    "fator = 1 + acrescimo\n",
    "\n",
    "quantidade_composto = (concentração * media) / 1000  # Quantidade por animal\n",
    "quantidade_total = quantidade_composto * num_animais  # Quantidade para o grupo\n",
    "quantidade_final = quantidade_total * fator  # Total com margem de segurança\n",
    "\n",
    "# Exibição dos resultados na interface do Streamlit\n",
    "st.divider()\n",
    "st.subheader(\"Resultados:\")\n",
    "st.write(\n",
    "    f\"**Quantidade por animal (média):** {quantidade_composto:.2f} mg\"\n",
    ")\n",
    "st.write(\n",
    "    f\"**Quantidade total para {num_animais} animais:** {quantidade_total:.2f}\"\n",
    "    \" mg\"\n",
    ")\n",
    "st.success(\n",
    "    f\"**Quantidade final com acréscimo de {margem:.0f}%:**\"\n",
    "    f\" {quantidade_final:.2f} mg\"\n",
    ")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.15"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
