import streamlit as st
from openai import OpenAI

openai_api_key = st.secrets["api_key"] 
# Create an OpenAI client.
client = OpenAI(api_key=openai_api_key)

modelo = st.sidebar.selectbox(
    "Modelo",
    ("gpt-3.5-turbo","gpt-4o-mini"),
)
temp = st.sidebar.select_slider(
    "Temperatura",
    options=[
    0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0
    ],
)


def asistente1(prompt,temp,modelo):
        stream = client.chat.completions.create(
                model=modelo,  
                messages=[
                    {"role": "system", "content": "You are an assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500,
                temperature=temp,
            )
        respuesta = stream.choices[0].message.content
        
        return respuesta

def asistente2(instruc,prompt,temp,modelo):
        stream = client.chat.completions.create(
                model=modelo,#"gpt-4o-mini",  
                messages=[
                    {"role": "system", "content": "You are an assistant."},
                    {"role": "user", "content": instruc + ": " + prompt}
                ],
                max_tokens=500,
                temperature=temp,
            )
        respuesta = stream.choices[0].message.content
        return respuesta
    
def asistente3(instruc,prompt,temp,modelo):
        stream = client.chat.completions.create(
                model=modelo,#"gpt-4o-mini",  
                messages=[
                    {"role": "system", "content": "You are an assistant."},
                    {"role": "user", "content": instruc + ": " + prompt}
                ],
                max_tokens=500,
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
    respuesta = asistente1(prompt,temp,modelo)
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
    
    respuesta = asistente2(instruc,prompt,temp,modelo)
    with st.chat_message("assistant"):
        st.write(respuesta)

def page_4():
    st.title("Page 4")
    instruc = "Para la instruccion que se pide genera el codigo para que la respuesta se despliegue en streamlit. Debe ser unicamente codigo ya que se ejecuutara. Evita dar cualquier mensaje adicional, solo codigo! Evita usar ```python"#st.sidebar.text_area("Instrucciones del sistema")
    prompt = st.chat_input("Escribe tu pregunta")
    if prompt==None:
        st.stop()
    with st.chat_message("user"):
        st.markdown(prompt)
    
    respuesta = asistente3(instruc,prompt,temp,modelo)
    with st.chat_message("assistant"):
        st.write(respuesta)
        
        exec(respuesta)
        #except:
         #   st.write("no")
         #   pass
pg = st.navigation([st.Page("page_1.py"), st.Page(page_2), st.Page(page_3),st.Page(page_4)])
pg.run()
