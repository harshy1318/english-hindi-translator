import streamlit as st
import requests

st.set_page_config(
    page_title="English → Hindi Translator",
    page_icon="🇮🇳"
)

st.title("🤖 English → Hindi Translator")
st.write("Translate any English word or sentence into Hindi")

def translate(text):
    url = "https://libretranslate.de/translate"
    data = {
        "q": text,
        "source": "en",
        "target": "hi",
        "format": "text"
    }
    response = requests.post(url, data=data)
    return response.json()["translatedText"]

text = st.text_area("Enter English text")

if st.button("Translate"):
    if text.strip():
        try:
            result = translate(text)
            st.subheader("🇮🇳 Hindi Meaning")
            st.success(result)
        except:
            st.error("Translation failed. Try again later.")
    else:
        st.warning("Please enter some text")
