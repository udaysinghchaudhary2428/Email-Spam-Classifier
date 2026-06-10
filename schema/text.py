import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download("punkt_tab")
nltk.download("stopwords")

stop_words = set(stopwords.words("english"))
ps = PorterStemmer()

def transform_text(text: str):
    text = text.lower()
    text = nltk.word_tokenize(text)

    words = []

    for word in text:
        if word.isalnum():
            words.append(word)

    words = [
        ps.stem(word)
        for word in words
        if word not in stop_words
    ]

    return " ".join(words)