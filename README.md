## English → Roman Urdu Translator (Streamlit)

Translate English text to Roman Urdu in your browser. This app uses a Hugging Face MarianMT model to translate English → Urdu and then converts that Urdu text to Roman Urdu with simple, readable transliteration rules. Proper names are preserved via placeholders, and a few common phrases are handled with special cases.

### Features
- **Streamlit UI**: Simple text area + Translate button.
- **Neural translation**: Uses `Helsinki-NLP/opus-mt-en-ur` from Hugging Face.
- **Roman Urdu output**: Lightweight character and word mapping for readable Roman Urdu.
- **Name preservation**: Naive placeholder logic keeps capitalized names intact.
- **MIT licensed**.

### Project structure
- `app.py` — Streamlit app and translation logic
- `requirements.txt` — Python dependencies
- `LICENSE` — MIT License

### Quick start
1) Create a virtual environment and install dependencies

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2) Run the app

```bash
streamlit run app.py
```

3) Use it
- Open the local URL printed by Streamlit.
- Enter English text and click "Translate".
- Read the Roman Urdu translation in the results box.

### How it works
- `translate_to_urdu(text)`
  - Extracts capitalized words as candidate names and replaces them with placeholders.
  - Checks a small set of special-case phrases (e.g., "how are you").
  - Loads `MarianTokenizer` and `MarianMTModel` for `Helsinki-NLP/opus-mt-en-ur` and generates Urdu translation.
  - Converts the Urdu text to Roman Urdu via `convert_to_roman_urdu` (character mapping + common word replacements).
  - Restores original names by replacing placeholders back.

- Streamlit UI (`app.py`)
  - Custom minimal CSS for styling.
  - Text area for input and a button to trigger translation.

### Requirements
- Python 3.8+
- Packages: `streamlit`, `transformers`, `torch`, `sentencepiece` (installed via `requirements.txt`).
- Internet access needed on first run to download the Hugging Face model weights and tokenizer.

### Notes and limitations
- **Name detection is naive**: Any capitalized word is treated as a name.
- **Roman Urdu mapping is approximate**: It aims for readability, not linguistic perfection.
- **Cold start**: Model and tokenizer load on translate; consider caching for speed.

### Possible improvements
- Cache model/tokenizer with `st.cache_resource` to avoid repeated loads.
- Improve name detection using NER.
- Expand Roman Urdu mappings and phrase dictionary.
- Add tests and CI.

### License
This project is licensed under the MIT License — see `LICENSE` for details.

### Acknowledgements
- Translation model: `Helsinki-NLP/opus-mt-en-ur` on Hugging Face.