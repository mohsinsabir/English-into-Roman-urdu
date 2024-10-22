import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load your translation model (you can modify the model name as needed)
model_name = "HuggingFaceModelForRomanUrdu"  # Replace with the model you fine-tune or select
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Streamlit UI
st.title("English to Roman Urdu Translation")
st.write("Enter an English prompt to get its Roman Urdu translation.")

# User input
english_text = st.text_input("Enter English Text:")

# Translation
if st.button("Translate"):
    if english_text:
        inputs = tokenizer.encode(english_text, return_tensors="pt", padding=True)
        outputs = model.generate(inputs)
        roman_urdu_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        st.write(f"Roman Urdu Translation: {roman_urdu_text}")
    else:
        st.write("Please enter text for translation.")
