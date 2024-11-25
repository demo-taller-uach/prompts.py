import streamlit as st
import openai

# Configuración de clave API desde secretos
openai_api_key = st.secrets["api_key"]
openai.api_key = openai_api_key

# Función para interactuar con OpenAI
def asistente1(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=800,
        temperature=0,
    )
    respuesta = response.choices[0].message.content
    return respuesta

# Función para interactuar con OpenAI con instrucciones específicas
def asistente2(instruc, prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an assistant."},
            {"role": "user", "content": instruc + ": " + prompt}
        ],
        max_tokens=800,
        temperature=0,
    )
    respuesta = response.choices[0].message.content
    return respuesta

# Página 2
def page_2():
    st.title("Page 2")
    prompt = st.chat_input("Escribe tu pregunta")
    if prompt:
        with st.chat_message("user"):
            st.markdown(prompt)
        respuesta = asistente1(prompt)
        with st.chat_message("assistant"):
            st.markdown(respuesta)

# Página 3
def page_3():
    st.title("Page 3")
    prompt = st.chat_input("Escribe tu pregunta")
    if prompt:
        with st.chat_message("user"):
            st.markdown(prompt)
        instruc = "Use emojis to improve your answers"
        respuesta = asistente2(instruc, prompt)
        with st.chat_message("assistant"):
            st.markdown(respuesta)

# Navegación de páginas
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Choose a page:", ["Page 2", "Page 3"])

    if page == "Page 2":
        page_2()
    elif page == "Page 3":
        page_3()

if __name__ == "__main__":
    main()
