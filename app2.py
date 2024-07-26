import streamlit as st
import ollama
from PIL import Image
import time



with st.sidebar:
    

    st.title("💬 Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    

    #client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    #response = ollama.generate(model='mistral', prompt=prompt)
    response1 = ollama.chat(model="gemma:2b", messages=st.session_state.messages)
    #ollama.embeddings
    #print(response)
    msg = response1['message']['content']
    def response_generator():
        msg = response1['message']['content']
    
        for word in msg.split():
            yield word + " "
            time.sleep(0.10)
    # Return Image
    #image = Image.open(io.BytesIO(image_bytes))
    #msg = f'here is your image related to "{prompt}"'
    st.session_state.messages.append({"role": "assistant", "content": msg})
    #st.chat_message("assistant").write(msg)
    with st.chat_message("assistant"):
        msg = st.write(response_generator())
    

    #st.chat_message("assistant").image(image, caption=prompt, use_column_width=True)