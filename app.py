import streamlit as st
from openai import OpenAI

openai_api_key = st.secrets["api_key"] 
# Create an OpenAI client.
client = OpenAI(api_key=openai_api_key)
def asistente(prompt):
        stream = client.chat.completions.create(
                model="gpt-4o-mini",  
                messages=[
                    {"role": "system", "content": "You are an assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=800,
                temperature=0,
            )
        respuesta = stream.choices[0].message.content
        return respuesta
def page_2():
    st.title("Page 2")
    prompt = st.chat_input("Escribe tu pregunta")
    if prompt==None:
        st.stop()
    with st.chat_message("user"):
        st.markdown(prompt)

pg = st.navigation([st.Page("page_1.py"), st.Page(page_2)])
pg.run()
