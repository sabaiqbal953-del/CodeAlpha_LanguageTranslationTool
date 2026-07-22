import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS

st.set_page_config(page_title="Language Translator", page_icon="🌐")
st.title("🌐 Language Translation Tool")
st.write("Text likho, language select karo, aur translate button dabao")

languages = {
    "English": "en",
    "Urdu": "ur",
    "Arabic": "ar",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Chinese": "zh-CN",
    "Hindi": "hi",
    "Turkish": "tr"
}

input_text = st.text_area("Apna text yahan likhein:", height=150)

col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("Source Language", list(languages.keys()), index=0)
with col2:
    target_lang = st.selectbox("Target Language", list(languages.keys()), index=1)

if st.button("Translate 🔄"):
    if input_text.strip() == "":
        st.warning("Pehle kuch text likhein!")
    else:
        try:
            translated = GoogleTranslator(
                source=languages[source_lang],
                target=languages[target_lang]
            ).translate(input_text)

            st.success("Translation Complete!")
            st.text_area("Translated Text:", value=translated, height=150)
            st.code(translated, language=None)

            if st.checkbox("🔊 Sunna chahte hain? (Text-to-Speech)"):
                tts = gTTS(text=translated, lang=languages[target_lang])
                tts.save("output.mp3")
                audio_file = open("output.mp3", "rb")
                st.audio(audio_file.read(), format="audio/mp3")

        except Exception as e:
            st.error(f"Error aayi: {e}")