import streamlit as st
import joblib
import os
import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Setup
nltk.download('vader_lexicon', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    return " ".join([lemmatizer.lemmatize(w) for w in text.split() if w not in stop_words])

@st.cache_resource
def load_model():
    # Looks for 'models/clf_tone.pkl' in the root
    return joblib.load('models/clf_tone.pkl')

model = load_model()
sia = SentimentIntensityAnalyzer()

st.title("Customer Service Auditor")
transcript = st.text_area("Paste Transcript")
if st.button("Analyze"):
    cleaned = clean_text(transcript)
    prob = model.predict_proba([cleaned])[0][1]
    st.metric("Tone Risk", f"{prob:.2%}")
