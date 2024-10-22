import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load your translation model (Update model_name with your fine-tuned model or pre-trained model)
model_name = "t5-small"  # Replace with the model you have fine-tuned or a valid Hugging Face model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Streamlit UI
st.title("English to Roman Urdu Translation")
st.write("Enter an English prompt to get its Roman Urdu translation.")

# User input
english_text = st.text_input("Enter English Text:")

# Translation logic
if st.button("Translate"):
    if english_text:
        with st.spinner("Translating..."):
            try:
                # Tokenize the input
                inputs = tokenizer.encode_plus(english_text, return_tensors="pt", padding=True, truncation=True)
                
                # Generate the translated output
                outputs = model.generate(inputs["input_ids"])
                
                # Decode the output
                roman_urdu_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
                
                # Display the translation
                st.success(f"Roman Urdu Translation: {roman_urdu_text}")
            except Exception as e:
                st.error(f"Error occurred: {e}")
    else:
        st.warning("Please enter text for translation.")

