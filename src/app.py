import streamlit as st
from database import init_db, save_prompt
import random

# Initialize DB
init_db()

st.title("AI Prompt Optimizer ✨")

prompt = st.text_area("Enter your prompt to optimize:")

if st.button("Analyze"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt!")
    else:
        score = random.randint(50, 100)  # Fake smart scoring 😎
        save_prompt(prompt, score)
        st.success(f"Prompt Score: {score}/100 🎯")
        st.write("✨ Tip: More clarity + context = better results!")
