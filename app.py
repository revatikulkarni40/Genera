import streamlit as st

def main():
    st.title("Genera")
    chat_container = st.container()

    user_input = st.text.input("Type your text here" , key="user_input")

    send_button = st.button("Proceed",key="send button")

    if send_button:
        llm_reponse = "This is a response from Genera"

        with chat_container:
             st.chat_message("user").write(user_input)
             st.chat_message("Genera").write("here is answer")

if __name__ == "_main_":
   main()            