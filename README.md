# Amazon Review Topic Modeling

This project provides an easy-to-use web application to analyze Amazon reviews using topic modeling. Users can input a review, and the system predicts the most relevant topic and its corresponding category using a trained Latent Dirichlet Allocation (LDA) model.

## Table of Contents

- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Dataset Generation](#dataset-generation)
- [Training the LDA Model](#training-the-lda-model)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project is a Flask web application that allows users to analyze Amazon reviews by predicting the review's associated topic. The topics have been mapped to different categories (e.g., `Electronics`, `Books`, `Toys`), which makes it easier to understand the sentiment and relevance of the review in the context of specific product categories.

## Technologies Used

- Python
- Flask
- Scikit-learn
- Latent Dirichlet Allocation (LDA)
- CountVectorizer
- HTML/CSS for the frontend
- Pandas (for dataset handling)
- Pickle (for model persistence)

## Project Structure

```
├── static/
├── templates/
│   └── index.html         # Frontend HTML template
├── lda_model.pkl          # Trained LDA model (saved using pickle)
├── vectorizer.pkl         # CountVectorizer (used for feature extraction)
├── app.py                 # Flask application file
├── dataset_generator.py   # Script for generating random Amazon review data
├── train_model.py         # Script for training the LDA model
└── README.md              # This readme file
```

## Setup and Installation

### Step 1: Clone the repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/your-username/amazon-review-topic-modeling.git
cd amazon-review-topic-modeling
```

### Step 2: Install the required dependencies

You need to install the required Python libraries before running the application. Make sure you have Python installed (preferably version 3.8 or later).

```bash
pip install -r requirements.txt
```

The `requirements.txt` file includes the following packages:

```txt
Flask
scikit-learn
pandas
numpy
faker
pickle-mixin
```

### Step 3: Train or Load the Model

You can either use the pre-trained model files (`lda_model.pkl` and `vectorizer.pkl`) provided in the repository, or train your own LDA model by following the steps below.

#### To Train the LDA Model:

1. Use the `dataset_generator.py` script to generate a synthetic Amazon reviews dataset.

```bash
python dataset_generator.py
```

2. Run the `train_model.py` script to train an LDA model on the dataset. This will output the trained model and vectorizer into `lda_model.pkl` and `vectorizer.pkl`, respectively.

```bash
python train_model.py
```

### Step 4: Running the Application

To start the Flask web application, run the `app.py` file:

```bash
python app.py
```

This will start a local Flask server, and you can access the web application by navigating to `http://127.0.0.1:5000` in your browser.

## Usage

1. After launching the web app, you'll see a form where you can input a review. 
2. Enter an Amazon review and click the **Analyze** button.
3. The application will return a predicted topic (like `Topic 1`, `Topic 2`, etc.) and map it to a specific product category (like `Books`, `Electronics`, or `Toys`).
4. The prediction will be displayed below the form.

### Example:

- **Input Review:** "This camera has great picture quality and long battery life."
- **Predicted Topic:** Topic 2
- **Category:** Electronics

## Dataset Generation

The `dataset_generator.py` script generates a synthetic dataset of Amazon reviews using the `Faker` library. You can specify the number of reviews to generate by editing the `num_rows` variable in the script.

```python
import pandas as pd
import random
import faker

# Initialize Faker
fake = faker.Faker()

# Define the number of rows
num_rows = 100000

# Generate random data
data = {
    'id': [i for i in range(1, num_rows + 1)],
    'text': [fake.sentence(nb_words=random.randint(5, 15)) for _ in range(num_rows)],
    'sentiment': [random.choice(['negative', 'neutral', 'positive']) for _ in range(num_rows)]
}

# Create DataFrame
df_random = pd.DataFrame(data)
df_random.to_csv('amazon_reviews.csv', index=False)
```

## Training the LDA Model

1. The LDA model is trained using the Amazon reviews dataset.
2. The `train_model.py` script loads the dataset, preprocesses the text data (removes stop words, vectorizes the text), and trains the LDA model.
3. The model and the vectorizer are saved to disk using `pickle` for later use.

```bash
python train_model.py
```

## Contributing

If you'd like to contribute to this project, feel free to create a pull request or submit an issue. We welcome any contributions that enhance the application's functionality or performance.

## License

This project is licensed under the MIT License. Feel free to modify and distribute as per the license terms.

---

### Detailed Steps:

1. **Introduction**: Brief overview of the project and its purpose.
2. **Technologies Used**: Lists the major technologies involved in the project.
3. **Project Structure**: Provides an overview of the directory structure and explains key files.
4. **Setup and Installation**: Instructions to set up the project locally, including cloning the repository, installing dependencies, and setting up the environment.
5. **Running the Application**: Instructions for running the Flask app, training the model, and using pre-trained model files.
6. **Dataset Generation**: Instructions for generating a synthetic dataset using Faker.
7. **Model Training**: Explains how to train the LDA model on the generated dataset.
8. **Contributing**: Encourages contributions from other developers and users.
9. **License**: Specifies the open-source license governing the project.

This README should guide users from setting up the environment to running the application and understanding the key components. You can adapt the content according to your project specifics.
