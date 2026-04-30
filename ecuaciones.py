import streamlit as st
import random

st.set_page_config(page_title="Ecuaciones de Primer Grado", page_icon="➗")

st.title("➗ Práctica: Ecuaciones de Primer Grado")

# Función para generar ecuación con solución entre 0 y 10
def generar_ecuacion():
    x = random.randint(0, 10)  # solución

    a = random.randint(1, 10)
    b = random.randint(0, 10)

    # a*x + b = c
    c = a * x + b

    return {
        "ecuacion": f"{a}x + {b} = {c}",
        "respuesta": x
    }

# Inicializar estado
if "ejercicio" not in st.session_state:
    st.session_state.ejercicio = generar_ecuacion()

# Mostrar ecuación
st.subheader("Resuelve la siguiente ecuación:")
st.write(f"### {st.session_state.ejercicio['ecuacion']}")

# Input del usuario
respuesta_usuario = st.number_input(
    "Ingresa el valor de x:",
    min_value=0,
    max_value=10,
    step=1
)

# Botón verificar
if st.button("✅ Verificar"):
    correcta = st.session_state.ejercicio["respuesta"]

    if respuesta_usuario == correcta:
        st.success("🎉 ¡Correcto!")
        st.snow()  # animación de nieve
    else:
        st.error(f"❌ Incorrecto. La respuesta correcta era {correcta}")

# Botón nuevo ejercicio
if st.button("🔄 Nuevo ejercicio"):
    st.session_state.ejercicio = generar_ecuacion()
    st.rerun()
