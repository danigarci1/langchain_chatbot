import streamlit as st
import base64
from langserve import RemoteRunnable

# Set up the Streamlit app
st.title("Chatbot")
# Get the current prompt from the session state or set a default value
prompt = st.session_state.get("prompt", [{"role": "system", "content": "none"}])

# Display previous chat messages
for message in prompt:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.write(message["content"])

# Get the user's question using Streamlit's chat input
question = st.chat_input("Ask anything")
chat_service_url = "https://127.0.0.1:8000"

# Create a RemoteRunnable instance
chat = RemoteRunnable(chat_service_url,cookies={"user_id": "sample_user"})
if question is not None:
    prompt.append({"role": "user", "content": question})
    
    with st.chat_message("user"):
        st.write(question)
    # Display an empty assistant message while waiting for the response
    with st.chat_message("assistant"):
        botmsg = st.empty()

    # Send the encoded data to the endpoint
    response = chat.invoke(
    {"human_input": question},
    {
        "configurable": {
            "conversation_id": "1234",
        },
    },
    )
    prompt.append({"role": "assistant", "content": response.content})
    st.session_state["prompt"] = prompt


