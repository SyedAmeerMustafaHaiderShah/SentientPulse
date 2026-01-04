import re
import string
import joblib
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Load saved artifacts
tfidf_bigram = joblib.load('models/tfidf_vectorizer.pkl')
nb_bigram = joblib.load('linear_svm_model.pkl')

# Preprocessing tools
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def predict_sentiment_batch(sentence_list):
    """
    MODIFIED:accepts a LIST of sentences and returns a LIST of predictions.
    """
    if not isinstance(sentence_list, list):
        # Fallback: if a single string is passed, wrap it in a list
        sentence_list = [sentence_list]

    clean_sentences = []

    # Loop through the batch to clean each sentence
    for text in sentence_list:
        # 1. lowercase
        text = text.lower()

        # 2. normalize apostrophes
        text = text.replace("’", "'")

        # 3. remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))

        # 4. remove numbers
        text = re.sub(r'\d+', '', text)

        # 5. remove stopwords and 6. lemmatization
        tokens = [lemmatizer.lemmatize(word) for word in text.split() if word not in stop_words]
        
        clean_text = " ".join(tokens)
        clean_sentences.append(clean_text)

    # 7. TF-IDF bigram transform (The whole list at once!)
    # No more [clean_text] wrapper here because clean_sentences is already a list
    vector_matrix = tfidf_bigram.transform(clean_sentences)

    # 8. Predict sentiment for the whole batch
    # We remove the [0] so it returns all predictions
    predictions = nb_bigram.predict(vector_matrix)

    return list(predictions)