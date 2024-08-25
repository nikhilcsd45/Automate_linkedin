import nltk   # good for  topic content
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from scipy.spatial.distance import cosine

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    tokens = nltk.word_tokenize(text.lower())
    tokens = [token for token in tokens if token.isalnum() and token not in stop_words]
    return " ".join(tokens)

def get_similarity(text1, text2):
    preprocessed_text1 = preprocess_text(text1)
    preprocessed_text2 = preprocess_text(text2)
    
    vectorizer = CountVectorizer().fit_transform([preprocessed_text1, preprocessed_text2])
    vectors = vectorizer.toarray()
    similarity = 1 - cosine(vectors[0], vectors[1])
    return similarity

text1 = "This is a sentence."
text2 = "This is another sentence."
similarity_score = get_similarity(text1, text2)
print(f"Cosine similarity between '{text1}' and '{text2}': {similarity_score}")




