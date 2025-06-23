import streamlit as st
import pandas as pd
import time

# Inicializa estados da sessão
if "battery_level" not in st.session_state:
    st.session_state.battery_level = 100
if "carga_critica" not in st.session_state:
    st.session_state.carga_critica = True
if "carga_secundaria" not in st.session_state:
    st.session_state.carga_secundaria = True
if "consumo_log" not in st.session_state:
    st.session_state.consumo_log = []

def consumir_energia():
    consumo = 0
    if st.session_state.carga_critica:
        consumo += 5
    if st.session_state.carga_secundaria:
        consumo += 3
    st.session_state.battery_level = max(0, st.session_state.battery_level - consumo * 0.1)
    st.session_state.consumo_log.append({
        "Tempo": time.strftime("%H:%M:%S"),
        "Bateria": round(st.session_state.battery_level, 2)
    })

# Título
st.title("CARENERGY - Gerenciador Inteligente de Energia")

st.markdown("### Nível da Bateria")
st.progress(st.session_state.battery_level / 100)

# Controle manual das cargas
col1, col2 = st.columns(2)
with col1:
    st.session_state.carga_critica = st.checkbox("Carga Crítica (ex: Geladeira)", value=st.session_state.carga_critica)
with col2:
    st.session_state.carga_secundaria = st.checkbox("Carga Secundária (ex: TV)", value=st.session_state.carga_secundaria)

# Automação básica
if st.session_state.battery_level < 30:
    st.session_state.carga_secundaria = False
    st.warning("Bateria crítica! Carga secundária desligada automaticamente.")

# Atualização manual
if st.button("Atualizar Consumo"):
    consumir_energia()

# Gráfico de histórico da bateria
if st.session_state.consumo_log:
    df = pd.DataFrame(st.session_state.consumo_log)
    st.line_chart(df.set_index("Tempo"))

# Estado atual
st.markdown(f"**Bateria:** {round(st.session_state.battery_level, 2)}%")
st.markdown(f"**Carga Crítica:** {'Ligada' if st.session_state.carga_critica else 'Desligada'}")
st.markdown(f"**Carga Secundária:** {'Ligada' if st.session_state.carga_secundaria else 'Desligada'}")
