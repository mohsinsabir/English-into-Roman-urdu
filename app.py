import streamlit as st
from transformers import MarianMTModel, MarianTokenizer
import torch
import re

def translate_to_urdu(text):
    # Extract proper names (assuming they are capitalized)
    names = re.findall(r'\b[A-Z][a-z]*\b', text)
    
    # Replace names with placeholders
    placeholder_text = text
    for i, name in enumerate(names):
        placeholder_text = placeholder_text.replace(name, f'PLACEHOLDER{i}')
    
    # Special cases dictionary for common phrases
    special_cases = {
        "how are you": "tum kyse ho",
        "hello": "assalam o alaikum",
        "thank you": "shukriya",
        "goodbye": "allah hafiz"
    }
    
    # Check for special cases first
    text_lower = placeholder_text.lower().strip()
    if text_lower in special_cases:
        return special_cases[text_lower]

    try:
        # Initialize tokenizer and model
        model_name = "Helsinki-NLP/opus-mt-en-ur"
        tokenizer = MarianTokenizer.from_pretrained(model_name)
        model = MarianMTModel.from_pretrained(model_name)
        
        # Translate
        inputs = tokenizer(placeholder_text, return_tensors="pt", padding=True)
        outputs = model.generate(**inputs)
        translation = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Convert to Roman Urdu
        roman_translation = convert_to_roman_urdu(translation)
        
        # Replace placeholders with original names
        for i, name in enumerate(names):
            roman_translation = roman_translation.replace(f'PLACEHOLDER{i}', name)
        
        return roman_translation
    
    except Exception as e:
        return f"Translation error: {str(e)}"

def convert_to_roman_urdu(urdu_text):
    # Mapping dictionary for Urdu to Roman Urdu
    mapping = {
        'ا': 'a', 'آ': 'a', 'ب': 'b', 'پ': 'p', 'ت': 't', 'ٹ': 't', 'ث': 's',
        'ج': 'j', 'چ': 'ch', 'ح': 'h', 'خ': 'kh', 'د': 'd', 'ڈ': 'd', 'ذ': 'z',
        'ر': 'r', 'ڑ': 'r', 'ز': 'z', 'ژ': 'zh', 'س': 's', 'ش': 'sh', 'ص': 's',
        'ض': 'z', 'ط': 't', 'ظ': 'z', 'ع': 'a', 'غ': 'gh', 'ف': 'f', 'ق': 'q',
        'ک': 'k', 'گ': 'g', 'ل': 'l', 'م': 'm', 'ن': 'n', 'ں': 'n', 'و': 'o',
        'ہ': 'h', 'ھ': 'h', 'ء': "'", 'ی': 'y', 'ے': 'e', 'ئ': 'y',
        '۔': '.', '،': ',', ' ': ' '
    }
    
    # Common word replacements
    word_replacements = {
        'کیسے': 'kyse',
        'تم': 'tum',
        'ہو': 'ho',
        'کیا': 'kya',
        'ہے': 'hai',
        'میں': 'main',
        'آپ': 'aap',
        'ہیں': 'hain',
        'میرا': 'mera',
        'نام': 'naam'
    }
    
    # First try to replace common words
    for urdu_word, roman_word in word_replacements.items():
        urdu_text = urdu_text.replace(urdu_word, roman_word)
    
    # Then convert remaining characters
    result = ''
    i = 0
    while i < len(urdu_text):
        if urdu_text[i] in mapping:
            result += mapping[urdu_text[i]]
        else:
            result += urdu_text[i]
        i += 1
    
    return result.strip()

# Streamlit UI
st.set_page_config(page_title="English to Roman Urdu Translation", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    .header {
        text-align: center;
        color: #4B0082;
    }
    .input-container {
        text-align: center;
        margin-bottom: 20px;
    }
    .translation {
        border: 2px solid #4B0082;
        padding: 10px;
        background-color: #f0f0f0;
        border-radius: 5px;
        text-align: center;
    }
    .button {
        background-color: #4B0082;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
    }
    .button:hover {
        background-color: #6A5ACD;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 class='header'>English to Roman Urdu Translation</h1>", unsafe_allow_html=True)

# Input text box
input_text = st.text_area("Enter English text for translation", height=150)

# Translate button
if st.button("Translate", key="translate_button", help="Click to translate the input text"):
    if input_text:
        translation = translate_to_urdu(input_text)
        st.markdown("<h3>Translation:</h3>", unsafe_allow_html=True)
        st.markdown(f"<div class='translation'>{translation}</div>", unsafe_allow_html=True)
    else:
        st.warning("Please enter some text to translate.")

# Main function
def main():
    pass

if __name__ == "__main__":
    main()
