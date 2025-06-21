
import streamlit as st

def calcular_clasificacion(dg_benfica_actual, gf_benfica_actual, goles_bayern, goles_benfica, goles_boca):
    # Calculamos la nueva diferencia de gol de Benfica
    dg_benfica_nuevo = dg_benfica_actual - (goles_bayern - goles_benfica)
    gf_benfica_nuevo = gf_benfica_actual + goles_benfica

    # Boca parte de -1 y 3 goles a favor
    dg_boca_nuevo = -1 + goles_boca
    gf_boca_nuevo = 3 + goles_boca

    # Evaluamos clasificación
    if dg_boca_nuevo > dg_benfica_nuevo:
        resultado = "Boca clasifica como 2º del grupo."
    elif dg_boca_nuevo == dg_benfica_nuevo:
        if gf_boca_nuevo > gf_benfica_nuevo:
            resultado = "Boca clasifica por mayor cantidad de goles a favor."
        elif gf_boca_nuevo == gf_benfica_nuevo:
            resultado = "Empate total. Se define por fair play o sorteo."
        else:
            resultado = "Boca queda eliminado por menor cantidad de goles a favor."
    else:
        resultado = "Boca queda eliminado por peor diferencia de gol."

    return dg_benfica_nuevo, gf_benfica_nuevo, dg_boca_nuevo, gf_boca_nuevo, resultado

# Interfaz Streamlit
st.title("Simulador de clasificación de Boca - Mundial de Clubes 2025")

st.markdown("""
Ajustá los resultados de los partidos para ver si Boca puede clasificar como segundo del grupo.
""")

goles_bayern = st.number_input("Goles de Bayern a Benfica", min_value=0, max_value=10, value=3)
goles_benfica = st.number_input("Goles de Benfica a Bayern", min_value=0, max_value=10, value=0)
goles_boca = st.number_input("Goles de Boca a Auckland City", min_value=0, max_value=15, value=5)

if st.button("Calcular clasificación"):
    dg_benfica, gf_benfica, dg_boca, gf_boca, resultado = calcular_clasificacion(
        dg_benfica_actual=6,
        gf_benfica_actual=8,
        goles_bayern=goles_bayern,
        goles_benfica=goles_benfica,
        goles_boca=goles_boca
    )

    st.subheader("Resultado")
    st.write(f"Diferencia de gol Benfica: {dg_benfica}")
    st.write(f"Goles a favor Benfica: {gf_benfica}")
    st.write(f"Diferencia de gol Boca: {dg_boca}")
    st.write(f"Goles a favor Boca: {gf_boca}")
    st.success(resultado)
