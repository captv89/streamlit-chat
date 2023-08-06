import streamlit as st
from transformers import pipeline, Conversation

# Hugging Face

# Create a pipeline for the model
chatbot = pipeline("conversational", model="facebook/blenderbot-400M-distill")


# Streamlit
# Create a title for your app
st.title("💬 Chatbot")



# Create a text input box for user input and a button to send the user input to the bot
user_input = st.text_input("User Input: ")


# Create a button to send the user input to the bot and return the bot's response
if st.button("Send"):
    # Send the user input to the bot
    user_conv = Conversation(user_input)
    bot_response = chatbot(user_conv)
    # Capture bot response
    print(bot_response)
    st.write("Bot: ", bot_response.generated_responses[-1])

# Create a button to clear and reset the chat
if st.button("Reset"):
    st.caching.clear_cache()
    st.experimental_rerun()







