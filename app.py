import streamlit as st
from prompts import build_prompt
from generator import generate_text

st.set_page_config(
    page_title="Generator tekstów",
    page_icon="📝"
)

st.title("Generator tekstów")

topic = st.text_input("Temat tekstu")

text_length = st.number_input(
    "Docelowa liczba słów",
    min_value=50,
    max_value=1000,
    value=200,
    step=50
)

st.subheader("Parametry stylu")

sentence_variability = st.slider(
    "Zmienność długości zdań",
    min_value=1,
    max_value=5,
    value=3
)

structure_regularity = st.slider(
    "Regularność struktury",
    min_value=1,
    max_value=5,
    value=3
)

language_smoothness = st.slider(
    "Wygładzenie języka",
    min_value=1,
    max_value=5,
    value=3
)

tone_profile = st.slider(
    "Profil tonu",
    min_value=1,
    max_value=5,
    value=3
)

if st.button("Generuj"):
    prompt = build_prompt(
        topic=topic,
        text_length=text_length,
        sentence_variability=sentence_variability,
        structure_regularity=structure_regularity,
        language_smoothness=language_smoothness,
        tone_profile=tone_profile
    )

    with st.spinner("Generowanie tekstu..."):
        generated_text = generate_text(prompt)

    st.subheader("Wygenerowany tekst")
    st.write(generated_text)

    with st.expander("Pokaż prompt"):
        st.text_area(
            "Prompt wysłany do modelu",
            value=prompt,
            height=300
        )