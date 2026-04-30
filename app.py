import streamlit as st
import random

st.set_page_config(page_title="Trivia Rock Peruano", page_icon="🎸")

st.title("🎸 Trivia: Cantantes del Rock Peruano")

# Banco de preguntas
preguntas = [
    {
        "pregunta": "¿Quién fue el vocalista principal de Soda Stereo (banda influyente en Perú)?",
        "opciones": ["Gustavo Cerati", "Pedro Suárez-Vértiz", "Miki González", "Pelo Madueño"],
        "respuesta": "Gustavo Cerati"
    },
    {
        "pregunta": "¿Quién fue el vocalista de Arena Hash?",
        "opciones": ["Pedro Suárez-Vértiz", "Daniel F", "Raúl Romero", "Libido"],
        "respuesta": "Pedro Suárez-Vértiz"
    },
    {
        "pregunta": "¿Quién es el vocalista de Libido?",
        "opciones": ["Salim Vera", "Wicho García", "Jhovan Tomasevich", "Gian Marco"],
        "respuesta": "Salim Vera"
    },
    {
        "pregunta": "¿Quién fue el vocalista de Mar de Copas?",
        "opciones": ["Wicho García", "Pelo Madueño", "Jean Paul Strauss", "Raúl Romero"],
        "respuesta": "Wicho García"
    },
    {
        "pregunta": "¿Quién es el vocalista de Zen?",
        "opciones": ["Jhovan Tomasevich", "Salim Vera", "Pedro Suárez-Vértiz", "Daniel F"],
        "respuesta": "Jhovan Tomasevich"
    }
]

# Inicializar estado
if "preguntas_mezcladas" not in st.session_state:
    st.session_state.preguntas_mezcladas = random.sample(preguntas, len(preguntas))
    for p in st.session_state.preguntas_mezcladas:
        random.shuffle(p["opciones"])

if "respuestas_usuario" not in st.session_state:
    st.session_state.respuestas_usuario = {}

# Mostrar preguntas
st.subheader("Responde las siguientes preguntas:")

for i, p in enumerate(st.session_state.preguntas_mezcladas):
    respuesta = st.radio(
        f"{i+1}. {p['pregunta']}",
        p["opciones"],
        key=f"pregunta_{i}"
    )
    st.session_state.respuestas_usuario[i] = respuesta

# Botón verificar
if st.button("✅ Verificar respuestas"):
    puntaje = 0

    for i, p in enumerate(st.session_state.preguntas_mezcladas):
        if st.session_state.respuestas_usuario.get(i) == p["respuesta"]:
            puntaje += 1

    st.write(f"🎯 Obtuviste {puntaje} de 5 correctas")

    if puntaje == 5:
        st.balloons()
        st.success("🎉 ¡Perfecto! ¡Eres un experto en rock peruano!")
    else:
        st.warning("Sigue intentando 🎸")

# Botón reiniciar
if st.button("🔄 Nueva trivia"):
    st.session_state.clear()
    st.rerun()
