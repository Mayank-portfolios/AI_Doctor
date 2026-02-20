import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

st.title("⚕️ Doctor.AI")

model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.1,
    max_tokens=None
)
prompt_template = ChatPromptTemplate([
    ("system", "You are a experience doctor"),
    ("user", "tell me the perfect cure and prediction {topic}")
])

user_input = st.text_input("Ask something:")

if st.button("Submit"):
    if user_input:
        # Format the prompt using user input
        formatted_prompt = prompt_template.invoke({"topic": user_input})
        
        # Send formatted prompt to model
        response = model.invoke(formatted_prompt)
        
        st.write("### Doctor's Advice:")
        st.write(response.content)