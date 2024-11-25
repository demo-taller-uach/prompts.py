import streamlit as st
from openai import OpenAI

openai_api_key = st.secrets["api_key"] 
# Create an OpenAI client.
client = OpenAI(api_key=openai_api_key)


temp = st.sidebar.select_slider(
    "Temperatura",
    options=[
    0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0
    ],
)

def asistente1(prompt,temp=0):
        stream = client.chat.completions.create(
                model="gpt-4o-mini",  
                messages=[
                    {"role": "system", "content": "You are an assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=800,
                temperature=temp,
            )
        respuesta = stream.choices[0].message.content
        return respuesta

def asistente2(instruc,prompt,temp):
        stream = client.chat.completions.create(
                model="gpt-4o-mini",  
                messages=[
                    {"role": "system", "content": "You are an assistant."},
                    {"role": "user", "content": instruc + ": " + prompt}
                ],
                max_tokens=800,
                temperature=temp,
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
    respuesta = asistente1(prompt)
    with st.chat_message("assistant"):
        st.write(respuesta)

def page_3():
    st.title("Page 3")
    instruc = st.sidebar.text_area("Instrucciones del sistema")
    prompt = st.chat_input("Escribe tu pregunta")
    if prompt==None:
        st.stop()
    with st.chat_message("user"):
        st.markdown(prompt)
    
    respuesta = asistente2(instruc,prompt)
    with st.chat_message("assistant"):
        st.write(respuesta)
pg = st.navigation([st.Page("page_1.py"), st.Page(page_2), st.Page(page_3)])
pg.run()
