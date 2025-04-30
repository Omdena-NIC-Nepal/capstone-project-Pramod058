import streamlit as st
import spacy
from textblob import TextBlob

def show():
    # Load spaCy English model for NLP
    nlp = spacy.load("en_core_web_sm")


    st.header("Text Analysis")
    user_text = st.text_area("Enter text to analyze:", placeholder="Weather is pretty good today!")

    if st.button("Analyze Text"):
        if not user_text.strip():
            st.warning("Please enter some text for analysis.")
            return

        doc = nlp(user_text)
        tokens = [token.text for token in doc]
        lemmas = [token.lemma_ for token in doc]
        pos_tags = [token.pos_ for token in doc]
        sentiment = TextBlob(user_text).sentiment  # (polarity, subjectivity)

                # Display Sentiment
        polarity = sentiment.polarity
        subjectivity = sentiment.subjectivity

        if polarity > 0.1:
            st.success(f"Positive Sentiment 😊\nPolarity: {polarity:.2f}, Subjectivity: {subjectivity:.2f}")
        elif polarity < -0.1:
            st.error(f"Negative Sentiment 😞\nPolarity: {polarity:.2f}, Subjectivity: {subjectivity:.2f}")
        else:
            st.warning(f"Neutral Sentiment 😐\nPolarity: {polarity:.2f}, Subjectivity: {subjectivity:.2f}")

        cols1, cols2 = st.columns(2)
        with cols1:
            st.write("**Tokens:**", tokens)
            st.write("**Lemmas:**", lemmas)
        with cols2: 
            st.write("**POS Tags:**", pos_tags)

