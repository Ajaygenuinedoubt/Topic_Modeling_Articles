from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load your LDA model and vectorizer
with open('lda_model.pkl', 'rb') as model_file:
    lda_model = pickle.load(model_file)

with open('vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Define a mapping of topics to categories based on analysis of the LDA model
topic_category_mapping = {
    0: 'Electronics',
    1: 'Books',
    2: 'Toys',
    3: 'Clothing',
    4: 'Home and Kitchen',
    5: 'Sports and Outdoors',
    6: 'Beauty and Health',
    7: 'Automotive',
    8: 'Pet Supplies',
    9: 'Baby Products'
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        review_text = request.form['review']
        
        # Transform the input text using the vectorizer
        X_new = vectorizer.transform([review_text])
        
        # Get the topic distribution for the document
        topic_distribution = lda_model.transform(X_new)
        
        # Find the topic with the highest probability
        topic_number = np.argmax(topic_distribution)
        
        # Get the category from the mapping
        category = topic_category_mapping.get(topic_number, 'Unknown Category')
        
        # Display the topic and the related category
        topic_label = f"Topic {topic_number + 1}"
        
        return render_template('index.html', prediction=topic_label, category=category)

if __name__ == '__main__':
    app.run(debug=True)
