import streamlit as st
import google.generativeai as genai

# Securely fetch the API key from Streamlit Secrets
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
except KeyError:
    st.error("API Key not found! Please add GOOGLE_API_KEY to your Streamlit Secrets.")
    st.stop()

st.title("Family Memory AI")

# Upload Photo
photo = st.file_uploader("Upload a photo of your loved one", type=['jpg', 'png', 'jpeg'])
if photo:
    st.image(photo, width=200)

# The Conversation
user_input = st.chat_input("Talk to them...")
if user_input:
    # Sends the message to the free Google Brain
    response = model.generate_content(f"You are a kind family member. Remember our history. User says: {user_input}")
    st.write(response.text)
    
    st.info("To make this photo talk for free, copy the text above and use SadTalker below.")
    st.markdown("[Open Free Video Generator](https://huggingface.co/spaces/vinthony/SadTalker)")
