import streamlit as st
import google.generativeai as genai

# Setup the Brain
genai.configure(api_key="PASTE_YOUR_GOOGLE_KEY_HERE")
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("Family Memory AI")

# Upload Photo
photo = st.file_uploader("Upload a photo of your loved one")
if photo:
    st.image(photo, width=200)

# The Conversation
user_input = st.chat_input("Talk to them...")
if user_input:
    # This sends the message to the free Google Brain
    response = model.generate_content(f"You are a kind family member. Remember our history. User says: {user_input}")
    st.write(response.text)
    
    st.info("To make this photo talk for free, copy the text above and use SadTalker below.")
    st.markdown("[Open Free Video Generator](https://huggingface.co/spaces/vinthony/SadTalker)")
