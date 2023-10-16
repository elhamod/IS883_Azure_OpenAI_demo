# azure.py
# Import necessary libraries
import streamlit as st
import openai
import os
# A comment
# Set up your OpenAI API key
openai.api_key = os.environ.get('OPENAI_API_KEY')
# Initialize Streamlit
st.title("This is such an awesome app!")

# Add a slider to control the temperature
temperature = st.slider('Temperature', min_value=0.0, max_value=1.0, value=0.7, step=0.05)
st.write(f'You selected a temperature of: {temperature}')

# Create a text input field for user queries
user_input = st.text_input("Ask a question:")

# Send the user's query to OpenAI GPT-3
if user_input:
    response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=user_input,
    max_tokens=50,
    temperature=temperature  # Use the temperature from the slider
    )
    st.write(response['choices'][0]['text'].strip())
