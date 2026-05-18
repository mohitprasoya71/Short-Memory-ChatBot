import streamlit as st
from backend import chatbot
from langchain_core.messages import HumanMessage, AIMessageChunk
import time
import uuid

# Generate unique thread_id per browser session
if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = str(uuid.uuid4())

CONFIG = {'configurable': {'thread_id': st.session_state['thread_id']}}  # unique per session

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

user_input = st.chat_input('Type here')

if user_input:
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})

    with st.chat_message('user'):
        st.markdown(user_input)

    with st.chat_message('assistant'):
        placeholder = st.empty()
        full_response = ""

        for message_chunk, metadata in chatbot.stream(
            {'messages': [HumanMessage(content=user_input)]},
            config=CONFIG,
            stream_mode='messages'
        ):
            if isinstance(message_chunk, AIMessageChunk):
                content = message_chunk.content

                if isinstance(content, list):
                    for block in content:
                        if isinstance(block, dict) and block.get("type") == "text":
                            text = block.get("text", "")
                            if text:
                                for char in text:
                                    full_response += char
                                    placeholder.markdown(full_response + "▌")
                                    time.sleep(0.01)

                elif isinstance(content, str) and content:
                    for char in content:
                        full_response += char
                        placeholder.markdown(full_response + "▌")
                        time.sleep(0.01)

        placeholder.markdown(full_response)

    st.session_state['message_history'].append({'role': 'assistant', 'content': full_response})